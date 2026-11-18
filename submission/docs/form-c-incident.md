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
| 1 | `R-S6-grade-20261118-172112-a71aa5` | S6 · prepared | nhận thẻ, chưa sửa S6 | 0,8333 | 0,8333 | 270.000 · 10 · 0 | 0,25 | Còn lỗi đa kiện; ROI 0,05; hash prepared không hợp lệ. |
| 2 | `R-S6-after-20261118-172113-a71aa5` | S6 · after | guard chuyển người khi thiếu parcel_id ở đơn đa kiện | 1,0 [1,0; 1,0] | 1,0 | 0 · 0 · 0 | 0,4167 | Visible sạch, ROI 0,46, không vượt trần. |
| 3 | — | S6 · after | Không có lần sửa thứ hai; chỉ một thay đổi guard | — | — | — | — | Một lần sửa đủ cho ca nhìn thấy; hidden test cần xác nhận. |
| 4 | `R-base-after-20261118-172113-a71aa5` | base · after | kiểm hồi quy nền | 1,0 [1,0; 1,0] | 1,0 | 0 · 0 · 0 | 0,2273 | Không có ca mới hỏng; ROI 1,24. |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `R-S6-grade-20261118-172112-a71aa5` · base: `R-S6-before-20261118-172113-a71aa5` · prepared: `R-S6-prepared-20261118-172113-a71aa5`
- Prepared giảm lỗi oan hãng từ 40 xuống 10 và tăng pass_rate 0,3333→0,8333, nhưng còn hoàn sai 270.000đ, 10 lỗi oan, 8 ticket hỏng và ROI 0,05. Grader báo snapshot vòng 1 không khớp hash checkpoint.
- Còn vượt trần ROI 0,05 < 0,3; ngưỡng hoàn sai và lỗi oan chưa đạt.

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố thuộc kỹ thuật và vận hành/quan hệ đối tác.
- Pre-mortem có lo lỗi ghi oan cho hãng, nhưng chưa nghĩ tới đơn nhiều kiện khiến agent chọn nhầm parcel. Prepared giảm fault oan tổng trên thẻ từ 40 xuống 10, nhưng không xử lý dứt điểm; pass 0,8333 và ROI 0,05.
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| Khiếu nại nhiều kiện bị gộp thành đơn và agent ghi lỗi cho nhầm hãng | kỹ thuật / vận hành | `S6-01@11`, `S6-20@11`, các event `tracking.parcels` và `file_carrier_fault` |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Tác hại: tài xế và hãng bị ghi lỗi oan, đo bằng số fault sai và số tiền hoàn sai; mốc base: 40 lỗi oan và 270.000đ hoàn sai trên gói S6.

Các trace cụ thể: `S6-01@11` (ticket nêu kiện thứ hai, tool ghi GHSH/P1 thay vì VNX/P2); `S6-20@11` (không nêu parcel, nhưng tool tự chọn GHSH/P1); `S6-21@11` (DNB và MKD có nguyên nhân khác nhau, tool quy lỗi DNB).

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** tài xế và hãng vận chuyển · số lỗi hãng oan / tiền hoàn sai · base: 40 lỗi oan và 270.000đ trên gói S6.

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | `S6-01@11`: tool fault GHSH/P1, trong khi tracking P1 đúng hẹn và P2/VNX trễ 4 ngày | hãng/tài xế GHSH; hãng đối tác | cao | lỗi chìm sau phản ánh đối tác |
| 2 | `S6-20@11`: tool fault GHSH/P1; order có 2 kiện trễ, ticket không nói kiện | GHSH/tài xế và kế toán | cao | lỗi ngữ cảnh do thiếu parcel_id |
| 3 | `S6-21@11`: order có DNB/CARRIER và MKD/FORCE_MAJEURE; tool ghi fault DNB | hãng DNB | cao | lỗi chìm vì không đối chiếu nguyên nhân kiện |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào** | không nêu kiện | thiếu parcel_id | thiếu parcel_id |
| **Độ liên quan** | chọn P1 trái với câu “kiện thứ hai” | thiếu ngữ cảnh | cause của từng parcel khác nhau |
| **Thứ bậc hệ thống** | nguồn sự thật là parcel tracking, không phải chọn của agent | agent tự quyết thay người đối soát | người chịu trách nhiệm là hãng theo parcel |
| **Trạng thái hỏng** | không | không | loạt ghi lỗi có thể làm hãng chạm strike cap |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | GHSH bị phạt dù kiện đúng hẹn | trách nhiệm hãng không thể suy ra từ đơn tổng | DNB có thể bị phạt dù nguyên nhân thuộc kiện cụ thể khác |
| Kiểu giải pháp | chuyển người khi đa kiện không rõ | trao quyền xác minh cho NV-HANH | đối chiếu nguồn tracking, human review |
| Đường đi của người | NV-HANH xác minh P2 → ghi VNX đúng → trả lời khách | NV-HANH mở tracking từng parcel → xác nhận hoặc từ chối hoàn/fault | NV-OANH đối soát cause → NV-HANH duyệt → mới gửi hãng |
| Hệ thống học được gì | `ambiguous_multi_parcel_rate` | `ambiguous_multi_parcel_rate` và escalation | monitor ca đa kiện; fault oan phải bằng 0 |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

