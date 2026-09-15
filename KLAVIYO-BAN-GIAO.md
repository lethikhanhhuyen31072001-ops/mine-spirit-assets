# Bàn giao — Klaviyo Mine Spirit

Cập nhật: 07/08/2026 — bốn luồng và popup đều đã chạy. 11/09/2026 thêm luồng bỏ giỏ quiz $4.90; 14/09/2026 sửa bộ lọc chuyển giao ATC/Browse. Mở phiên mới thì đọc file này trước.

---

## 1. Tài khoản

| | |
|---|---|
| Tài khoản Klaviyo | Tên hiển thị **"Taichi Gemstones"** nhưng đang dùng cho **Mine Spirit** |
| Owner | tài khoản công ty (hỏi Huyền) |
| Người thao tác | Huyền — quyền Admin (hỏi Huyền) |
| Gói | **500 active profile / 5.000 lượt gửi mỗi tháng** (Billing 11/09/2026; kỳ tính 24 → 24; Auto-upgrades bật) |
| Shopify | `avk1em-rg.myshopify.com` → `minespirit.com` |
| Domain gửi | `send.minespirit.com` — đã Verified + Activated |
| Người gửi | Mine Spirit `<support@minespirit.com>` (nối Freshdesk) |
| Địa chỉ | 1500 N Grant St Ste N, Denver, CO 80203, United States |

⚠️ Huyền còn **một tài khoản Klaviyo riêng** tên "Mine Spirit" tự đăng ký — **không dùng cái đó**, rất dễ đăng nhập nhầm.

---

## 2. Đang ở đâu

### ✅ Luồng Checkout Abandonment — ĐANG CHẠY THẬT

Bật Live 05/08/2026. 10 mail, trải 18 ngày. Đã có khách thật đi qua và mở M1, M2.

### ✅ Luồng Add to Cart Abandonment — ĐANG CHẠY THẬT

Bật Live 06/08/2026, 11:23. 10 mail, trải 18 ngày, cấu trúc giống luồng Checkout.

Đã soát toàn bộ 20 khối trước khi bật: mọi delay đúng, khối 13 ngày đúng, và 5 mail cần tắt Smart Sending (M2, M3, M4, M7, M10) đều đã tắt. Đã gửi thử M1, M2, M9 về hộp thư thật — hiển thị đúng.

Khác luồng Checkout ở ba chỗ:
- Trigger `Added to Cart`, profile filter **hai dòng** (thêm `Checkout Started` = zero times **in the last 30 days**) để khách tiến vào thanh toán rơi khỏi luồng này. ⚠ Sửa 14/09/2026: trước là *since starting this flow* — thủng khi khách vào checkout trước rồi mới thêm giỏ (vd Buy it now), khách chạy song song hai luồng và nhận hai bản cùng lúc các mail tắt Smart Sending. Đã kiểm chứng 15/09/2026: profile bị trùng chỉ còn nhận mail của luồng Checkout
- Nội dung M1, M2 viết riêng cho tệp ATC — họ **chưa quyết mua**, không phải chỉ vấp ở bước cuối như tệp Checkout
- Mã giảm giá tung muộn hơn: M1, M2 không mã (luồng Checkout cũng vậy)

### ✅ Luồng Welcome Series — ĐANG CHẠY THẬT

Bật Live 07/08/2026. 3 mail: W1 ngay lập tức · W2 ngày 2 · W3 ngày 27.

Trigger là **List** (`Liste d'adresses e-mail` — danh sách popup đổ vào), không phải Metric. Re-entry: **No re-entry**. Không có biến event nào, chỉ `{% coupon_code 'WELCOME10' %}` và `{% unsubscribe_link %}`.

W3 có thêm Additional filter `Placed Order zero times since starting this flow` — người đã mua không cần nhận mail nhắc hạn mã.

Mỗi mail có **hàng 3 sản phẩm bấm được**, ảnh và link lấy thật từ web. Silver Larimar Necklace và Magical Energy Talisman xuất hiện ở cả 3 mail (2 món bán chạy nhất, 527 và 741 review).

### ✅ Popup thu email — ĐANG CHẠY

Form Klaviyo, tên "Email Popup", đổ vào list `Liste d'adresses e-mail`.

| Cài đặt | Giá trị |
|---|---|
| Hiện sau | 15 giây |
| Đóng rồi hiện lại | 30 ngày |
| Đã điền rồi | không hiện lại |
| Không hiện ở | `*/checkouts/*` |
| Địa điểm | United States (+ Vietnam tạm thời để test — **nhớ bỏ**) |
| Đối tượng | Don't show to existing Klaviyo profiles |
| Teaser | Có, góc dưới trái |

Mã `WELCOME10` — 10%, hạn 30 ngày, Activation At send time. Đã thử thật: trừ đúng 10% ở checkout.

### ✅ Luồng Browse Abandonment — ĐANG CHẠY THẬT

Bật Live 07/08/2026. 10 mail, 18 ngày, cùng lịch với hai luồng bám đuôi kia.

