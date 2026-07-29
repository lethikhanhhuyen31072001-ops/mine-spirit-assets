# Mine Spirit — Assets & CS Documents

Kho tài liệu và tài nguyên phục vụ vận hành thị trường US cho hai thương hiệu
**Mine Spirit** và **Taichi Gemstone**.

## Nội dung

### Email templates (Shopify)

| File | Dùng để làm gì |
|---|---|
| `mine-spirit-order-confirmation-DAN-VAO-SHOPIFY.html` | Bản chính thức — dán vào Shopify → Settings → Notifications → Order confirmation. Chứa biến Liquid (`{{ order_name }}`, `{{ line_items }}`…) nên mở bằng trình duyệt sẽ thấy chữ thô, đó là bình thường. |
| `mine-spirit-order-confirmation-XEM-TRUOC.html` | Bản xem trước, điền sẵn dữ liệu mẫu. Chỉ để xem bố cục, **không dán vào Shopify**. |

Trước khi dùng bản chính thức, thay chuỗi `DAN_LINK_LOGO_VAO_DAY` bằng URL công khai của logo.

### Logo

- `Logo Mine Spirit/` — 6 file gốc, ảnh vuông ~1254×1254 px
- `Logo Mine Spirit/for-email/` — bản đã cắt viền, thu nhỏ và nén cho email:
  - `minespirit-logo-dark.jpg` — dùng cho header nền tím `#120320`, hiển thị ở 200 px
  - `minespirit-logo-light.jpg` — dùng nếu header đổi sang nền trắng
  - `minespirit-icon.jpg` — dùng cho chữ ký email và footer

### Tài liệu quy trình CSKH

Không nằm trong repo này. Tài liệu quy trình được giữ nội bộ trên Lark.

## Ghi chú

Các mốc chính sách đang áp dụng cho Mine Spirit:

- Xử lý đơn: 1–3 business days
- Giao hàng: 15–25 business days sau khi gửi
- Miễn phí vận chuyển cho đơn từ $60