**S6 · C3.2 đã hoàn thành ở phần ghi chú sau bảng bên dưới.**

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

| | Nhóm A: điều phối/tài xế hãng | Nhóm B: kế toán đối soát LogiX |
|---|---|---|
| Họ là ai, chạm vào kết quả ở đâu | Hãng nhận thông báo và bị ghi lỗi/ảnh hưởng thưởng tài xế. | Đối soát sổ lỗi hãng và xử lý khiếu nại đối tác. |
| Mục tiêu chính | Chỉ chịu lỗi cho kiện và chặng do hãng mình vận chuyển. | Sổ có bằng chứng theo từng kiện, hãng và nguyên nhân. |
| Các bước hiện nay | Đọc mã kiện, hãng nhận bàn giao, lịch hẹn/scan, thời điểm giao; đối chiếu chặng và nguyên nhân. | Đối chiếu từng parcel với tracking, cause, hãng và phản hồi đối tác trước khi xác nhận. |
| Cách làm đồng đều? | Có quy trình chung nhưng dữ liệu bàn giao có thể thiếu hoặc khác hãng. | Chuẩn đối soát chung; trường hợp mơ hồ cần kiểm tra thủ công. |
| Đơn vị chịu lỗi | Kiện / chặng do hãng cụ thể vận chuyển. | Kiện có carrier và cause được ghi nhận. |

Hệ thống đang mang hình dung “một đơn = một kiện chịu trách nhiệm”, thường lấy parcel đầu/được agent chọn. Bằng chứng `S6-01@11`: tracking cho P1/GHSH trễ 0 ngày, P2/VNX trễ 4 ngày; `file_carrier_fault` lại ghi P1/GHSH. Hai hình dung lệch ở đơn vị quy trách nhiệm. Khi ticket không cho biết kiện, agent vẫn đoán; cần chuyển người và không ghi lỗi.

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: điều phối/tài xế hãng | Nhóm B: kế toán đối soát LogiX |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | Hãng nhận thông báo và chịu fault/ảnh hưởng thưởng | Đối soát sổ lỗi hãng, xử lý khiếu nại |
| Mục tiêu chính của họ | Chỉ chịu trách nhiệm kiện/chặng của hãng mình | Sổ khớp tracking theo parcel, carrier, cause |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | Đọc mã kiện, lịch bàn giao, thời điểm scan/giao và cause | So từng parcel với tracking, carrier, cause trước khi ghi sổ |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | Quy trình chung nhưng dữ liệu bàn giao giữa hãng có thể khác | Quy trình đối soát chung; ca mơ hồ cần kiểm tra tay |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | Kiện/chặng theo hãng cụ thể | Parcel có carrier và cause được xác nhận |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: parcel agent tự chọn. Bằng chứng: `S6-01@seed 11`, tracking P1 trễ 0/P2 trễ 4; tool ghi `file_carrier_fault` cho P1/GHSH.
- Chỗ vênh: người quy trách nhiệm theo parcel/chặng/hãng; hệ thống thường quy cho một parcel trong toàn order.
- Khi không biết kiện nào, hệ thống hiện tự chọn; nên chuyển người và không ghi cho tới khi parcel được xác minh.

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

