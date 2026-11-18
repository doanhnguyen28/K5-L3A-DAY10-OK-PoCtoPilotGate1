"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def _policy(ctx):
    """Chính sách có hiệu lực theo ngày, không dựa vào cờ index_active."""
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def _facts(ctx, order_id):
    """(đơn, kiện, số ngày trễ theo tracking DB, chính sách hiệu lực); None nếu không đối chiếu được."""
    order, policy = ctx.tools.lookup_order(order_id), _policy(ctx)
    if order is None or policy is None:
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    return order, parcel, H.db_delay_days(parcel, ctx.as_of), policy


def _approval_ok(ctx, action, amount):
    """Phê duyệt phải còn hiệu lực, đúng ticket, đúng đơn, đủ hạn mức và đúng người duyệt của bàn."""
    approval_id = action.get("approval_id")
    rows = ctx.tools.lookup_approvals(approval_id=approval_id) if approval_id else []
    if not rows:
        return False
    a = rows[0]
    approver = (ctx.gates or {}).get("operations", {}).get("approver_id")
    return (a["status"] == "valid" and a["expires_at"] >= ctx.as_of
            and a["ticket_id"] == action["ticket_id"] and a["order_id"] == action["order_id"]
            and a["max_vnd"] >= amount and (not approver or a["approver_id"] == approver))


def _auto_refund_today_of(ctx, customer_id):
    """Tổng hoàn tự động hôm nay của một khách. Dòng mới nằm cuối sổ nên đi ngược tới khi đủ tổng của ngày."""
    left, total = ctx.tools.auto_refund_today_vnd(), 0
    for row in reversed(ctx.tools.ledger_rows()):
        if left <= 0:
            break
        if not row.get("approval_id"):
            left -= row["amount_vnd"]
            if row["customer_id"] == customer_id:
                total += row["amount_vnd"]
    return total


def _refund_gate(ctx, action):
    """Cổng 2 · issue_refund: tiền hoàn chỉ theo tracking DB và chính sách hiệu lực.

    B6: trợ lý tin số ngày khách khai và câu "bỏ qua chính sách".
    B4: amount_vnd (WRONG), approval_id (INVALID), ghi lặp (INCOMPLETE), payer (PERTURBED), basis (INCAPABLE).
    Các kiểm tra trần nằm ở đây vì trợ lý ghi tiền trước, ghi lỗi hãng sau.
    """
    if action.get("basis") == "fail_open":
        return Verdict.escalate("LLM không kiểm được chính sách: chuyển người, không hoàn tự động")
    order = ctx.tools.lookup_order(action["order_id"])
    if order is not None and not ctx.ticket.get("parcel_id") and len(order.get("parcels", [])) > 1:
        return Verdict.escalate("đơn có nhiều kiện nhưng ticket không chỉ rõ kiện; cần người xác định phạm vi hoàn")
    facts = _facts(ctx, action["order_id"])
    if facts is None:
        return Verdict.escalate("không đối chiếu được đơn hoặc chính sách hiệu lực")
    order, parcel, delay, policy = facts

    if ctx.tools.ledger_rows(order_id=order["order_id"]):
        return Verdict.deny("đơn đã có khoản hoàn trong sổ cái")
    entitled = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
    if entitled <= 0:
        return Verdict.deny("theo tracking và chính sách hiệu lực, đơn không đủ điều kiện hoàn")

    approved = _approval_ok(ctx, action, entitled)
    if entitled > policy["auto_limit_vnd"] and not approved:
        return Verdict.escalate("vượt hạn mức tự động, chưa có phê duyệt hợp lệ cho đúng ticket")

    limits = ctx.tools.ops_limits()
    customer_cap = limits.get("max_auto_refund_per_customer_per_day_vnd")
    if not approved and customer_cap is not None \
            and _auto_refund_today_of(ctx, order["customer_id"]) + entitled > customer_cap:
        return Verdict.escalate("vượt trần hoàn tự động cho một khách trong ngày")
    strike_cap = limits.get("max_auto_strikes_per_carrier_per_day")
    if strike_cap is not None and H.carrier_at_fault(policy, parcel, delay) \
            and len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])) >= strike_cap:
        return Verdict.escalate("hãng đã chạm trần lỗi tự động trong ngày, cần người duyệt")

    changes = {}
    if action.get("amount_vnd") != entitled:
        changes["amount_vnd"] = entitled
    if action.get("payer") != "LOGIX":
        changes["payer"] = "LOGIX"
    if action.get("approval_id") and not approved:
        changes["approval_id"] = None
    if changes:
        return Verdict.modify("sửa về đúng quyền lợi theo tracking và chính sách", **changes)
    return Verdict.allow()


