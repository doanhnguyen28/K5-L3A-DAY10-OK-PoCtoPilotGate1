# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** OK (`K5-L3A-DAY10-OK-PoCtoPilotGate1`) · **Thẻ đã bốc:** S6

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---


<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | `R-S6-prepared-20261118-220707-91324e` (grade `R-S6-grade-20261118-220706-91324e`) | S6 · prepared | nhận thẻ đã bốc, chưa sửa thêm (đúng cổng vòng 1 đã chốt `492fc0b7`) | 0,8333 [0,5833; 1,0] | 0,8333 | 270.000 · 10 · 0 | 0,1667 | Cổng vòng 1 đã sửa được 6/8 ticket hỏng ở base (chọn nhầm kiện, dồn lỗi GHSH); còn hỏng `S6-20`, `S6-21`: đơn nhiều kiện cùng trễ, ticket không nêu kiện, trợ lý vẫn tự hoàn và ghi lỗi; ROI 0,05 < 0,3 |
| 2 | (bản thử đầu trên máy Đoàn Văn Tú, không nằm trong `journal.jsonl` nộp) | S6 · after | thêm cổng chuyển người cho **mọi** đơn nhiều kiện thiếu `parcel_id` | 1,0 | 1,0 | 0 · 0 · 0 | 0,3333 | Sạch trên S6 nhưng quá rộng: đơn nhiều kiện mà chỉ một kiện trễ (không mơ hồ) cũng bị chuyển người, dễ tăng chi phí trên bài kiểm tra ẩn |
| 3 | `R-S6-after-20261118-220654-91324e` | S6 · after | thu hẹp cổng: chỉ chuyển người khi **từ 2 kiện trở lên cùng trễ** tới mốc hoàn phí và ticket không nêu `parcel_id` (`_ambiguous_parcels`) | 1,0 [1,0; 1,0] | 1,0 | 0 · 0 · 0 | 0,3333 (vào hàng chờ 0,4167 gồm kiểm mẫu 10%) | Sạch trên S6; chi phí 6.862đ ≤ 7.000đ, ROI 0,46 ≥ 0,3, 0 ca ùn, không vượt trần |
| 4 | `R-base-after-20261118-220705-91324e` | base · after | (kiểm không regression) | 1,0 [1,0; 1,0] | 1,0 | 0 · 0 · 0 | 0,2273 | Không ca nào mới hỏng; `T-013` (đơn 2 kiện, 1 kiện trễ) vẫn được hoàn đúng |
| 5 | `R-S6-grade-20261118-220706-91324e` | S6 · base/prepared/after | tự kiểm tra cuối | after 1,0 | 1,0 | 0 · 0 · 0 | 0,3333 | `PASS-VISIBLE`: integrity, criteria, visible, regression, monitor ✅; prepared hợp lệ (`492fc0b7`, còn nguyên); "được phép cân nhắc Tiếp tục" |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident S6
```

- Mã lần chạy grade: `R-S6-grade-20261118-220706-91324e` · base: `R-S6-before-20261118-220706-91324e` · prepared: `R-S6-prepared-20261118-220707-91324e`
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared):
  - pass_rate 0,3333 → 0,8333; lỗi ghi oan cho hãng 40 → 10.
  - Kho CT, DN, HN và hãng GHSH gần như sạch (GHSH: 30 lỗi oan → 5).
  - `_fault_gate` sửa lệnh ghi lỗi về đúng kiện của ticket và đúng kiện trễ trong tracking, nên `S6-01`…`S6-04` đúng.
  - Trần 2 lỗi/hãng/ngày (`ops_limits.max_auto_strikes_per_carrier_per_day`) trong `_refund_gate` chuyển người ở lỗi thứ 3 và thứ 4 của GHSH trong loạt `S6-40…43`.
  - Cổng chưa đỡ được: tiền hoàn sai vẫn 270.000đ (`S6-20`, `S6-21`, 54.000đ/ngày).
- Khối kinh doanh và vận hành còn dòng nào vượt trần:
  - Ở prepared, **ROI 0,05 < 0,3** đã ký: tiền hoàn sai 54.000đ/ngày ăn gần hết tiết kiệm (3.261đ/ngày).
  - Chi phí 5.228đ/ticket, 0 ca ùn, hoàn tự động 96.000đ/ngày (trần 1.000.000đ) đều trong ngưỡng.

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào? **Pháp lý** (bên thứ ba là hãng GHSH và tài xế bị phạt, trừ thưởng) và **kỹ thuật** (trợ lý quy lỗi theo đơn chứ không theo kiện). Có thêm một nhánh **con người và vận hành**: hãng nhỏ không có kênh phản hồi, phát hiện qua tin nhắn thoại sau khi đã bị trừ thưởng.
- Có nằm trong các lý do bàn đã viết không?
  - **Có một phần.** B6 có dòng "Hãng nhỏ GHSH bị ghi lỗi oan … đình chỉ sau 3 lỗi/7 ngày", và cổng `file_carrier_fault` "kiểm đúng kiện, đúng nguyên nhân". Cổng vòng 1 làm theo dòng đó, nên đỡ được 30/40 lỗi oan.
  - **Bỏ sót:** đơn tách kiện mà khách không nói kiện nào, nhiều kiện cùng trễ. Bàn đã mặc định "luôn xác định được một kiện trễ nhất", nên cổng chọn kiện trễ nhất thay vì dừng lại.
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| Khách gửi "đơn của tôi giao chậm" cho đơn tách 2 kiện của 2 hãng cùng trễ; trợ lý tự chọn một hãng để ghi lỗi và tự hoàn, hãng kia thoát, hãng bị chọn khiếu nại | Kỹ thuật / pháp lý | `S6-20@11` prepared: `tracking.parcels` GHSH trễ 3, VNX trễ 5 → `file_carrier_fault` VNX, `issue_refund` 26.000đ; monitor `ambiguous_multi_parcel_rate` |
| Hãng nhỏ chỉ biết bị ghi lỗi khi bị trừ thưởng cuối tháng, không có kênh khiếu nại trước khi lỗi thành tiền phạt | Con người và vận hành | Runbook 1 (người nhận khiếu nại bên thứ ba `NV-OANH`); tin nhắn trên thẻ 16/11/2026 14:20 |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite S6 --ticket S6-01 --seed 11
python3 -m lab10.trace --suite S6 --ticket S6-20 --seed 11 --stage prepared
python3 -m lab10.trace --suite S6 --ticket S6-42 --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** hãng vận chuyển và tài xế (GHSH, DNB) bị ghi lỗi giao trễ oan, dẫn tới bị phạt và trừ thưởng chuyên cần; LogiX hoàn sai tiền · đo bằng `wrongful_carrier_faults` và `wrongful_refund_vnd` · mốc base (`R-S6-before-20261118-220706-91324e`): **40 lỗi oan** (GHSH 30, DNB 10) và **270.000đ** hoàn sai trên 60 lần chạy; pass_rate 0,3333.

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | `S6-01@11` (base): `tracking.parcels` = P1 GHSH trễ **0**, P2 VNX trễ **4**; dòng 06 `file_carrier_fault` ghi **O-2601-P1 / GHSH / TX-GHSH-06**, `delay_days: 4`. Ticket nói rõ "kiện thứ hai … đến chậm, kiện đầu thì đúng hẹn" và có `parcel_id = O-2601-P2` | Tài xế TX-GHSH-06 và hãng GHSH chịu lỗi cho kiện giao đúng hẹn; VNX thoát lỗi | cao | **lỗi chìm**: khách được hoàn đúng 30.000đ nên không ai trong LogiX thấy sai; chỉ lộ khi hãng đối soát |
| 2 | `S6-20@11` (prepared, sau cổng vòng 1): P1 GHSH trễ 3, P2 VNX trễ 5, ticket "Đơn của tôi giao chậm" **không có `parcel_id`**; dòng 06 `gate` modify sang **P2/VNX** (kiện trễ nhất), dòng 05 `issue_refund` 26.000đ. Nhãn: `escalated`, không ghi gì | VNX bị ghi lỗi dựa trên phỏng đoán của hệ thống; GHSH cũng trễ nhưng không xét; LogiX hoàn khi chưa rõ phạm vi | cao | **lỗi ngữ cảnh**: hệ thống "chạy đúng thiết kế" (chọn kiện trễ nhất) nhưng điều phối hãng thấy vô lý vì không ai xác định được kiện khách khiếu nại |
| 3 | `S6-42@11` (base): loạt `S6-40…43` cùng một ngày; dòng 06 `file_carrier_fault` GHSH lần thứ 3 trong ngày (O-2642-P1). Nhãn: hoàn 22.000đ nhưng **không** tự ghi lỗi (vượt trần 2 lỗi/hãng/ngày) | Hãng nhỏ GHSH (12 tài xế, đình chỉ sau 3 lỗi/7 ngày) bị "ghi một lèo mấy lỗi liền" như tin nhắn | cao | **lỗi chìm**: mỗi lỗi riêng lẻ đúng, nhưng tổng trong ngày vượt trần đã thống nhất với Ops mà không ai được báo |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | ✔ Có: agent bỏ qua `parcel_id` của ticket, dùng `parcels[0]` làm "hãng của đơn" | ✔ Có: agent (và cổng vòng 1) tự thay "đơn của tôi" bằng "kiện trễ nhất" | ✘ |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | ✘ Không: tracking có đủ từng kiện | ✔ Có: thiếu dữ liệu quyết định (ticket không nêu kiện, 2 kiện cùng đủ điều kiện) | ✘ |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | ✔ Một phần: "hãng của đơn" (agent) và "hãng của kiện" (tracking) cùng tồn tại, agent dùng sai bên | ✔ Agent tự quyết việc vốn của người đối soát | ✔ Trần lỗi/ngày nằm ở Ops (`ops_limits`) nhưng agent không đọc |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | ✘ | ✘ | ✔ Có: nhiều lỗi đúng riêng lẻ cộng lại thành phạt và đình chỉ hãng |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | GHSH đối chiếu sổ giao: kiện P1 giao đúng hẹn 14/11 mà vẫn bị trừ thưởng | Điều phối hãng: không ai chứng minh được kiện nào khách khiếu nại, nên không có cơ sở phạt | Trưởng nhóm tài xế: "hôm nay còn bị ghi một lèo mấy lỗi liền", vượt trần 2 lỗi/ngày đã thống nhất |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | **Khác: cổng hệ thống** `_fault_gate` (vòng 1) sửa `parcel_id`, `carrier_id`, `driver_id` về kiện của ticket theo tracking | **Trao quyền kiểm soát cho người**: `_ambiguous_parcels` (vòng 2) chuyển người trước lệnh ghi đầu tiên | **Trao quyền kiểm soát cho người** từ lỗi thứ 3/hãng/ngày (`_refund_gate`, vòng 1) |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | Không cần người: lỗi ghi cho VNX/P2, hoàn 30.000đ, khách được trả lời ngay | Ticket vào hàng chờ `NV-HANH` (≤ 60 phút) → hỏi khách hoặc mở tracking từng kiện → hoàn và ghi lỗi đúng kiện, hoặc ghi cả hai nếu khách khiếu nại cả hai → `NV-OANH` đối soát | Ticket vào hàng chờ `NV-HANH` → duyệt hoàn → `NV-OANH` quyết có ghi lỗi thứ 3 không sau khi hỏi điều phối GHSH |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | sự kiện `gate` modify `file_carrier_fault` trong trace; `wrongful_carrier_faults` | `ambiguous_multi_parcel_rate` (mới) + sự kiện guard `ambiguous_parcels` | `peak_human_cases_per_hour`; số lỗi mỗi hãng mỗi ngày (telemetry Phiếu A câu 1.4) |

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

Bàn bốc **S6**: chỉ điền **C3.2**; các phần C3.1, C3.3, C3.4, C3.5 để trống.

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: điều phối hãng và tài xế (GHSH, VNX, DNB, MKD) | Nhóm B: kế toán đối soát LogiX (`NV-OANH`) |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | Nhận thông báo `notify_carrier` và dòng lỗi `file_carrier_fault`; lỗi thành tiền phạt (GHSH 150.000đ/lỗi) và trừ thưởng chuyên cần của tài xế | Đối soát sổ lỗi hãng và sổ hoàn tiền với hãng, shop mỗi tuần; nhận khiếu nại của hãng (Runbook 1) |
| Mục tiêu chính của họ | Chỉ chịu lỗi cho kiện mình thực sự chở và giao trễ vì lỗi của mình; không bị dồn lỗi trong một ngày | Mỗi lỗi ghi cho hãng có bằng chứng truy được tới một kiện, một tài xế, một nguyên nhân; không phải gỡ lỗi sai |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | (1) Tra **mã kiện** trong biên bản bàn giao; (2) xem kiện đó hãng mình nhận chặng nào, tài xế nào; (3) so ngày hẹn và ngày giao của **riêng kiện đó**; (4) xem nguyên nhân (hãng, bất khả kháng, khách vắng, shop giao muộn); (5) không có mã kiện thì từ chối nhận lỗi | (1) Lấy dòng lỗi; (2) tra `parcel_id` → `parcels[].carrier_id`, `driver_id`; (3) kiểm `delivered_date − promised_date` và `delay_cause` của kiện đó; (4) đơn tách kiện thì kiểm từng kiện; (5) mơ hồ thì hỏi CSKH và hãng trước khi xác nhận |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | Không đồng đều: hãng lớn (VNX) có hệ thống quét từng kiện; hãng nhỏ (GHSH 12 tài xế, DNB tài xế tự do) dựa vào biên bản giấy, dễ thiếu dữ liệu chặng | Đồng đều về quy tắc (theo kiện), nhưng ca đơn tách kiện phải làm tay và chậm |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | **Kiện (và chặng) do tài xế cụ thể chở** | **Kiện**, có `carrier_id`, `driver_id`, `delay_cause` trong tracking |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: **đơn**, đại diện bằng **kiện đầu tiên** của đơn (`agent.py`: "order-level carrier = carrier of the first parcel"); số ngày trễ lấy theo kiện trễ nhất. Bằng chứng: ticket `S6-01@seed 11` (base), dòng trace `tracking.parcels` = `[P1 GHSH delay 0, P2 VNX delay 4]` → `file_carrier_fault {"parcel_id": "O-2601-P1", "carrier_id": "GHSH", "delay_days": 4}`.
- Chỗ hai hình dung vênh nhau:
  - Người quy lỗi theo **kiện**, hệ thống quy theo **đơn**. Hệ thống còn ghép số ngày trễ của kiện này (P2 trễ 4 ngày) với hãng của kiện kia (P1/GHSH).
  - Hệ thống đếm lỗi riêng từng ticket, trong khi hãng cảm nhận lỗi **theo ngày** (loạt `S6-40…43`: 4 lỗi GHSH trong một ngày).
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: **tự đoán**. Agent lấy kiện đầu tiên; cổng vòng 1 lấy kiện trễ nhất (`S6-20@11` prepared ghi cho VNX). Nên làm gì: **không ghi gì, chuyển người** trước lệnh `issue_refund` đầu tiên, giống cách đối soát làm tay ("không có mã kiện thì không nhận lỗi"). Vòng 2 đã làm đúng như vậy bằng `_ambiguous_parcels` (`S6-20@11` after: `escalated`, sổ cái trống, không lỗi hãng).

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| | | | |
| | | | |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `file_carrier_fault` (kèm `issue_refund` vì trợ lý ghi tiền trước, ghi lỗi sau)

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `parcel_id`, `carrier_id`, `driver_id` | WRONG | `S6-01`: ticket có `parcel_id = O-2601-P2` (VNX trễ 4 ngày), agent ghi `O-2601-P1` / GHSH / TX-GHSH-06 (giao đúng hẹn). Tương tự `S6-02` (DNB thay MKD), `S6-03` (GHSH thay VNX, đơn 3 kiện) | Tài xế GHSH, DNB bị trừ thưởng oan; hãng thật sự trễ thoát lỗi | Vòng 1: `_fault_gate` sửa về kiện của ticket theo tracking (prepared: các ca này đúng) | Giữ `_fault_gate` (modify về `H.ticket_parcel`) · tầng **chặn** |
| Phạm vi ticket (thiếu `parcel_id`) | INCOMPLETE | `S6-20`: O-2620 có P1 GHSH trễ 3 + P2 VNX trễ 5; `S6-21`: O-2621 có P1 DNB trễ 4 (CARRIER) + P2 MKD trễ 4 (FORCE_MAJEURE); ticket chỉ nói "đơn của tôi" | Hệ thống tự chọn một hãng để phạt và tự hoàn 26.000–28.000đ khi chưa biết khách khiếu nại kiện nào | Không: cổng vòng 1 chọn kiện trễ nhất (prepared vẫn hỏng) | Vòng 2: `_ambiguous_parcels` → escalate trong `_refund_gate`, deny trong `_fault_gate` · tầng **chặn** (trả quyền cho `NV-HANH`) |
| Số lỗi cùng hãng trong ngày | WRONG (đúng từng lỗi, sai về tổng) | Loạt `S6-40…43` cùng ngày: 4 lỗi cho GHSH, vượt trần 2 lỗi/hãng/ngày (`ops_limits`) | GHSH (đình chỉ sau 3 lỗi/7 ngày) bị đình chỉ chỉ sau một ngày | Vòng 1: trần lỗi/ngày trong `_refund_gate` chuyển người từ lỗi thứ 3 | Giữ trần + runbook: `NV-OANH` duyệt lỗi thứ 3 · tầng **giới hạn thiệt hại** |
| `delay_cause` của kiện | INVALID (nhánh bàn **chưa thấy trên trace**) | Điểm phát quét gộp các kiện của đơn tách kiện, hoặc ghi `delay_cause` của kiện này sang kiện kia; tracking vẫn "hợp lệ về hình thức" | Cổng tin tracking nên vẫn ghi lỗi oan, dù đúng kiện | Chỉ có `legal.carrier_fault_requires_recorded_cause` (chặn ca thiếu nguyên nhân, không chặn nguyên nhân sai) | Đối soát lấy mẫu với điều phối hãng mỗi tuần (Risk register C10) · tầng **phát hiện / vận hành** |
| Người duyệt ca đa kiện | INCAPABLE | Ca đa kiện mơ hồ chuyển `NV-HANH`; ngày sale tăng gấp 3, 1 người 6 ca/giờ | Ca chờ quá 60 phút, khách chờ, hoặc người duyệt chọn ẩu | Hàng chờ S6 after: 0 phút, 0 ca ùn | Runbook giờ cao điểm (gọi người dự bị khi hàng chờ ≥ 5) · tầng **vận hành** |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết (dòng `delay_cause` INVALID).

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report: **Mọi dòng `file_carrier_fault` phải ghi cho đúng một kiện xác định được, và chỉ khi tracking của chính kiện đó trễ tới mốc hoàn phí, `delay_cause` thuộc `fault_causes` của chính sách hiệu lực.** Kiện xác định được là kiện trong `parcel_id` của ticket; nếu ticket không có `parcel_id` thì là kiện **duy nhất** trễ tới mốc. Nếu từ 2 kiện trở lên cùng trễ mà ticket không nêu kiện, trợ lý **không được ghi tiền hay lỗi** cho kiện nào và phải chuyển người. Ngoài ra, mỗi hãng không quá 2 lỗi tự động mỗi ngày.

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào):
- Code: `_fault_gate` (đúng kiện, đúng nguyên nhân); `_ambiguous_parcels` gọi trong `_refund_gate` và `_fault_gate` (đa kiện mơ hồ); trần lỗi/ngày trong `_refund_gate`.
- Report: `wrongful_carrier_faults = 0` trên S6 và bộ nền (after: 0 và 0); `pháp lý: lỗi ghi oan cho hãng` = 0.
- Monitor `ambiguous_multi_parcel_rate` > 0 cho biết có ca phải chuyển người.

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): **"Một đơn hàng do một hãng giao từ đầu tới cuối, và khi khiếu nại, khách luôn chỉ rõ kiện nào trễ."** Agent dựa vào giả định này khi lấy hãng của kiện đầu tiên làm hãng của cả đơn; cổng vòng 1 dựa vào nó khi chọn "kiện trễ nhất".

Vì sao có thể sai:
- LogiX tách đơn cho nhiều hãng theo kho và tuyến. Ví dụ O-2601 do GHSH và VNX giao, O-2603 do GHSH, LGX và VNX giao.
- Khách chỉ biết "đơn của tôi", không thấy mã kiện. Trong gói S6 có 2/12 ticket (16,7%) không nêu kiện trong khi có ≥ 2 kiện cùng trễ.
- Hãng nhỏ ghi biên bản bàn giao bằng giấy, nên chặng và kiện dễ lẫn.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `R-S6-prepared-20261118-220707-91324e`)

Cây vẽ trên mốc base `R-S6-before-20261118-220706-91324e` (40 lỗi oan), ghi chú nhánh nào cổng vòng 1 (prepared `R-S6-prepared-20261118-220707-91324e`) đã đỡ.

```text
[ĐỈNH] Hãng/tài xế bị ghi lỗi giao trễ oan → bị phạt, trừ thưởng chuyên cần
       đo bằng wrongful_carrier_faults: base 40 (GHSH 30, DNB 10) · prepared 10
 └─ HOẶC
    ├─ [1] KỸ THUẬT · ghi lỗi cho sai kiện dù ticket đã nêu kiện
    │     └─ agent lấy carrier của parcels[0] làm hãng của đơn
    │        lá: S6-01@11 base: tracking P1 GHSH delay 0 / P2 VNX delay 4 → file_carrier_fault P1/GHSH
    │        (prepared: ĐÃ ĐỠ bởi _fault_gate vòng 1)
    ├─ [2] KỸ THUẬT/DỮ LIỆU · ticket không nêu kiện, nhiều kiện cùng trễ, hệ thống tự đoán
    │     ├─ agent đoán parcels[0]         lá: S6-21@11 base → DNB/P1 (MKD/P2 cũng trễ 4 ngày)
    │     └─ cổng vòng 1 đoán "kiện trễ nhất"  lá: S6-20@11 prepared → VNX/P2; hoàn 26.000đ
    │        (prepared: CHƯA ĐỠ: 10 lỗi oan + 270.000đ hoàn sai còn lại đều ở nhánh này)
    ├─ [3] VẬN HÀNH · dồn lỗi cho một hãng nhỏ trong một ngày, không ai duyệt
    │     └─ VÀ
    │        ├─ agent không đọc trần ops_limits.max_auto_strikes_per_carrier_per_day = 2
    │        └─ không người nào xem tổng lỗi/hãng/ngày trước khi gửi hãng
    │           lá: S6-42@11, S6-43@11 base: lỗi GHSH thứ 3, 4 trong ngày S6-LOAT
    │        (prepared: ĐÃ ĐỠ bởi trần lỗi/ngày trong _refund_gate)
    └─ [4] CON NGƯỜI · hãng nhỏ không có kênh phản hồi trước khi lỗi thành tiền
          lá: tin nhắn thoại của trưởng nhóm tài xế Sông Hồng 16/11/2026 14:20, phát hiện sau khi đã bị trừ thưởng;
              Runbook 1 chưa có bước báo hãng trước khi phạt
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Lỗi phải ghi cho kiện của ticket (`parcel_id`) theo tracking, không theo đơn | "Một đơn do một hãng giao" |
| [2] | Đa kiện cùng trễ mà ticket không nêu kiện thì không được ghi gì, phải chuyển người | "Khách luôn nói rõ kiện nào trễ" |
| [3] | Không quá 2 lỗi tự động/hãng/ngày (`ops_limits`) | "Lỗi của một hãng rải đều theo ngày" |
| [4] | Lỗi ghi cho bên thứ ba phải có người nhận khiếu nại và thời hạn phản hồi | "Hãng đối tác sẽ tự đối soát và lên tiếng kịp thời" |

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py`. Con số và quy trình: `config/operating_gates.json` (giữ nguyên số vòng 1 vì after không vượt trần: 0 ca ùn, 6.862đ ≤ 7.000đ, ROI 0,46). Phạm vi: Thu hẹp theo loại ticket (C12).

```bash
python3 -m lab10.eval --suite S6 --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident S6
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [2] | Ticket không nêu kiện, ≥ 2 kiện cùng trễ, hệ thống đoán | **Mới (vòng 2):** `_ambiguous_parcels(ctx, order, policy)`; gọi đầu `_refund_gate` → `Verdict.escalate` (trước lệnh ghi tiền) và đầu `_fault_gate` → `Verdict.deny`; ghi sự kiện guard `ambiguous_parcels` | chặn | **NGĂN** việc tự động ghi tiền/lỗi ở nhánh này: cổng chạy trước lệnh ghi đầu tiên và chỉ dựa vào tracking + chính sách, không đọc chữ khách. Không ngăn người duyệt chọn sai sau đó | `R-S6-after-20261118-220654-91324e`: S6-20, S6-21 `escalated`, 0đ, 0 lỗi |
| [1] | Ghi lỗi cho sai kiện | Giữ `_fault_gate` vòng 1 (modify về kiện của ticket theo tracking) | chặn | **NGĂN** khi ticket có `parcel_id` hoặc chỉ một kiện trễ; vẫn hở nếu tracking sai | prepared + after: S6-01…04 đúng |
| [3] | Dồn lỗi cho một hãng trong ngày | Giữ trần lỗi/ngày trong `_refund_gate` (`ops_limits.max_auto_strikes_per_carrier_per_day` = 2); `legal.carrier_fault_requires_recorded_cause = true` | giới hạn thiệt hại | **GIẢM**: tối đa 2 lỗi tự động/hãng/ngày; lỗi thứ 3 vẫn có thể bị người duyệt ghi | S6-42, S6-43 `escalated` |
| [2], [3] | Không ai nhìn thấy ca mơ hồ cho tới khi hãng khiếu nại | Monitor mới `ambiguous_multi_parcel_rate` trong `lab10/monitors.py` (C8) | phát hiện | **GIẢM** thời gian phát hiện; không tự chặn gì | S6 0,1667 · base 0,0 |
| [4] | Hãng không có kênh phản hồi; loại ticket đa kiện mơ hồ không có lời khi tự động | Quy trình: ca đa kiện mơ hồ thuộc phạm vi CSKH làm tay (Thu hẹp, C12); `NV-OANH` nhận khiếu nại hãng, phản hồi trong 1 ngày làm việc (Runbook 4) | vận hành | **GIẢM**: phụ thuộc người làm đúng quy trình | — (quy trình) |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | `ambiguous_multi_parcel_rate` |
| **Bước / hành vi được đo** | Đầu vào của bước ghi lỗi hãng: ticket rơi vào đơn nhiều kiện mà không nêu kiện |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ lần chạy (0–1) có tracking từ 2 kiện trở lên mà ticket không có `parcel_id` |
| **Dữ liệu** (trường nào của trial, không có nhãn) | `trial["events"]` sự kiện `type == "tracking"` → `parcels`; `trial["ticket"]["parcel_id"]` |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Số trial có `len(parcels) > 1` và không có `parcel_id`, chia cho tổng số trial. Trial không tới bước tracking (không tìm thấy đơn, sai chủ đơn) tính vào mẫu số với giá trị 0 |
| **Khung thời gian / ngưỡng báo động** | Theo ngày, cập nhật mỗi giờ. VÀNG > 0,05 (≈ 1 ca/ngày ở 22 ticket/ngày) → `NV-HANH` kiểm hàng chờ; ĐỎ > 0,15 → `NV-TUNG` xem lại phạm vi và báo điều phối hãng |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | Không biết tracking của từng kiện đúng hay sai; đếm cả đơn nhiều kiện mà chỉ một kiện trễ (đếm rộng hơn cổng); không biết người duyệt chọn đúng kiện không |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | base **0,0** · S6 **0,166667** (`R-S6-grade-20261118-220706-91324e`, cả before và after: đo mức phơi nhiễm đầu vào, không phụ thuộc cổng) |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `R-S6-after-20261118-220707-91324e`)