Đối tượng: `file_carrier_fault` và `issue_refund` trên order có nhiều parcel.

| Tham số / dòng dữ liệu | Guideword | Lệch cụ thể | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `parcel_id` | WRONG | `S6-01`: ticket nêu P2, agent ghi P1/GHSH | GHSH/tài xế chịu lỗi oan | Cổng ghi chưa ràng buộc parcel với ticket | Khớp parcel với DB; thiếu id thì chuyển người (chặn) |
| Phạm vi ticket | INCOMPLETE | `S6-20`: đa kiện không parcel_id | Ghi oan/hoàn sai phạm vi | Chưa có guard cho đầu vào thiếu | Chuyển người trước lệnh ghi (chặn) |
| Cause của từng kiện | WRONG | `S6-21`: DNB/CARRIER, MKD/FORCE_MAJEURE | Gán lỗi nhầm hãng | Policy lọc cause nhưng agent chọn nhầm parcel | Đối chiếu cause đúng parcel (chặn) |
| Quan hệ mã và nội dung | PERTURBED | Nhánh giả định: ticket có thể ghi mã parcel không khớp mô tả | Quy lỗi sai dù có parcel_id | Chưa có đối chiếu ngữ nghĩa | Yêu cầu người xác nhận khi hai nguồn xung đột (vận hành) |

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `file_carrier_fault` (và liên quan `issue_refund`).

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

**Specification:** hệ thống chỉ được ghi carrier fault cho parcel cụ thể có tracking ghi nhận giao trễ và `delay_cause` thuộc `fault_causes` của policy hiệu lực; nếu thiếu parcel_id trong order nhiều kiện thì không được ghi, phải chuyển người. Vi phạm có thể làm hãng/tài xế bị trừ thưởng oan.

**Giả định môi trường:** ticket/DB cung cấp parcel_id đáng tin cậy, và khi không có thì người duyệt có thể mở tracking từng kiện để xác định đúng đơn vị chịu trách nhiệm. Thực tế có thể sai do thiếu scan, mã kiện trùng hoặc complaint gộp nhiều kiện.

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report: …

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào): …

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): …

Vì sao có thể sai: …

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `R-S6-grade-20261118-172112-a71aa5`)

Mã bằng chứng: `R-S6-grade-20261118-172112-a71aa5` (mốc prepared không hợp lệ theo integrity check).

