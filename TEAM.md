# Team

## Thông tin nhóm

- Tên nhóm: OK
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-OK-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S6

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai |
| --: | --------- | ---- | --- |
| 1 | Nguyễn Đăng Doanh | 2A202603597 | Sản phẩm và kinh doanh |
| 2 | Phạm Như Long | 2A202603395 | Kỹ sư cổng |
| 3 | Đoàn Văn Tú | 2A202603595 | Vận hành và pháp lý |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenDangDoanh-2A202603597

### Phần việc phụ trách

Vai Sản phẩm và kinh doanh + Vận hành và pháp lý.
- Đề: câu 1.1, 1.2, 1.4, 1.6; 2.3, 2.4, 2.9, 2.10; 3.2, 3.3, 3.7; quyết định v1, v2.
- Phiếu: A (A1, A2 cột telemetry, A3, A4, A5); B (B3, B4, B5, B6 lăng kính kinh doanh/con người/pháp lý, B7.3 ticket hiểm, B7.4, B7.5, B7.6, B8); C (C1, C3, C4, C5, C7 phần config, C10, C11, C12).
- File: `config/acceptance_criteria.json`, `config/operating_gates.json` (`business`, `operations`, `legal`), `submission/submission.json`.

### Đóng góp cụ thể

- Viết và ký Bản tiêu chí (5 ngưỡng bắt buộc, `business_ops`, `stop_condition`, 4 dòng `decision_rule`).
- Đặt cổng kinh doanh, vận hành, pháp lý trong `config/operating_gates.json`.
- Viết bản đồ dữ liệu và ví dụ drift (REFUND-v4); HAZOP vòng 1; checklist 9 nhóm việc; runbook 1–3 và giờ cao điểm.
- Viết quyết định v1, v2.

### Bằng chứng

- Commit `Sign acceptance criteria`: `142672c`
- Mã lần chạy dùng cho B8: `R-base-before-20261118-170257-d34b57`, `R-base-prepared-20261118-170341-d34b57`; cho C12: `R-S6-grade-20261118-220706-91324e`
- Phiếu A mục A1–A5; Phiếu B mục B3–B8; Phiếu C mục C1, C3–C5, C10–C12.

### Exit ticket

- **Học được:** tiêu chí phải viết và ký **trước** khi xem số. Ngưỡng `escalation_rate_max` 0,35 và `cost_per_ticket_vnd_max` 7.000đ ký từ đầu là thứ làm v2 chọn **Thu hẹp** thay vì Tiếp tục: S6 after đạt mọi ngưỡng, nhưng tỉ lệ chuyển người 0,3333 và chi phí 6.862đ đều sát trần. Nếu không ký trước, rất dễ nới ngưỡng cho vừa kết quả.
- **Còn chưa chắc:** các con số vận hành đều là mock (10 phút/ca duyệt, 16,7% ticket đa kiện mơ hồ, tracking luôn đúng). Mình chưa chắc khi chạy với 2 depot thật thì chi phí còn dưới 7.000đ/ticket không, vì biên hiện chỉ khoảng 2%.

Có dùng trợ lý AI (Claude) để đọc code, đề xuất bản nháp phiếu và ngưỡng; các con số đã được bàn soát lại và giải thích được.

## PhamNhuLong-2A202603395

### Phần việc phụ trách

Vai Kỹ sư cổng; câu 1.3, 2.1–2.2, 2.6–2.8, 3.1, 3.4–3.6; phụ trách `lab10/guards.py`, `lab10/monitors.py` và chạy eval/trace/grade/check_submission.

### Đóng góp cụ thể

- Viết cổng vòng 1 trong `lab10/guards.py` (commit `7b53a05`):
  - `pre_guard` ghim chính sách theo ngày hiệu lực;
  - `_refund_gate`: tính lại quyền lợi từ tracking DB, ép `payer = LOGIX`, chặn hoàn lặp, kiểm phê duyệt hợp lệ, trần 300.000đ/khách/ngày, trần 2 lỗi/hãng/ngày, chặn `fail_open`;
  - `_fault_gate`: ghi lỗi đúng kiện, đúng nguyên nhân;
  - `_notice_gate`: chỉ gửi hãng các trường trong `carrier_notice_fields`;
  - `_reply_gate`.