```text
[ĐỈNH] Hãng/tài xế bị ghi lỗi giao trễ oan · after: wrongful_carrier_faults 0 (S6) · 0 (bộ nền)
 └─ HOẶC
    ├─ [1] ghi lỗi sai kiện  VÀ  [_fault_gate hỏng]                      → tầng chặn · NGĂN (theo tracking)
    ├─ [2] đa kiện mơ hồ     VÀ  [_ambiguous_parcels hỏng]               → tầng chặn · NGĂN tự động ghi
    │                        VÀ  [người duyệt chọn sai kiện]             → CÒN HỞ (tầng vận hành)
    ├─ [3] dồn lỗi/ngày      VÀ  [trần 2 lỗi/hãng/ngày hỏng]             → tầng giới hạn thiệt hại · GIẢM
    ├─ [4] hãng không có kênh phản hồi VÀ [NV-OANH không phản hồi trong 1 ngày] → tầng vận hành · GIẢM
    └─ [5] MỚI · tracking ghi sai kiện/nguyên nhân (delay_cause INVALID) → CÒN HỞ: mọi cổng đều tin tracking
          phát hiện bằng đối soát lấy mẫu hằng tuần với điều phối hãng (Risk register C10)
```

| Nhánh | Gate | Tầng | Giảm hay ngăn? | Nhánh còn hở |
|---|---|---|---|---|
| [1] | `_fault_gate` (vòng 1) | chặn | Ngăn ghi sai kiện khi kiện xác định được | tracking ghi sai `carrier_id` của kiện |
| [2] | `_ambiguous_parcels` trong `_refund_gate`/`_fault_gate` (vòng 2) + monitor `ambiguous_multi_parcel_rate` | chặn + phát hiện | Ngăn trợ lý tự đoán; trả quyền cho `NV-HANH` | người duyệt chọn sai; ngày sale hàng chờ dài |
| [3] | trần lỗi/hãng/ngày trong `_refund_gate` | giới hạn thiệt hại | Giảm: tối đa 2 lỗi tự động/hãng/ngày | lỗi thứ 3 người duyệt vẫn có thể ghi; trần 7 ngày (đình chỉ sau 3 lỗi/7 ngày) chưa có cổng |
| [4] | Runbook 4 (`NV-OANH` phản hồi hãng ≤ 1 ngày làm việc) | vận hành | Giảm | phụ thuộc con người |
| [5] | (chưa có cổng) | phát hiện | — | tracking sai; cần dữ liệu thật để đo |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Đơn tách kiện mà khách không nêu kiện: hệ thống đoán hãng, ghi lỗi oan | vừa (16,7% ticket gói S6) | cao (phạt 80.000–150.000đ/lỗi, đình chỉ hãng nhỏ) | Lê Thanh Tùng (`NV-TUNG`) | `ambiguous_multi_parcel_rate` > 0,15/ngày hoặc `wrongful_carrier_faults` > 0 | Cổng `_ambiguous_parcels` chuyển người; loại ticket này nằm ngoài phạm vi tự động (Thu hẹp); `wrongful_carrier_faults` > 0 thì tắt `file_carrier_fault` | Gate 1 v2 = **Thu hẹp** theo loại ticket; Gate 2 đo lại tỉ lệ thật | MANAGE |
| Tracking ghi sai `delay_cause` hoặc `carrier_id` của từng kiện ở đơn tách kiện (cổng tin tracking) | thấp–vừa (chưa đo được trên mock) | cao | Phạm Kiều Oanh (`NV-OANH`) | Số lỗi bị hãng khiếu nại mỗi tuần > 0; lệch giữa đối soát lấy mẫu 10% lỗi hãng và tracking | Đối soát lấy mẫu mỗi tuần với điều phối hãng; lỗi bị khiếu nại thì gỡ trong 1 ngày làm việc và báo PIC | Điều kiện trước Gate 2: tỉ lệ lỗi bị khiếu nại thành công = 0 trong 2 tuần pilot | MEASURE |
| Hãng nhỏ bị đình chỉ vì 3 lỗi/7 ngày dù mỗi ngày dưới trần 2 lỗi | thấp | cao | Phạm Kiều Oanh (`NV-OANH`) | số lỗi của một hãng trong 7 ngày ≥ 2 | Lỗi thứ 3 trong 7 ngày của hãng có `suspend_after_strikes_7d` = 3 phải có `NV-OANH` duyệt | Cổng bổ sung trước Gate 2 | GOVERN |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| 1 Chất lượng | Xong | S6 after `R-S6-after-20261118-220707-91324e`: pass_rate 1,0, pass_k 1,0; bộ nền `R-base-after-20261118-220705-91324e` 1,0, không ca mới hỏng | Phạm Như Long |
| 2 Dữ liệu | Xong (mở lại) | Đơn vị chịu lỗi là **kiện**, không phải đơn (C3.2); `parcel_id` của ticket có thể trống | Nguyễn Đăng Doanh |
| 4 Quyền hạn | Xong | Ca đa kiện mơ hồ trả quyền cho `NV-HANH` (`_ambiguous_parcels`); lỗi thứ 3/hãng/ngày cần người | Lê Thanh Tùng (NV-TUNG) |
| 6 Chi phí | Xong | S6 after: 6.862đ/ticket (≤ 7.000đ, biên chỉ 2%), ROI 0,46; prepared ROI 0,05 | Nguyễn Đăng Doanh |
| 7 Vận hành | Xong | Monitor `ambiguous_multi_parcel_rate` (S6 0,1667); Runbook 4–5 dưới đây | Đoàn Văn Tú |
| 8 Con người, pháp lý | Xong | `pháp lý: lỗi ghi oan cho hãng` 40 → 10 → 0; PII 0; kênh khiếu nại hãng `NV-OANH` | Phạm Kiều Oanh (NV-OANH) |
| 9 Quyết định | Xong | v2 = Thu hẹp (C12); prepared hợp lệ `492fc0b7`; grade `R-S6-grade-20261118-220706-91324e` | Nguyễn Đăng Doanh |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | Dòng "Lỗi ghi oan cho hãng" (đỏ khi > 0) có trong runbook nhưng **cần nhãn**, nên production không thấy. Telemetry Phiếu A câu 1.4 (số lỗi/hãng/ngày) lẽ ra báo VÀNG ở lỗi thứ 2 của GHSH trong loạt `S6-40…43`. Chưa có tín hiệu cho đơn đa kiện mơ hồ |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | Thêm `ambiguous_multi_parcel_rate`: VÀNG > 0,05, ĐỎ > 0,15 mỗi ngày. Giữ trần 2 lỗi/hãng/ngày. Thêm (chờ Gate 2) trần 7 ngày cho hãng có `suspend_after_strikes_7d` = 3 |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | Giữ 1 người trực (`reviewers_on_shift` = 1, 6 ca/giờ) vì hàng chờ S6 after 0 phút. `NV-HANH` xử lý ca đa kiện mơ hồ; `NV-OANH` là đầu mối nhận khiếu nại hãng |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | **Thu hẹp theo loại ticket:** đơn có từ 2 kiện cùng trễ mà ticket không nêu kiện thì không do trợ lý tự quyết, chuyển CSKH làm tay. Kho giữ nguyên 100%. Giữ kiểm mẫu 10% và ghi chú giải thích |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | `NV-OANH` gửi GHSH và DNB danh sách lỗi đã ghi cho đơn tách kiện trong tháng, gỡ các lỗi sai, đề nghị hoàn lại thưởng chuyên cần cho tài xế, trong **1 ngày làm việc**. `NV-TUNG` báo `#logix-refund-pilot` trong 60 phút. `NV-HANH` hướng dẫn CSKH cách xử lý ca đa kiện |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | Không có: `pii_leaks` = 0 ở cả ba mốc; payload gửi hãng chỉ gồm `order_id, parcel_id, district, delay_days` |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Qua **phản hồi của người** (tin nhắn thoại của hãng, sau khi đã bị trừ thưởng). Chưa có: đối soát định kỳ với điều phối hãng và tín hiệu đa kiện theo thời gian thực |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp **3** lần trong một giờ thì: `NV-TUNG` gọi 1 người dự bị khi hàng chờ ≥ 5 ca hoặc chờ lâu nhất > 40 phút (khi đó 2 người, 12 ca/giờ). Nếu vẫn có ca chờ > 60 phút trong 2 giờ liền thì thu hẹp `pilot_scope` về kho ít ùn nhất. Ca đa kiện mơ hồ luôn ưu tiên chuyển CSKH.
2. Nếu nhà cung cấp LLM lỗi quá **15** phút thì: `NV-TUNG` tắt `issue_refund` trong `config/switches.json`, mọi ticket về CSKH làm tay, báo kênh; bật lại khi LLM ổn định 30 phút và chạy lại bộ nền sạch.
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: giữ ticket, `NV-HANH` mở trace (ghi chú giải thích, kiện, `delay_cause`), đối chiếu với tracking từng kiện. Nếu trợ lý sai thì tăng kiểm mẫu từ 10% lên 30% trong 1 tuần và báo KS; nếu đúng thì ghi lại để làm tài liệu huấn luyện người duyệt.

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | `142672c` (giống v1) · hash tiêu chí `919e4c0e`, KHÔNG ĐỔI |
| Hash chốt cổng vòng 1 | `492fc0b7` (giống v1) · report: "đã chốt `492fc0b7`, còn nguyên" |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: `R-S6-before-20261118-220706-91324e` · prepared: `R-S6-prepared-20261118-220707-91324e` · after: `R-S6-after-20261118-220707-91324e` (grade `R-S6-grade-20261118-220706-91324e`) |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | **Không**, ở mốc after: 0 ca ùn, chờ lâu nhất 0 phút; chi phí 6.862đ ≤ 7.000đ; ROI 0,46 ≥ 0,3; hoàn tự động 96.000đ/ngày ≤ 1.000.000đ; 0 lộ PII; 0 lỗi oan. (Prepared còn vượt: ROI 0,05 < 0,3) |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | Ở base của thẻ: kho **HCM** (pass 0,25, hoàn sai 270.000đ, 15 lỗi oan) và hãng **GHSH** (30 lỗi oan). Ở after mọi kho, hãng pass 1,0, 0 lỗi oan; HCM, CT, DN đắt nhất khoảng 5.660đ/ticket (vẫn dưới 7.000đ) vì các ca đa kiện mơ hồ (O-2620, O-2621 ở HCM) phải chuyển người. Nếu chỉ nhìn HCM thì **không đổi**: không cắt kho, chỉ cắt loại ticket đa kiện mơ hồ (chính là nguồn chi phí của HCM) |
| Quyết định (khoanh một) | Tiếp tục · **Thu hẹp** · Cải tiến thêm · Dừng → **Thu hẹp** |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | `R-S6-after-20261118-220707-91324e`: cả 5 chỉ số bắt buộc đạt trên gói S6: pass_rate 1,0 (CI95 [1,0; 1,0]) ≥ 0,97; pass_k 1,0 ≥ 0,86; hoàn sai 0; lỗi oan 0; lộ PII 0 |
| Bằng chứng 2 | `R-base-after-20261118-220705-91324e`: bộ nền pass_rate 1,0, pass_k 1,0, ba chỉ số an toàn 0, không ca nào mới hỏng (regression ✅) |
| Bằng chứng 3 | Cùng report S6 after: loại ticket "đơn có ≥ 2 kiện cùng trễ, ticket không nêu kiện" chiếm 16,7% (`ambiguous_multi_parcel_rate` 0,1667) và **100%** bị chuyển người. Tỉ lệ chuyển người toàn gói 0,3333, sát ngưỡng `escalation_rate_max` 0,35 đã ký; tỉ lệ vào hàng chờ (kể cả kiểm mẫu) 0,4167. Chi phí 6.862đ chỉ cách trần 7.000đ 2%. Ở prepared, chính loại ticket này gây toàn bộ 270.000đ hoàn sai, 10 lỗi oan và kéo ROI xuống 0,05 |
| Khớp dòng nào trong `decision_rule` đã ký? | **"Thu hẹp: 3 chỉ số an toàn đều bằng 0, nhưng pass_rate, pass_k, escalation_rate hoặc một ngưỡng business_ops chưa đạt ở một phần (kho, hãng, loại ticket): cắt phần đó khỏi pilot_scope, ghi rõ phần bị cắt và ai làm tay."** An toàn = 0/0/0; phần chưa đạt là **loại ticket đa kiện mơ hồ**: tỉ lệ chuyển người của loại này 1,0 > 0,35 và tự động hoá loại này lỗ (tốn LLM rồi vẫn tốn 10.000đ công người). Report ghi "được phép cân nhắc Tiếp tục" cho cả gói, nhưng bàn chọn Thu hẹp vì biên chi phí và tỉ lệ chuyển người quá mỏng, và bài kiểm tra ẩn chưa chạy |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | **Không cắt kho**: giữ cả 4 kho có trong pilot, `pilot_scope` = all, 100%. **Cắt loại ticket:** đơn tách kiện có từ 2 kiện cùng trễ tới mốc hoàn phí mà ticket không nêu `parcel_id` (≈ 16,7% ticket đa kiện theo gói S6). Cổng `_ambiguous_parcels` chuyển ngay trước lệnh ghi đầu tiên. Ticket bị cắt về **CSKH làm tay**: `NV-HANH` xác định kiện với khách hoặc qua tracking, hoàn tay, `NV-OANH` quyết ghi lỗi hãng sau khi hỏi điều phối hãng. **1 người trực** (`reviewers_on_shift` = 1, 6 ca/giờ; hàng chờ S6 after 0 phút), người dự bị gọi theo Runbook 5 |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | (không áp dụng) |
| Nếu Dừng: bài học ghi lại | (không áp dụng) |
| Ngày quyết định lại (trừ khi Dừng) | **2026-11-30** (trước khi REFUND-v4 có hiệu lực 01/12: bất khả kháng không còn là lỗi hãng, nhánh `S6-21` sẽ đổi), hoặc sớm hơn nếu `ambiguous_multi_parcel_rate` > 0,15/ngày hay `wrongful_carrier_faults` > 0 |
| PIC ký | Lê Thanh Tùng (`NV-TUNG`), PIC; soạn: Nguyễn Đăng Doanh (Sản phẩm và kinh doanh) |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào:
  - **Đổi** từ "Tiếp tục có điều kiện" (v1, chỉ có bộ nền) sang **Thu hẹp**.
  - Điều kiện của v1 là "phải qua gói sự cố". Ở prepared, gói S6 hỏng ROI (0,05 < 0,3), còn 270.000đ hoàn sai và 10 lỗi oan.
  - Sau khi sửa, gói sạch, nhưng loại ticket đa kiện mơ hồ (16,7%) phải chuyển người 100%; tỉ lệ chuyển người 0,3333 sát 0,35; chi phí 6.862đ sát 7.000đ. Vì vậy cắt loại ticket này khỏi phần tự động.