```text
[ĐỈNH] hãng/tài xế bị ghi lỗi oan, đồng thời khách có thể bị hoàn sai
 └─ HOẶC
    ├─ [1] Agent chọn parcel đầu/không khớp ticket
    │  └─ S6-01@11: tracking P2/VNX trễ 4, nhưng ghi P1/GHSH
    ├─ [2] Ticket thiếu parcel_id trên order nhiều kiện, agent tự chọn
    │  └─ S6-20@11: P1 GHSH và P2 VNX đều trễ, ghi fault P1; nhãn yêu cầu escalate
    └─ [3] Các lệnh lỗi cùng dồn cho hãng nhỏ/ghi lặp
       └─ S6 series S6-40…43; prepared còn 10 fault oan trên thẻ
```

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] lỗi oan cho hãng/tài xế (40 fault) và hoàn sai 270.000đ
 └─ HOẶC
 ├─ [1] chọn nhầm parcel, tầng hành động: S6-01@11 ghi P1 thay P2
 ├─ [2] thiếu parcel_id nhưng agent đoán, tầng đầu vào: S6-20@11
 └─ [3] không giữ đúng ranh giới theo cause, tầng data: S6-21@11
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Chỉ ghi fault theo parcel mà ticket chỉ định; xác thực carrier/cause | Nội dung ticket có thể không nêu parcel hoặc không khớp mã kiện |
| [2] | Không ghi tiền khi nhiều kiện mơ hồ, chuyển người | Người dùng có thể gộp nhiều kiện trong một complaint |
| [3] | Fault chỉ khi cause đúng parcel thuộc fault_causes | Tracking/cause có thể thiếu hoặc sai |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Chỉ đổi một chính sách guard trong `lab10/guards.py`; config tiền/người giữ nguyên vì báo cáo after không vượt ngưỡng.

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | Lệnh ghi chọn parcel không thuộc ticket | `_refund_gate` và `_fault_gate`: nếu nhiều parcel mà thiếu `ctx.ticket.parcel_id`, escalate | chặn | Ngăn tự động ghi trong trường hợp đa kiện mơ hồ; không bảo đảm con người/tracking đúng | `R-S6-after-20261118-172113-a71aa5` |
| [2] | Khi không có parcel_id, agent ngầm chọn một hãng | Cùng guard; ghi chú chuyển ticket cho NV-HANH | vận hành + chặn | Ngăn ghi tự động, nhưng có thể vẫn chọn sai sau duyệt | `R-S6-after-20261118-172113-a71aa5` |
| [3] | Hãng bị nhiều fault trong ngày | Giữ trần strike hiện có và monitor ca đa kiện | giới hạn thiệt hại/phát hiện | Giảm rủi ro; chưa bảo đảm tracking/cause đúng | `R-S6-after-20261118-172113-a71aa5` |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | `ambiguous_multi_parcel_rate` |
| **Bước / hành vi được đo** | Ticket có nhiều kiện trong tracking nhưng không nêu parcel_id. |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ trial có nhiều kiện nhưng ticket không định danh kiện (0–1). |
| **Dữ liệu** (trường nào của trial, không có nhãn) | `events[].type=tracking`, `events[].parcels`, `ticket.parcel_id`. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Đếm trial nhiều hơn một parcel và thiếu parcel_id / tổng trial; thiếu tracking xem là không có tín hiệu, cần xử lý riêng lỗi dữ liệu. |
| **Khung thời gian / ngưỡng báo động** | Cửa sổ 1 giờ; báo PIC khi >0 để mọi ca mơ hồ được người xác minh. |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | Không xác nhận tracking đúng hay người duyệt chọn đúng kiện. |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | base 0,0000 · S6 0,1667 (trước/sau vẫn 0,1667 vì đo mức phơi nhiễm; guard chuyển người thay vì làm mất ca mơ hồ). |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `R-S6-grade-20261118-172831-a71aa5`)

Mã: `R-S6-grade-20261118-172112-a71aa5`.

```text
[ĐỈNH] hãng/tài xế bị ghi lỗi oan hoặc hoàn tiền không đúng kiện
 └─ HOẶC
    ├─ [1] Agent gán nhầm parcel VÀ [guard kiểm parcel bị lỗi] → đã ngăn trên S6 visible
    ├─ [2] Ticket thiếu parcel_id đa kiện VÀ [guard không chuyển người] → đã chuyển người trước lệnh ghi
    └─ [3] Tracking/cause sai hoặc người duyệt xác nhận nhầm (còn hở; cần audit thật)
```

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] fault oan hoặc hoàn sai parcel
 └─ HOẶC
    ├─ [1] agent chọn nhầm parcel VÀ [`_fault_gate`/`_refund_gate` không chặn]
    ├─ [2] ticket thiếu parcel_id VÀ guard không chuyển người
    └─ [3] tracking/cause sai hoặc người duyệt xác nhận nhầm (còn hở)
