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
- Mã lần chạy cuối dùng cho C12: `R-S6-grade-20261118-172831-a71aa5`
- Phiếu A mục A1–A5; Phiếu B mục B3–B8; Phiếu C mục C1, C3–C5, C10–C12.

### Exit ticket

`[Nguyễn Đăng Doanh tự bổ sung một điều học được và một điều còn chưa chắc.]`

Có dùng trợ lý AI (Claude) để đọc code, đề xuất bản nháp phiếu và ngưỡng; các con số đã được bàn soát lại và giải thích được.

## PhamNhuLong-2A202603395

### Phần việc phụ trách

Vai Kỹ sư cổng; câu 1.3, 2.1–2.2, 2.6–2.8, 3.1, 3.4–3.6; phụ trách `lab10/guards.py`, `lab10/monitors.py` và chạy eval/trace/grade/check_submission.

### Đóng góp cụ thể

Lịch sử repo ghi nhận các thay đổi guard và monitor vòng 1; phần tiếp nối S6 thêm chuyển người duyệt khi ticket thiếu parcel_id trên đơn đa kiện và monitor `ambiguous_multi_parcel_rate`.

### Bằng chứng

Commit: `0ae691f`, `7b53a05`, `56c3601`; mã grade cuối: `R-S6-grade-20261118-172831-a71aa5`; Phiếu C mục C2, C4, C7–C9.

### Exit ticket

`[Phạm Như Long tự bổ sung một điều học được và một điều còn chưa chắc.]`

## DoanVanTu-2A202603595

### Phần việc phụ trách

Vai Vận hành và pháp lý; câu 1.2, 1.4, 2.4, 2.10, 3.3, 3.7; mục `operations`/`legal` trong `config/operating_gates.json` và `submission/submission.json`.

### Đóng góp cụ thể

Theo bảng phân công, phụ trách PIC/người duyệt, điều kiện dừng, quyền riêng tư, runbook và phần nộp. Nhóm đã ghi các nội dung vận hành/pháp lý trong config và Phiếu C; cần Tú xác nhận phần việc cá nhân thực tế.

### Bằng chứng

`config/operating_gates.json`; Phiếu B mục B7.5–B7.6; Phiếu C mục C10–C11; mã grade cuối `R-S6-grade-20261118-172831-a71aa5`.

### Exit ticket

`[Đoàn Văn Tú tự bổ sung một điều học được và một điều còn chưa chắc.]`
