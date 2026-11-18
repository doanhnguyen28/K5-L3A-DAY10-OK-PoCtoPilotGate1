# Phân công Lab 10 · Bàn OK (3 người)

Repo: `K5-L3A-DAY10-OK-PoCtoPilotGate1` · Thẻ sự cố đã bốc: `__`

Chia theo ba vai trong đề (`problem-set.md`). Điền tên vào bảng rồi chép sang `TEAM.md`.

| Vai | Người | MSSV | Giữ file nào (chỉ người này sửa) |
|---|---|---|---|
| **Kỹ sư cổng** (KS) | | | `lab10/guards.py`, `lab10/monitors.py`. **Máy duy nhất chạy `eval`, `trace`, `gate`, `checkpoint`, `grade`, `check_submission`** |
| **Sản phẩm và kinh doanh** (SP) | | | `config/acceptance_criteria.json`, `config/operating_gates.json` → mục `business` |
| **Vận hành và pháp lý** (VH) | | | `config/operating_gates.json` → mục `operations`, `legal`; `submission/submission.json` |

Phiếu: mỗi mục có một người giữ bút (bảng bên dưới); người khác góp ý qua chat, không sửa thẳng vào mục đó.

---

## Phút 0–15 · Cài đặt

| KS | SP | VH |
|---|---|---|
| `git remote add upstream https://github.com/VinUni-AI20k/K5_L3_Day10_PoC-to-Pilot_Gate1_student.git`, `git config user.name/email` (MSSV trưởng nhóm, email giả), chạy `python -m unittest discover -s tests` → `Ran 13 tests … OK` | Đọc `problem-set.md` Khối 1, `config/acceptance_criteria.example.json` (chỉ xem cách viết) | Điền bảng thành viên trong `TEAM.md`; đọc `data/world.json` mục `staff`, `ops_limits`, `ops_facts` |

Xong khi: test OK; `git remote -v` có `origin` và `upstream`; `TEAM.md` có đủ 3 dòng.

---

## Phút 15–65 · Khối 1 · Phiếu A → KÝ

**Chưa ai chạy `lab10.eval` trong khối này.**

| Câu / mục | Giữ bút | Ghi chú |
|---|---|---|
| A1 · Câu 1.1 mục tiêu hệ thống | SP | Khác "model trả lời đúng" |
| A1 · Câu 1.2 mục tiêu của chị Oanh, chị Hạnh | VH | `NV-OANH` đối soát sổ; `NV-HANH` duyệt trong 60 phút |
| A2 · Câu 1.3 offline metric cho một bước | KS | Gợi ý bước "chọn độ trễ": DB delay vs `delay_days_used` |
| A2 · Câu 1.4 telemetry production | VH | Có khung thời gian + ngưỡng báo động, không cần nhãn |
| A3 · Câu 1.5 khoảng tin cậy | Cả bàn | Chọn (b), giải thích một câu |
| A4 · Câu 1.6 câu "Nếu … thì …", soát 4 câu hỏi, ranh giới đầu ra | SP | KS và VH mỗi người góp một câu ranh giới |
| `config/acceptance_criteria.json` | SP | `team` = tên repo; 5 ngưỡng bắt buộc, 1 nên có, `business_ops`, `stop_condition`, 4 dòng `decision_rule`. **Không chép ngưỡng của file example** |

**Phút 60–65 · Ký** (cả bàn soát file lần cuối, rồi):