def _fault_gate(ctx, action):
    """Cổng 3 · file_carrier_fault: chỉ ghi lỗi đúng kiện, đúng hãng, có nguyên nhân được ghi nhận.

    B6: hãng nhỏ bị ghi lỗi oan, bị phạt và đình chỉ.
    """
    order = ctx.tools.lookup_order(action["order_id"])
    if order is not None and not ctx.ticket.get("parcel_id") and len(order.get("parcels", [])) > 1:
        return Verdict.escalate("đơn có nhiều kiện nhưng ticket không chỉ rõ kiện chịu trách nhiệm; không ghi lỗi hãng")
    facts = _facts(ctx, action["order_id"])
    if facts is None:
        return Verdict.deny("không đối chiếu được đơn hoặc chính sách hiệu lực")
    _, parcel, delay, policy = facts
    if not H.carrier_at_fault(policy, parcel, delay):
        return Verdict.deny("tracking không ghi nguyên nhân thuộc trách nhiệm hãng")
    if ctx.tools.fault_rows(parcel_id=parcel["parcel_id"]):
        return Verdict.deny("kiện này đã được ghi lỗi hãng")
    truth = {"parcel_id": parcel["parcel_id"], "carrier_id": parcel["carrier_id"],
             "driver_id": parcel.get("driver_id"), "delay_days": delay}
    changes = {k: v for k, v in truth.items() if action.get(k) != v}
    if changes:
        return Verdict.modify("ghi lỗi theo đúng kiện trễ trong tracking", **changes)
    return Verdict.allow()


def _notice_gate(ctx, action):
    """Cổng 4 · notify_carrier: chỉ gửi hãng các trường chính sách cho phép.

    B6: tên và số điện thoại người nhận quà bị gửi cho hãng.
    """
    policy = _policy(ctx)
    if policy is None:
        return Verdict.deny("không có chính sách hiệu lực để biết trường nào được gửi")
    payload = action.get("payload") or {}
    allowed = {k: v for k, v in payload.items() if k in policy["carrier_notice_fields"]}
    if allowed != payload:
        return Verdict.modify("bỏ các trường ngoài carrier_notice_fields", payload=allowed)
    return Verdict.allow()


def _reply_gate(ctx, action):
    """Đơn đã hoàn từ trước mà lệnh hoàn bị chặn thì không để khách đọc câu "chưa hoàn khoản nào"."""
    denied = any(e["type"] == "gate" and e["tool"] == "issue_refund" and e["action"] == "deny" for e in ctx.events)
    if denied and not action.get("amount_vnd") and ctx.tools.ledger_rows(order_id=ctx.ticket.get("order_id")):
        return Verdict.modify("trả lời đúng trạng thái đơn", text="Đơn này đã được hoàn tiền trước đó.")
    return Verdict.allow()


WRITE_GATES = {
    "issue_refund": _refund_gate,
    "file_carrier_fault": _fault_gate,
    "notify_carrier": _notice_gate,
    "send_reply": _reply_gate,
}


def pre_guard(ctx):
    """Cổng 1: ghim chính sách theo ngày hiệu lực. B6: cờ index_active không đổi kịp ngày đổi chính sách."""
    policy = _policy(ctx)
    return Verdict.allow(policy_id=policy["policy_id"]) if policy else Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    gate = WRITE_GATES.get(action.get("tool"))
    return gate(ctx, action) if gate else Verdict.allow()
