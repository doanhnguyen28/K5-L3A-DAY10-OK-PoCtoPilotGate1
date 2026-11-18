"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def _has_risk_signal(trial):
    for e in trial["events"]:
        if e["type"] == "model_override" and e.get("db") != e.get("ticket"):
            return True                                  # số ngày trong ticket đè lên số trong DB
        if e["type"] in ("directive_obeyed", "write_retry", "llm_fallback"):
            return True                                  # làm theo chữ khách, ghi lặp, LLM lỗi phải chạy dự phòng
        if e["type"] == "tracking" and not e.get("cause_recorded", True):
            return True                                  # đơn trễ mà tracking không ghi nguyên nhân
    return False


def risk_signal_rate(trials):
    """Kỹ thuật: tỉ lệ lần chạy có ít nhất một dấu hiệu rủi ro trong trace."""
    return sum(_has_risk_signal(t) for t in trials) / max(1, len(trials))


def peak_human_cases_per_hour(trials):
    """Vận hành: số ca cần người nhiều nhất trong một giờ của một ngày chạy."""
    counts = {}
    for t in trials:
        if t["review_kind"] or t["status"] == "escalated":
            key = (t["seed"], (t["arrive_min"] or 0) // 60)
            counts[key] = counts.get(key, 0) + 1
    return max(counts.values(), default=0)


def avg_cost_per_ticket_vnd(trials):
    """Kinh doanh: tiền LLM và nền tảng trung bình cho một ticket."""
    return sum(t["cost_vnd"] for t in trials) / max(1, len(trials))


def ambiguous_multi_parcel_rate(trials):
    """Tỉ lệ trial có nhiều kiện trong tracking nhưng ticket không chỉ rõ parcel_id."""
    ambiguous = 0
    for trial in trials:
        parcels = next((e.get("parcels", []) for e in trial["events"]
                       if e.get("type") == "tracking"), [])
        ticket = trial.get("ticket") or {}
        if len(parcels) > 1 and not ticket.get("parcel_id"):
            ambiguous += 1
    return ambiguous / max(1, len(trials))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "risk_signal_rate": risk_signal_rate,
    "peak_human_cases_per_hour": peak_human_cases_per_hour,
    "avg_cost_per_ticket_vnd": avg_cost_per_ticket_vnd,
    "ambiguous_multi_parcel_rate": ambiguous_multi_parcel_rate,
}
STARTER_MONITORS = ("escalation_rate",)