Trigger `Viewed Product`. **Profile filter BA dòng** (`Placed Order`, `Checkout Started`, `Added to Cart` đều zero times) — Browse là luồng nông nhất nên phải loại mọi hành vi sâu hơn. Từ 14/09/2026: `Checkout Started` và `Added to Cart` tính **in the last 30 days**; `Placed Order` vẫn *since starting this flow* (cùng lý do như luồng ATC ở trên).

Nội dung vốn đã viết đúng tệp khách, không phải viết lại. Chỉ sửa: thang mã (M1, M2 bỏ mã), 8 mã tĩnh → động, M2 tách 3 khối, thêm in đậm 6 chỗ, đồng nhất chân mail, thêm hàng sản phẩm ở M4/M9/M10.

**Luồng đông khách nhất trong ba luồng bám đuôi** — ~164 profile/tháng theo số Taichi, so với 146 của Checkout và 11 của ATC.

### ✅ Luồng Quiz – Checkout Abandonment $4.90 — ĐANG CHẠY THẬT

Bật Live 11/09/2026. 3 mail: C1 sau 1 giờ (tắt Smart Sending) · C2 sau 19 giờ · C3 sau 2 ngày. Trigger `Checkout Started`, trigger filter `Items contains Your Full Spirit Map` — gói $4.90 là bundle, sự kiện ghi 4 món con chứ không ghi tên gói. Luồng Checkout trang sức loại cả hai gói quiz bằng hai dòng `doesn't contain` nối **AND**. Chi tiết: `klaviyo-flow-quizcheckout-BANG-DUNG.txt`.

---

## 3. Lịch gửi (dùng chung cho 3 luồng bám đuôi)

Luồng Welcome có lịch riêng: W1 ngay · W2 ngày 2 · W3 ngày 27.

| # | Delay trước đó | Ngày thứ | Smart Sending |
|---|---|---|---|
| M1 | 1 giờ | 0,04 | giữ |
| M2 | 5 giờ | 0,25 | **TẮT** |
| M3 | 2 giờ | 0,33 | **TẮT** |
| M4 | 10 giờ | 0,75 | **TẮT** |
| M5 | 2 ngày | 2,75 | giữ |
| M6 | **13 ngày** | 15,75 | giữ |
| M7 | 2 giờ | 15,83 | **TẮT** |
| M8 | 1 ngày | 16,83 | giữ |
| M9 | 1 ngày | 17,83 | giữ |
| M10 | 12 giờ | 18,33 | **TẮT** |

Tắt Smart Sending ở mail nào cách mail trước **dưới 16 giờ** — nếu không Klaviyo nuốt mail mà không báo lỗi.

---

## 4. Mã giảm giá

Ba mã **động**, tạo trong Klaviyo → Content → Coupons, Activation = **At send time**:

| Mã | Giảm | Hạn | Dùng ở |
|---|---|---|---|
| `SPIRIT10` | 10% | 30 ngày | M3, M4 |
| `SPIRIT20` | 20% | 24 giờ | M5 |
| `SPIRIT35` | 35% | 48 giờ | M8, M9, M10 |

Trong template viết: `{% coupon_code 'SPIRIT10' %}`

Hạn 48 giờ của SPIRIT35 khớp với lời hứa trong ba mail cuối: M8 "48 hours" → M9 "24 hours left" → M10 "a few more hours".

---

## 5. Biến đã kiểm chứng bằng dữ liệu thật

**Ba sự kiện, ba bộ khoá khác nhau.** Đây là chỗ đã suýt hỏng ba lần — không được suy từ sự kiện này sang sự kiện kia.

| | `Checkout Started` | `Added to Cart` | `Viewed Product` |
|---|---|---|---|
| Tên sản phẩm | `item.title` | `Product Name` ⚠️ có dấu cách | `Name` |
| Cú pháp | trong vòng lặp | `{{ event\|lookup:'Product Name' }}` | `{{ event.Name }}` |
| Giá | `item.price` → `79.97` | `event.Price` → `149.97` | `event.Price` → **`"$39.94"`** |
| Tự thêm `$`? | Có | Có | **Không — đã có sẵn** |
| Ảnh | `item.product.images.0.src` | `event.ImageURL` | `event.ImageURL` |
| Link | `event.extra.checkout_url` | **không có** | `event.URL` |
| Nhiều món | Có, `{% for %}` | Không | Không |

**`Checkout Started`** — giỏ nhiều món nên phải lặp:
```
event.extra.checkout_url
event.extra.line_items → item.title / item.price / item.quantity
                         item.product.images.0.src
```

**`Added to Cart`** — không có `checkout_url`. Dùng link tự thêm giỏ, chạy được cả khi khách đổi máy:
```
https://minespirit.com/cart/{{ event.VariantID }}:{{ event.Quantity }}
```
Đã thử: link này đưa thẳng tới trang thanh toán với món hàng có sẵn.

⚠️ `event.URL` của `Added to Cart` trỏ về `.myshopify.com`, đừng dùng. Riêng `Viewed Product` thì `event.URL` trỏ đúng domain thật.