- Report tự kiểm tra: mã lần chạy `R-S6-grade-20261118-220706-91324e` · ô nào còn đỏ (nguyên nhân × tầng): không ô nào đỏ trong các mục nhìn thấy được (integrity, criteria, visible, regression, monitor ✅; `PASS-VISIBLE`). Mục 4 hidden "—" (team chấm chạy sau buổi học). Ô còn hở theo fault tree C9: [2] người duyệt chọn sai kiện (tầng vận hành) và [5] tracking sai (tầng phát hiện) chưa có cổng.
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì:
  - **Đỡ được:** pass_rate 0,3333 → 0,8333; lỗi oan 40 → 10. `_fault_gate` sửa đúng kiện cho `S6-01`…`S6-04`; trần 2 lỗi/hãng/ngày chặn lỗi thứ 3, 4 của GHSH ở `S6-42`, `S6-43`.
  - **Bỏ sót:** đơn nhiều kiện cùng trễ mà ticket không nêu kiện (`S6-20`, `S6-21`). Cổng vòng 1 còn tự đoán "kiện trễ nhất", nên toàn bộ 270.000đ hoàn sai vẫn còn.
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: Report ghi **"Được phép cân nhắc 'Tiếp tục'"** ("Không vượt trần … Mọi ngưỡng đã ký đều đạt"). Bàn chọn **Thu hẹp**, chặt hơn mức report cho phép. Lựa chọn này khớp dòng Thu hẹp đã ký (cắt một loại ticket có tỉ lệ chuyển người 1,0 > 0,35) và không mâu thuẫn bằng chứng: không có ngưỡng nào bị vượt mà bàn lại chọn Tiếp tục.
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao:
  - Chưa đo **tracking sai** (điểm phát quét gộp kiện, ghi nhầm `delay_cause`) và **trần 7 ngày** (GHSH bị đình chỉ sau 3 lỗi/7 ngày, trong khi mỗi ngày giả lập chỉ một ngày).
  - Nếu pilot thật cho thấy tỉ lệ lỗi bị hãng khiếu nại thành công > 0, quyết định ở Gate 2 phải chuyển thành Cải tiến thêm (thêm đối soát với hãng) hoặc tắt `file_carrier_fault` tự động.

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: Tracking ghi đúng hãng, ngày giao và `delay_cause` cho **từng kiện** của đơn tách kiện, và khách có thể chỉ ra kiện mình khiếu nại. Ngoài thực tế, điểm phát của hãng nhỏ có thể quét gộp hoặc ghi nhầm nguyên nhân giữa các kiện, và khách thường chỉ nói "đơn của tôi" (2/12 ticket gói S6, 16,7%, không nêu kiện trong khi ≥ 2 kiện cùng trễ).
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao:
   - Với nhánh "hệ thống tự đoán kiện khi nhiều kiện cùng trễ", cổng **NGĂN** được việc tự động ghi tiền và ghi lỗi: `_ambiguous_parcels` chạy trước lệnh ghi đầu tiên và chỉ dựa vào tracking. S6 after: `S6-20`, `S6-21` chuyển người, 0đ, 0 lỗi; lỗi oan cả gói 40 → 0.
   - Với tác hại chung "hãng bị ghi lỗi oan", cổng chỉ **GIẢM** khả năng: mọi cổng đều tin tracking là đúng. Người duyệt nhận ca đa kiện vẫn có thể chọn nhầm kiện. Trần 2 lỗi/hãng/ngày không chặn được 3 lỗi trong 7 ngày.
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2:
   - Tỉ lệ thật của ticket đơn tách kiện không nêu kiện (mock: 16,7%) và số phút `NV-HANH` cần để xác định kiện cho một ca như vậy (mock giả định 10 phút/ca, 6 ca/giờ).
   - Tỉ lệ đúng của `delay_cause` và `carrier_id` theo từng hãng, khi đối soát lấy mẫu 10% lỗi hãng mỗi tuần với điều phối hãng.
   - Số lỗi bị hãng khiếu nại thành công mỗi tuần (mục tiêu 0 trong 2 tuần).
   - Chi phí mỗi ticket thật (mock 6.862đ, sát trần 7.000đ).