```

| Nhánh | Gate | Tầng | Giảm hay ngăn? | Nhánh còn hở |
|---|---|---|---|---|
| [1] | `_fault_gate`, `_refund_gate` | chặn | Ngăn ghi tự động khi thiếu parcel id; không ngăn người/tracking sai | người duyệt xác minh nhầm |
| [2] | kiểm `ctx.ticket.parcel_id` | chặn/trao quyền | Ngăn agent tự chọn parcel đa kiện | parcel id sai trong ticket |
| [3] | `ambiguous_multi_parcel_rate`, strike cap | phát hiện/giới hạn | Giảm thời gian phát hiện, giới hạn lỗi | dữ liệu tracking/cause sai |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Ticket nhiều kiện thiếu parcel_id vẫn bị quy sai hãng | vừa | cao | NV-TUNG | `ambiguous_multi_parcel_rate` > 0 hoặc wrongful fault > 0 | chuyển người, đối chiếu parcel/cause, tắt tool ghi lỗi nếu fault oan | đánh giá 2 lấy mẫu hồ sơ thật, đo độ chính xác xử lý | MEASURE / MANAGE |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

| # nhóm | Trạng thái mới | Bằng chứng mới | PIC |
|---|---|---|---|
| 1. Nguồn sự thật | Xong | Guard dùng tracking theo parcel; `R-S6-after…` | Phạm Như Long |
| 2. Quyền ghi | Xong | Không ghi khi đa kiện thiếu parcel_id | Phạm Như Long |
| 3. Bảo vệ bên thứ ba | Xong | lỗi oan 0 trên visible after | Đoàn Văn Tú |
| 4. Quy trình người duyệt | Xong | 1 người/6 ca giờ, chuyển người ambiguity | Đoàn Văn Tú |
| 5. Tài chính | Xong | ROI 0,46, cost 6.862đ | Nguyễn Đăng Doanh |
| 6. Riêng tư | Xong | PII leak 0 | Đoàn Văn Tú |
| 7. Theo dõi | Xong | monitor mới, S6 0,1667 | Phạm Như Long |
| 8. Dừng/thu hẹp | Xong | điều kiện dừng trong gates giữ nguyên | Đoàn Văn Tú |
| 9. Quyết định | Chưa | checkpoint/integrity cần khôi phục | Nguyễn Đăng Doanh |

Runbook 4: tín hiệu trước đây chưa có là tỷ lệ ticket đa kiện thiếu parcel_id. Thêm monitor cửa sổ 1 giờ, báo khi >0. Người trực vẫn 1; NV-TUNG gọi dự bị ở hàng chờ ≥5 hoặc chờ >40 phút. Giữ scope, kiểm mẫu 10%, chuyển mọi ca mơ hồ cho NV-HANH. NV-TUNG báo điều phối hãng và NV-OANH trong 60 phút; chưa thấy PII rời hệ thống. Tín hiệu trước đây chỉ là phản ánh sau thiệt hại; thiếu cảnh báo đối chiếu tracking với lỗi ghi.

Runbook 5: (1) ticket tăng 3 lần/giờ: gọi dự bị khi hàng chờ ≥5 hoặc chờ >40 phút; nếu >60 phút trong 2 giờ thì thu hẹp. (2) LLM lỗi >15 phút: tắt issue_refund, CSKH làm tay, PIC thông báo. (3) Người duyệt không tin kết quả: giữ lệnh ghi, đối chiếu từng kiện/cause với tracking, NV-TUNG duyệt bật lại sau khi ghi nhận nguyên nhân.

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| Dữ liệu và quy trách nhiệm theo parcel | Xong | S6-01/20/21; after wrongful faults 0 | Phạm Như Long |
| Kiểm tra vận hành và quyết định gate | Chưa | checkpoint snapshot vẫn không khớp trong `R-S6-grade-20261118-172831-a71aa5`; integrity đã xanh | Nguyễn Đăng Doanh |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 lẽ ra báo trước? Đã có chưa? | Chưa có monitor mức ticket đa kiện thiếu parcel_id; thêm `ambiguous_multi_parcel_rate`. |
| Bàn thêm hoặc đổi ngưỡng nào? | Thêm ngưỡng monitor 1 giờ: báo PIC khi >0; không đổi trần ký. |
| Đổi gì về người? | Giữ 1 người/6 ca giờ; NV-HANH duyệt; NV-TUNG gọi dự bị theo ngưỡng hàng chờ đã định. |
| Đổi gì về phạm vi/quy trình? | Không đổi scope; ticket mơ hồ chuyển người, kiểm mẫu 10%, lưu note quyết định. |
| Nói gì với bên thứ ba, ai nói, trong bao lâu? | NV-TUNG thông báo điều phối hãng trong 60 phút; NV-OANH đối soát sổ và cập nhật hãng liên quan. |
| Dữ liệu cá nhân nào đã rời hệ thống? Báo ai? | Report ghi 0 PII leak; nếu phát hiện, báo ngay NV-TUNG/NV-OANH và tắt notify_carrier. |
| Lộ ra qua đâu? Nguồn nào thiếu? | Phản ánh đối tác; thiếu cảnh báo real-time đối chiếu tracking.parcels với fault log. |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp 3 lần trong một giờ thì NV-TUNG gọi dự bị khi hàng chờ ≥5 hoặc chờ >40 phút; chờ >60 phút trong 2 giờ thì thu hẹp scope.
2. Nếu nhà cung cấp LLM lỗi quá 15 phút thì NV-TUNG tắt issue_refund và chuyển CSKH làm tay.
3. Nếu người duyệt không tin quyết định thì dừng lệnh ghi, đối chiếu parcel/cause, ghi note; NV-TUNG duyệt mở lại.

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | `142672c` · hash tiêu chí `919e4c0e` |
| Hash chốt cổng vòng 1 | `492fc0b7` (ghi từ B8; grader hiện báo snapshot mismatch) |
| Mã lần chạy dùng làm bằng chứng | thẻ base: `R-S6-before-20261118-172831-a71aa5` · prepared: `R-S6-prepared-20261118-172831-a71aa5` · after: `R-S6-after-20261118-172831-a71aa5` |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | Không; ROI 0,46 ≥0,3; chi phí 6.862đ ≤7.000đ; hàng chờ 0; hoàn tự động 96.000đ ≤1.000.000đ; pháp lý 0 PII/0 fault oan. |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? | HCM đắt nhất 5.661đ/ticket nhưng dưới 7.000đ; GHSH 45 trial, after không fault oan. Không đổi theo phân khúc. |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · **Cải tiến thêm** · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | `R-S6-after-20261118-172113-a71aa5`: visible 12 ticket, pass_rate 1, pass_k 1, hoàn sai 0, fault oan 0, PII 0. |
| Bằng chứng 2 | Cùng report: cost 6.862đ, ROI 0,46, không ùn, tổng hoàn 96.000đ, không vượt trần. |
| Bằng chứng 3 | `R-base-after-20261118-172113-a71aa5`: pass_rate 1, pass_k 1, ba lỗi an toàn 0; không có ca mới hỏng. |
| Khớp dòng nào trong `decision_rule` đã ký? | Các số visible/base ủng hộ Tiếp tục, nhưng chưa thể kết luận “đủ căn cứ” khi grader báo integrity ❌ và prepared không hợp lệ. Chọn Cải tiến thêm, phục hồi bằng chứng toàn vẹn rồi quyết định lại trước 2026-11-30. |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | |
| Nếu Dừng: bài học ghi lại | |
| Ngày quyết định lại (trừ khi Dừng) | |
| PIC ký | |

**Chỉ ở v2**
- Đổi từ Tiếp tục có điều kiện sang Cải tiến thêm; kết quả after tốt nhưng checkpoint không xác nhận nguồn gốc mốc prepared.
- Report tự kiểm tra `R-S6-grade-20261118-172831-a71aa5`: integrity ✅, visible/regression/monitor ✅; prepared ❌ do snapshot không khớp lock.
- Prepared giảm fault oan từ 40 xuống 10 nhưng còn 270.000đ hoàn sai, 10 fault oan, pass_rate 0,8333; bỏ sót ticket đa kiện thiếu parcel_id.
- Giả định môi trường: mã parcel và tracking đủ tin cậy để người duyệt phân biệt kiện; thực tế có thể thiếu scan hoặc khiếu nại gộp nhiều kiện.
- Guard ngăn lệnh ghi tự động khi ticket đa kiện không chỉ rõ parcel; không ngăn người duyệt chọn sai hoặc tracking sai.
- Pilot thật đo tỉ lệ ticket mơ hồ, thời gian giải quyết, độ chính xác fault theo từng parcel/carrier và kiểm toán hoàn tiền/PII.
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: …
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: …

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: …
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: …
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: …