**Luồng Welcome** kích hoạt bằng danh sách nên **không có biến event nào** — chỉ `{% coupon_code %}` và `{% unsubscribe_link %}`.

---

## 6. Bẫy đã gặp — đừng lặp lại

| Bẫy | Hậu quả |
|---|---|
| `<a href="{% unsubscribe %}">` | Vỡ HTML. Phải dùng `{% unsubscribe_link %}` |
| Smart Sending bật mặc định | Nuốt mail cách nhau dưới 16 giờ, **không báo lỗi** |
| Sửa template sau khi gắn vào flow | Flow vẫn dùng bản cũ — phải dán lại trong flow |
| Gõ nhầm Days/Hours | 13 ngày thành 13 giờ, cả luồng dồn một ngày |
| Dùng biến của sự kiện khác | Ô sản phẩm trống, ảnh vỡ |
| "Add past profiles" | Đẩy hàng loạt khách cũ vào luồng, cạn quota |

---

## 7. Quy ước trình bày (đã chốt)

- **Icon thân mail:** ký tự ✦ (`&#10022;`) màu vàng `#C6A15B`. Không dùng emoji trong thân mail
- **Emoji:** chỉ ở subject và preview text
- **In đậm:** tối đa 2–3 chỗ, chỉ đậm câu trả lời nỗi lo của người đọc
- **In nghiêng:** chỉ dùng cho trích dẫn review
- **Tách khối:** khi là danh sách mục ngang hàng (3 lý do, 5 cam kết) — nền `#F7F4FB`, viền trái vàng
- **Chân trang:** địa chỉ Denver + `{% unsubscribe_link %}`, chữ 12px màu nhạt, không icon

Review dùng trong mail là **review thật lấy từ minespirit.com**: Angel P., Jennifer G., Vicki R., Angie B., Dawn R., Misty L.

---

## 8. File trong dự án

```
klaviyo-templates/                  33 file: CHECKOUT / ATC / BROWSE ×10, WELCOME ×3
mine-spirit-LUONG-BAM-DUOI-*.html   3 file gốc luồng bám đuôi
mine-spirit-LUONG-WELCOME.html      file gốc luồng Welcome
klaviyo-flow-checkout-BANG-DUNG.txt bảng dựng flow Checkout
klaviyo-flow-atc-BANG-DUNG.txt      bảng dựng flow Add to Cart
klaviyo-anh-prompt.txt              prompt tạo ảnh (chỉ M7, M8 thực sự cần)
klaviyo-dns-records.txt             bản ghi DNS đã dùng
DEMO-*.html                         bản xem thử, không nạp lên Klaviyo
```

**Sản phẩm dùng trong mail** (ảnh + link thật từ web): Silver Larimar Necklace $79.97 · Magical Energy Talisman $39.94 · 7 Chakra Pendant $24.97 · 108 Amazonite Mala $36.97 · Angel Aura Cluster $34.97

**Cách sửa template:** sửa file gốc `mine-spirit-LUONG-BAM-DUOI-*.html` → chạy lại script tách → chạy audit → nạp lên Klaviyo. Đừng sửa thẳng vào 30 file tách, sẽ bị ghi đè.

**Script audit:**
```bash
python ~/.claude/skills/klaviyo-abandonment-flow/scripts/audit_templates.py klaviyo-templates
```

**Skill:** `klaviyo-abandonment-flow` — chứa toàn bộ quy trình, bẫy, và quy ước trình bày.

---

## 9. Việc còn lại

Bốn luồng và popup đều đã chạy. Không còn việc dựng, chỉ còn vận hành.

1. **Bỏ Vietnam khỏi Location của popup** — đã thêm để test. Để lại thì thu email khách Việt Nam: không mua được vì giá và phí ship tính theo thị trường Mỹ, nhưng vẫn tính tiền profile.

2. **Theo dõi quota hàng tuần** — 

   Các luồng chạy chung gói 500 profile / 5.000 lượt mỗi tháng (11/09/2026: dùng 193 profile, 461 lượt). Profile gần **400** thì nhắc admin nâng gói — nhất là khi lead quiz bắt đầu chảy vào Klaviyo. Auto-upgrades đang bật: vượt lượt gửi thì Klaviyo tự nâng gói và tính thêm tiền.

3. **Sau 6–8 tuần, đọc Flow Analytics** khi mỗi mail đủ ~100 người nhận. Cột quan trọng nhất là **Placed Order rate** và **Skipped**.
   - Skipped khác 0 → có mail đang bị nuốt, kiểm tra Smart Sending và profile filter
   - Mail nào Placed Order gần 0 → cân nhắc cắt, nhất là ba mail cuối đang tặng 35%

4. **Ảnh chụp thật cho M7 và M8** của luồng Checkout và ATC. M8 lập luận về vân đá độc bản nên ảnh AI sẽ tự phá lập luận — phải là ảnh thật.

5. ~~Nâng gói trước khi bật ads~~ — đã ở gói 500 profile / 5.000 lượt (thấy 11/09/2026).
