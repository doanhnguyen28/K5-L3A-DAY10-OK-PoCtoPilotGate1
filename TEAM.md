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

- Commit `Sign acceptance criteria`: `_______`
- Mã lần chạy dùng cho B8 / C12: `__________`
- Phiếu A mục A1–A5; Phiếu B mục B3–B8; Phiếu C mục C1, C3–C5, C10–C12.

### Exit ticket

`<Một điều học được, một điều còn chưa chắc — tự viết cuối buổi>`

Có dùng trợ lý AI (Claude) để đọc code, đề xuất bản nháp phiếu và ngưỡng; các con số đã được bàn soát lại và giải thích được.

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