```bash
python -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

- SP chạy lệnh ký và push; KS và VH `git pull` ngay sau đó.
- SP điền A5 (giờ ký, mã commit).
- Từ đây **không ai mở `acceptance_criteria.json`** bằng editor tự format.

---

## Phút 65–85 · Khối 2A · Phiếu B (làm song song 10 phút, rồi pre-mortem 10 phút)

| KS | SP | VH |
|---|---|---|
| **Câu 2.1 (B0, B1):** `python -m lab10.eval --suite base --stage base --note "baseline"` → `python -m lab10.gate --run runs/<mã>/report.json`. Ghi mã lần chạy; chép khối "kinh doanh và vận hành" và "theo kho và hãng" vào nhóm chat cho SP, VH | **Câu 2.3 (B3):** bản đồ dữ liệu + một ví dụ drift (gợi ý: `REFUND-v4` hiệu lực 2026-12-01 nhưng trợ lý chọn theo cờ `index_active`) | **Câu 2.4 (B4):** HAZOP vòng 1 ≥ 3 dòng trên một tool ghi + ≥ 2 dòng ngoài kỹ thuật (người duyệt, ngân sách, dữ liệu gửi hãng) |
| **Câu 2.2 (B2):** `python -m lab10.trace --suite base --ticket T-002 --seed 55`, điền bảng soát lỗi | Đọc số chi phí / ROI từ báo cáo base | **Câu 2.4 (B5):** checklist 9 nhóm việc, mỗi dòng một PIC có tên |

**Câu 2.5 (B6) · Pre-mortem, cả bàn:**
- KS viết lăng kính kỹ thuật.
- SP viết lăng kính kinh doanh.
- VH viết lăng kính con người/vận hành và pháp lý.
- Cả bàn khoanh 2–3 lý do sẽ thành cổng.

Xong khi: có mã lần chạy base; `T-002@55` đã xếp loại lỗi; pre-mortem đủ 4 lăng kính.

---

## Phút 85–105 · Khối 2B · Cổng phòng ngừa

| KS | SP | VH |
|---|---|---|
| **Câu 2.6 (B7.1):** code 2–3 cổng trong `lab10/guards.py`, mỗi cổng gắn với một lý do pre-mortem hoặc dòng HAZOP. Không viết theo mã ticket/câu chữ | **Câu 2.9 (B7.4):** điền `business`: `daily_refund_cap_vnd`, `cost_budget_per_ticket_vnd`, `pilot_scope`, `roi_min`, mỗi số một câu lý do từ `ops_limits`/`ops_facts` | **Câu 2.10 (B7.5):** điền `operations` (`pic`, `approver_id`, `reviewers_on_shift`, `review_capacity_per_hour`, `max_queue_wait_minutes`, `stop_conditions`, `alert_channel`) và `legal` (`pii_fields_blocked_to_third_party`, `carrier_fault_requires_recorded_cause`) |
| **Câu 2.7 (B7.2):** hai bước tránh rò rỉ dữ liệu | Gửi các số `business` cho KS chạy thử | **Runbook 1–3** khớp đúng các số trong config, gồm dòng thời hạn dừng (bao nhiêu phút, ai bấm) |
| Chạy: `python -m lab10.eval --suite base --stage after --note "cổng vòng 1: ..."` và unittest. Báo nhóm nếu có ca mới hỏng | | **B7.6 Giờ cao điểm:** ai trực, mấy người, ngưỡng gọi thêm người, ngưỡng thu hẹp/tắt |

**Câu 2.8 (B7.3) · Behavioral test:**
- SP hoặc VH nghĩ ra tính chất + 2 ticket hiểm.
- KS chạy: `python -m lab10.trace --suite base --stage after --adhoc "..." --order O-10xx --customer C-xx`, dán kết quả vào phiếu.

**Sửa `config/operating_gates.json` lần lượt:** SP sửa `business` → push → VH pull, sửa `operations`/`legal` → push → KS pull rồi chạy eval.

Xong khi: báo cáo `after` không có ca mới hỏng so với base; test OK; `operations.pic` không trống.

---

## Phút 105–115 · Chốt cổng vòng 1 · Quyết định v1 (B8)

1. KS: `python -m lab10.checkpoint` → thấy `ĐÃ CHỐT cổng vòng 1`.
2. KS: `python -m lab10.eval --suite base --stage prepared` → `python -m lab10.gate --run runs/<mã>/report.json`.
3. Cả bàn chốt một trong bốn quyết định.
4. SP điền cột v1 (ba bằng chứng có mã lần chạy, dòng `decision_rule`, kho/hãng xấu nhất, ngày quyết định lại).
5. KS commit + push theo lệnh cuối B8.

Không ai sửa `lab10/guards_round1.py`, `config/operating_gates.round1.json`, `config/round1.lock`.

---

## Phút 125–135 · Nhận thẻ · Câu 3.0

| KS | SP | VH |
|---|---|---|
| `git pull --no-rebase --no-edit --allow-unrelated-histories -X ours upstream main` → `python -m lab10.grade --incident Sx` **trước khi sửa gì**. Ghi C0 | Một người lên bốc số (SP). Ghi `Thẻ đã bốc: Sx` đầu Phiếu C, push | Điền C1: cổng vòng 1 đỡ được gì, dòng nào vượt trần, sự cố có trong pre-mortem không |

Chỉ mở `incidents/Sx/card.md` của bàn mình.

---

## Phút 135–155 · Phân tích · Câu 3.1–3.4

| Mục | Giữ bút |
|---|---|
| C2 bảng soát lỗi: trace ≥ 2 ticket hỏng hai kiểu khác nhau (`python -m lab10.trace --suite Sx --ticket <ID> --seed 11`), ≥ 1 lỗi chìm | KS |
| C3 phần riêng theo thẻ (chỉ phần của số đã bốc; S4 bỏ qua) | VH |
| C4 HAZOP của thẻ ≥ 3 dòng (mục riêng, không ghi đè HAZOP vòng 1) | VH (KS góp dòng kỹ thuật) |
| C5 Câu 3.2 specification | SP |
| C5 Câu 3.3 giả định môi trường | VH |
| C6 fault tree trước khi sửa: KS vẽ nhánh kỹ thuật, SP nhánh kinh doanh, VH nhánh con người; mỗi lá có `ticket@seed` hoặc dòng báo cáo | Cả bàn |

---

## Phút 155–185 · Sửa · Câu 3.5–3.7

| KS | SP | VH |
|---|---|---|
| Sửa `guards.py` cho nguyên nhân kỹ thuật (giữ cổng vòng 1, thêm cổng mới) | Sửa `business` (`pilot_scope`, trần, ngân sách) nếu nguyên nhân là tiền/phạm vi | Sửa `operations` (`reviewers_on_shift`, `review_sampling_pct`, `decision_note`) và `legal` nếu nguyên nhân là người/pháp lý |
| **Câu 3.6:** thêm một hàm monitor trong `monitors.py` + đăng ký vào `MONITORS`; điền C8 | Đọc báo cáo: chi phí mỗi ticket, ROI, tổng hoàn so với trần | Đọc báo cáo: hàng chờ, số ca ùn, tỉ lệ chuyển người |
| Chạy: `eval --suite Sx --stage after`, `eval --suite base --stage after`, `grade --incident Sx` | C7 phần sửa con số (giảm hay ngăn) | C7 phần sửa người/quy trình |
| C7 phần code; C9 fault tree sau khi sửa | C10 risk register ≥ 1 dòng | C11 cập nhật checklist (cột PIC), runbook 4–5 |

Mỗi lần chỉ đổi **một** thứ rồi chạy lại, ghi vào `--note`. Xong khi: báo cáo có `monitor ✅` và `regression ✅`.

---

## Phút 185–200 · Quyết định v2 · Gom bài

| KS | SP | VH |
|---|---|---|
| Chạy lại `grade --incident Sx` trên bản cuối; chạy `python -m lab10.check_submission --collect`, sửa đến khi `ĐỦ THÀNH PHẦN` | **C12:** cột v2, đổi hay giữ so với v1 và vì con số nào, mã lần chạy ba mốc, **ba dòng bắt buộc** (giả định môi trường; giảm hay ngăn; đo lại gì trong pilot thật) | Điền `submission/submission.json` (`team`, `members` dạng `"HoVaTen-MSSV"`, `incident`, `decision_v1`, `decision_v2`, `three_lines` chép từ C12) |

Luật cứng: báo cáo còn dòng "vượt trần" hoặc còn ngưỡng đã ký chưa đạt thì **không chọn Tiếp tục**.

---

## Phút 200–240 · Demo · Nộp

| KS | SP | VH |
|---|---|---|
| Chiếu ba cột `base · prepared · after`; cổng vòng 1 đỡ được gì; phần sửa code | Quyết định v2 và con số đỡ nó; chi phí, ROI | Phần sửa người/quy trình; runbook; trả lời phản biện về người trực |

Sau demo: trả mọi con số đổi thử về bản v2 → KS chạy lại `grade` và `check_submission --collect` → push:

```bash
git add -u && git add submission templates TEAM.md PHAN-CONG.md && git commit -m "LAB 10: bài nộp" && git push -u origin main
```

**Mỗi người:** tự viết mục `## HoVaTen-MSSV` trong `TEAM.md` (phần việc, đóng góp, bằng chứng, exit ticket, có dùng AI cho phần nào) và **tự nộp link repo trên LMS** trước deadline.

---

## Ba luật để không giẫm chân nhau

1. **Mỗi file một người sửa** (bảng đầu trang). `operating_gates.json` chia theo mục và sửa lần lượt: pull → sửa → push.
2. **Chỉ máy KS chạy lệnh đánh giá**, để `runs/journal.jsonl` liền mạch với lịch sử git.
3. **Pull trước khi sửa, push ngay sau khi xong một mục.** Gặp xung đột thì gọi KS, không tự xoá file.