- Thêm 3 monitor trong `lab10/monitors.py` (commit `0ae691f`): `risk_signal_rate`, `peak_human_cases_per_hour`, `avg_cost_per_ticket_vnd`.
- Kết quả: bộ nền 0,9909 → 1,0, hoàn sai 20.000đ → 0, lỗi oan 1 → 0; trên S6 (prepared) lỗi oan 40 → 10 trước khi biết thẻ.

### Bằng chứng

Commit: `0ae691f`, `7b53a05`, `56c3601`; chốt vòng 1 `492fc0b7`; grade cuối `R-S6-grade-20261118-220706-91324e`; Phiếu B mục B0–B2, B7.1–B7.3; Phiếu C mục C2, C4, C7–C9.

### Exit ticket

*(Nháp theo phần việc trong repo, Phạm Như Long đọc lại và sửa bằng lời của mình trước khi nộp.)*

- **Học được:** cổng đặt ngoài model, so lệnh ghi với nguồn sự thật (tracking, chính sách hiệu lực) thì đỡ được cả lỗi mình chưa biết trước. Cổng `_fault_gate` viết từ pre-mortem đã sửa đúng kiện cho `S6-01`…`S6-04` dù lúc viết chưa có thẻ S6.
- **Còn chưa chắc:** cổng nào cũng tin tracking là đúng. Nếu điểm phát ghi nhầm `delay_cause` hoặc `carrier_id` thì cổng vẫn ghi lỗi oan, và mock không có ca nào để thử điều này.

## DoanVanTu-2A202603595

### Phần việc phụ trách

Vai Vận hành và pháp lý; câu 1.2, 1.4, 2.4, 2.10, 3.3, 3.7; mục `operations`/`legal` trong `config/operating_gates.json` và `submission/submission.json`.

### Đóng góp cụ thể

- Phân tích thẻ S6 lần đầu (commit `43fc6b2`): dò trace `S6-01@11`, `S6-20@11`, `S6-21@11`, so `tracking.parcels` với `file_carrier_fault`, chỉ ra hệ thống quy lỗi theo đơn chứ không theo kiện.
- Viết bản đầu cổng chuyển người cho đơn nhiều kiện thiếu `parcel_id` trong `lab10/guards.py`. Bản này sau được thu hẹp thành `_ambiguous_parcels`, chỉ áp dụng khi từ 2 kiện cùng trễ.
- Thêm monitor `ambiguous_multi_parcel_rate` trong `lab10/monitors.py` (bộ nền 0,0, S6 0,1667).
- Viết bản đầu Phiếu C: C2, C3.2, C4, C6–C11 (risk register, cập nhật checklist, runbook 4–5).
- Điền bản đầu `submission/submission.json` và chạy `check_submission`.

### Bằng chứng

Commit `43fc6b2` (`lab10/guards.py`, `lab10/monitors.py`, `templates/form-c-incident.md`, `submission/`); Phiếu C mục C2, C3.2, C4, C10–C11; monitor `ambiguous_multi_parcel_rate`; grade cuối `R-S6-grade-20261118-220706-91324e`.

### Exit ticket

*(Nháp theo phần việc trong repo, Đoàn Văn Tú đọc lại và sửa bằng lời của mình trước khi nộp.)*

- **Học được:** tác hại trên thẻ S6 không nằm ở model mà ở **đơn vị quy lỗi**. Người trong nghề quy lỗi theo kiện, hệ thống quy theo đơn. Khi đầu vào không đủ để biết kiện nào, hành động an toàn là dừng trước lệnh ghi đầu tiên và chuyển người, không phải đoán "kiện trễ nhất".
- **Còn chưa chắc:** chuyển ca đa kiện mơ hồ cho chị Hạnh chỉ giảm chứ chưa ngăn được lỗi oan. Người duyệt vẫn có thể chọn nhầm kiện, và vào ngày sale 1 người trực 6 ca/giờ có thể không đủ.
