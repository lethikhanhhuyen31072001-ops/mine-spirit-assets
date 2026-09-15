# -*- coding: utf-8 -*-
"""Dung trang xem thu 3 mail Bo Gio $4.90 (QUIZCHECKOUT-C1..C3), kem ban dich tieng Viet.

Chay:  python klaviyo-quizcheckout-xem-truoc.py
Ra:    mine-spirit-XEM-TRUOC-QUIZCHECKOUT.html (cung thu muc)

Khoi san pham trong template dung bien Klaviyo; o day thay bang du lieu mau
(goi $4.90 that tren Shopify) de xem duoc. File template goc giu nguyen.
"""
import io, os, re, base64, tempfile, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, "klaviyo-templates")
OUT = os.path.join(HERE, "mine-spirit-XEM-TRUOC-QUIZCHECKOUT.html")
LOGO_URL = ("https://raw.githubusercontent.com/lethikhanhhuyen31072001-ops/"
            "mine-spirit-assets/main/Logo%20Mine%20Spirit/for-email/minespirit-logo-dark.jpg")
PROD_URL = "https://cdn.shopify.com/s/files/1/0831/2481/4083/files/Goi-1-Map-Report-4.90.png?width=400"
PROD_TITLE = "Your Full Reading — The Whole Set"
PROD19_URL = "https://cdn.shopify.com/s/files/1/0831/2481/4083/files/Goi-2-Map-Report-5-Solutions-19.png?width=400"
# Cong tac trong template (tu 15/09/2026): gio co mon "Your Full Spirit Map" = goi $4.90, con lai = goi $19
SWITCH = re.compile(r"{% if 'Your Full Spirit Map' in event\.Items %}(.*?){% else %}(.*?){% endif %}", re.S)
# Cong tac trong ban dich: [[chu cho $4.90||chu cho $19]]
VI_SWITCH = re.compile(r"\[\[(.*?)\|\|(.*?)\]\]", re.S)
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128"}


def data_uri(url, cache_name, box):
    cache = os.path.join(tempfile.gettempdir(), cache_name)
    if os.path.exists(cache):
        return io.open(cache, encoding="utf-8").read().strip()
    raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45).read()
    try:
        from PIL import Image
        im = Image.open(io.BytesIO(raw)).convert("RGB")
        im.thumbnail(box)
        buf = io.BytesIO(); im.save(buf, "JPEG", quality=76, optimize=True)
        raw = buf.getvalue()
    except Exception:
        pass
    uri = "data:image/jpeg;base64," + base64.b64encode(raw).decode()
    io.open(cache, "w", encoding="utf-8").write(uri)
    return uri


def render_sample(html, logo, prod, prod19=None, is490=True):
    """Thay the Klaviyo bang du lieu mau; is490 chon nhanh cong tac: goi $4.90 hay goi $19."""
    html = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    html = SWITCH.sub(lambda m: m.group(1) if is490 else m.group(2), html)
    html = html.replace("{% for item in event.extra.line_items %}", "").replace("{% endfor %}", "")
    html = re.sub(r"{% if item\.quantity > 1 %}.*?{% endif %}", "", html, flags=re.S)
    html = html.replace("{{ item.title }}", PROD_TITLE)
    html = html.replace("{{ item.price|floatformat:2 }}", "4.90")
    html = html.replace("{{ item.product.images.0.src }}", prod)
    # C1 tu 11/09/2026 dat anh goi co dinh (Klaviyo ghi 4 mon con, khong ghi ten goi)
    html = re.sub(r"https://cdn\.shopify\.com/s/files/[^\"]*Goi-1-Map-Report-4\.90\.png[^\"]*", prod, html)
    if prod19:
        html = re.sub(r"https://cdn\.shopify\.com/s/files/[^\"]*Goi-2-Map-Report-5-Solutions-19\.png[^\"]*", prod19, html)
    html = html.replace("{{ event.extra.checkout_url }}", "#")
    html = html.replace("{% unsubscribe_link %}", "#")
    html = html.replace(LOGO_URL, logo)
    left = re.findall(r"{{.*?}}|{%.*?%}", html)
    assert not left, "Con the Klaviyo chua thay: %s" % left[:3]
    return html


# (file, id, moc, cach mail truoc, subject EN, preview EN, subject VI, preview VI, than VI)
# Ban 2 (11/09/2026): viet lai theo noi dau — dung chinh loi khach trong quiz that.
MAILS_CU_KHONG_DUNG = [
("QUIZCHECKOUT-C1", "C1", "+1 giờ", "Sau khi bỏ checkout",
 "Your reading is waiting at the last step 🕯️", "Nothing was charged. Everything is saved.",
 "Bản đọc của chị đang chờ ở bước cuối 🕯️", "Chưa trừ tiền. Mọi thứ vẫn được lưu.",
 """<h4>Chị dừng lại khi chỉ còn một bước nữa</h4>
<p>Chị đã chọn bản đọc đầy đủ và đi tới tận trang thanh toán. Rồi có việc gì đó kéo chị đi — chuyện đó bình thường.</p>
<p><b>Chưa có khoản nào bị trừ</b>, và <b>câu trả lời cùng giỏ hàng của chị vẫn được lưu</b>. Chị không phải làm lại quiz.</p>
<div class="vbox"><p class="vdim">Khối sản phẩm: ảnh gói, tên <b>Your Full Reading — The Whole Set</b> và giá $4.90 — Klaviyo lấy từ đúng giỏ của từng khách.</p></div>
<p class="vcta">Nút: Hoàn tất và mở bản đọc của tôi</p>
<p>Email của chị <b>đã được điền sẵn</b> — chị không phải gõ lại.</p>
<p>Không muốn gõ số thẻ? Có thể trả bằng PayPal và Apple Pay. <span class="vwarn">cần xác nhận đang bật trước khi chạy</span></p>
<p class="vdim">Ba cam kết dưới nút: Trả một lần, không gia hạn · Hoàn tiền trong 28 ngày · Bản số — không phải giao hàng</p>"""),

("QUIZCHECKOUT-C2", "C2", "+20 giờ", "Hôm sau",
 "What your $4.90 opens 🔑", "Seven things, one payment, nothing renews.",
 "$4.90 của chị mở ra những gì 🔑", "Bảy thứ, trả một lần, không gia hạn.",
 """<h4>Đây là mọi thứ bên trong</h4>
<p>Trong giỏ, nó hiện tên là <b>Your Full Reading — The Whole Set</b>. Đó chính là gói Map &amp; Report chị đã chọn ở cuối bài quiz — cùng một thứ, chỉ là tên dài hơn.</p>
<div class="vbox"><span class="vlab">NHỮNG GÌ NÓ MỞ RA</span>
<p>✦ Bầu trời thật ngày chị sinh — mười hành tinh, tính chứ không đoán<br>
✦ Mười hai thẻ tháng cho 2026 và 2027<br>
✦ Mười năm tới, đọc từng năm<br>
✦ Sáu điều chị đang trải qua<br>
✦ Cả bảy tầng được chấm điểm, gọi tên tầng yếu nhất<br>
✦ Nghi thức chín mươi giây đầu tiên, cho tối nay<br>
✦ Lộ trình năm bước, sắp theo đúng bản đồ của chị</p></div>
<div class="vbox dark"><span class="vlab">CẢ BẢY, VỚI</span> <span class="vbig">$4.90</span>
<p><b>Trả một lần. Không gia hạn.</b> Thuộc về chị.</p></div>
<p class="vcta">Nút: Mở cả bảy — $4.90</p>
<p class="vdim">Dưới nút: Đưa chị về thẳng giỏ hàng, email đã điền sẵn.</p>"""),

("QUIZCHECKOUT-C3", "C3", "Ngày 3", "+2 ngày",
 "28 days to change your mind 🤍", "One payment. Nothing to ship. Nothing renews.",
 "28 ngày để đổi ý 🤍", "Trả một lần. Không giao hàng. Không gia hạn.",
 """<h4>Gần như không mất gì khi mở nó</h4>
<p>Nếu chị vẫn đang cân nhắc, cũng hợp lý thôi. Đây là chính xác những gì chị đang mạo hiểm.</p>
<div class="vbox"><p><b>✦ Hai mươi tám ngày để đổi ý</b><br>Trả lời bất kỳ email nào của chúng tôi trong 28 ngày, <b>chúng tôi hoàn lại $4.90</b>. Không phải điền form.</p></div>
<div class="vbox"><p><b>✦ Trả một lần, thế là xong</b><br><b>Không gia hạn</b>, không tính thêm gì về sau. Bản đọc thuộc về chị, đọc lại được.</p></div>
<div class="vbox"><p><b>✦ Bản đọc số — không phải giao hàng</b><br>Không phải đưa địa chỉ, không phải chờ bưu điện.</p></div>
<p class="vcta">Nút: Mở bản đọc của tôi — $4.90</p>
<p class="vdim">Dưới nút: Giỏ hàng và câu trả lời của chị vẫn được lưu.</p>
<p>Nếu bây giờ chưa phải lúc, cũng không sao. Đây là lá thư cuối chúng tôi gửi về giỏ hàng này.</p>"""),
]

MAILS = [
("QUIZCHECKOUT-C1", "C1", "+1 giờ", "Sau khi bỏ checkout",
 "It was never just tiredness 🕯️", "You saw the number. The reason is one tap away.",
 "Chưa bao giờ chỉ là mệt 🕯️", "Chị đã thấy con số. Lý do nằm cách một chạm.",
 """<h4>Chị đã thấy con số. Giờ hãy xem vì sao.</h4>
<p>Ngay trước trang thanh toán, chị đã thấy một điều mà hầu hết mọi người chưa bao giờ thấy được viết ra: phần nào trong chị đang cạn nhất — và cạn tới mức nào.</p>
<p>Có thể chị vẫn gọi nó là mệt. Nhưng nếu đó không phải là mệt, mà là một chỗ rò — bắt đầu từ sớm hơn chị tưởng thì sao?</p>
<div class="vbox dark"><span class="vlab">BẢN ĐỌC CỦA CHỊ, TỚI LÚC NÀY</span>
<p>Tầng yếu nhất và điểm số của nó — <b>✓ chị đã thấy</b><br>
<b>Vì sao nó cạn trước tiên</b> — 🔒 đang khoá<br>
<b>Những tháng tới sẽ đè lên nó</b> — 🔒 đang khoá<br>
<b>Việc đầu tiên nên làm, ngay tối nay</b> — 🔒 đang khoá[[||<br>
<b>Năm lời giải, viết theo bản đồ của chị</b> — 🔒 đang khoá]]</p>
<p class="vdim">Một chạm là mở hết.</p></div>
<div class="vbox"><p class="vdim">Khối sản phẩm: ảnh gói, tên <b>[[Your Full Reading — The Whole Set||Map &amp; Report + 5 Solutions — The Complete Reading]]</b>, [[$4.90||$19]] · vẫn còn trong giỏ.</p></div>
<p><b>Chưa có khoản nào bị trừ, và câu trả lời của chị vẫn được lưu</b> — chị không phải làm lại quiz.</p>
<p class="vcta">Nút: Xem vì sao — [[$4.90||$19]]</p>
<p class="vdim">Dưới nút: Email của chị đã được điền sẵn. Không muốn gõ số thẻ? Có thể trả bằng PayPal và Apple Pay.</p>
<p class="vdim">Ba cam kết: Trả một lần, không gia hạn · Hoàn tiền trong 28 ngày · Bản số — không phải giao hàng</p>"""),

("QUIZCHECKOUT-C2", "C2", "+20 giờ", "Hôm sau",
 "How long have you been calling it “just tired”? 🌙", "Your reading puts a name to it — tonight.",
 "Chị gọi nó là “chỉ mệt thôi” bao lâu rồi? 🌙", "Bản đọc gọi đúng tên nó — ngay tối nay.",
 """<h4>Chị đã gọi nó là “chỉ mệt thôi” bao lâu rồi?</h4>
<p>Vài tháng? Một năm? Lâu hơn nữa?</p>
<p>Đó là chữ dễ với tới nhất. Nó che được những lần thức giấc lúc 3 giờ sáng, cái đầu vẫn chạy khi cơ thể đã dừng, những buổi sáng bắt đầu mà đã thấy kiệt. Và nó để mọi người — kể cả chị — cho qua mà không phải hỏi thêm gì.</p>
<div class="vbox dark"><span class="vbig">63%</span> <span class="vlab">người làm quiz này đồng ý</span>
<p><i>“Đôi khi tôi thấy trống rỗng và tự hỏi tất cả cố gắng này rốt cuộc để làm gì.”</i></p></div>
<p>Chị không phải người duy nhất mang câu nói đó. <b>Nhưng mang nó mà không có tên gọi mới là thứ khiến nó nặng.</b></p>
<div class="vbox"><span class="vlab">BẢN ĐỌC GỌI ĐÚNG TÊN NÓ</span>
<p>✦ Tầng nào trong bảy tầng của chị cạn trước tiên — và vì sao<br>
✦ Những tháng tới sẽ đè lên nó nặng nhất, kèm việc nên làm trong từng tháng<br>
✦ Lộ trình năm bước theo đúng thứ tự hợp với chị — bắt đầu bằng nghi thức chín mươi giây tối nay</p></div>
<p>[[$4.90, một lần — có lẽ còn ít hơn số chị đã chi cho người khác hôm nay.||$19, một lần — có lẽ còn ít hơn số chị đã chi cho người khác trong tuần này.]]</p>
<p class="vcta">Nút: Gọi đúng tên nó — [[$4.90||$19]]</p>
<p class="vdim">Dưới nút: Về lại giỏ hàng đã lưu, email điền sẵn. Trong giỏ nó có tên “[[Your Full Reading — The Whole Set||Map &amp; Report + 5 Solutions — The Complete Reading]]”.</p>"""),

("QUIZCHECKOUT-C3", "C3", "Ngày 3", "+2 ngày",
 "When did you last buy something just for you? 🤍", "You carry a lot that nobody counts. This one is yours.",
 "Lần cuối chị mua một thứ chỉ cho riêng mình là khi nào? 🤍", "Chị gánh nhiều thứ không ai đếm. Thứ này là của chị.",
 """<h4>Những thứ chị gánh mà không ai đếm</h4>
<p>Trong quiz, chị đã được hỏi điều gì đang lấy của chị nhiều nhất lúc này, mà hầu như chẳng ai đếm tới. Dù chị chọn gì, chị đã trả lời thật lòng. Đây là những câu được chọn nhiều nhất:</p>
<div class="vbox"><p><b style="color:#C6A15B">43%</b> &nbsp;Một mất mát, hay một chương đã khép, vẫn còn nằm trong lòng tôi<br>
<b style="color:#C6A15B">28%</b> &nbsp;Tiền bạc hay tương lai khiến tôi khó thả lỏng<br>
<b style="color:#C6A15B">27%</b> &nbsp;Cơ thể tôi đã đổi khác, và tôi không còn tin nó như trước<br>
<b style="color:#C6A15B">24%</b> &nbsp;Chăm lo cho một người nhiều hơn những gì người khác thấy</p></div>
<p>Và cứ 100 người thì 55 người đồng ý với câu này: <i>“Đặt người khác lên trước thường khiến tôi còn lại rất ít sức cho chính mình.”</i></p>
<p>Vậy đây là một ý nhỏ, hơi vô lý: <b>chi [[$4.90||$19]] cho một thứ chỉ dành riêng cho chị.</b> Không phải cho nhà cửa. Không phải cho gia đình. Cho chị.</p>
<div class="vbox"><p>✦ Đổi ý? Trả lời trong 28 ngày và <b>chúng tôi hoàn lại [[$4.90||$19]]</b>. Không cần điền form.<br>
✦ Trả một lần. Không gia hạn.<br>
✦ Bản số — không phải giao hàng, không phải chờ đợi.</p></div>
<p class="vcta">Nút: Thứ này là cho tôi — [[$4.90||$19]]</p>
<p class="vdim">Dưới nút: Giỏ hàng và câu trả lời của chị vẫn được lưu.</p>
<p>Nếu bây giờ chưa phải lúc, cũng không sao. Đây là lá thư cuối chúng tôi gửi về giỏ hàng này.</p>"""),
]

CSS = """<style>
:root{--bg:#150C2E;--bg2:#1E1440;--gold:#C6A15B;--pale:#EDE9F5;--mute:#9C93B5;--line:#2E2350;--warn:#F2A8B6}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--pale);font-family:"Be Vietnam Pro",-apple-system,"Segoe UI",sans-serif;font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
.wrap{max-width:760px;margin:0 auto;padding:0 18px 80px}
h1{margin:0;font-size:clamp(1.7rem,5vw,2.4rem);font-weight:700;letter-spacing:-.02em;line-height:1.1;color:#fff}
.top{padding:52px 0 30px}
.kick{font-family:"IBM Plex Mono",monospace;font-size:.64rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold)}
.lede{color:var(--mute);font-size:1.02rem;max-width:60ch;margin-top:12px}
.lede b{color:#fff}
.rail{height:2px;width:44px;background:var(--gold);border-radius:2px;margin:18px 0 0}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:8px;margin-top:22px}
.facts div{background:var(--bg2);border:1px solid var(--line);border-radius:9px;padding:11px 13px;font-size:.84rem;color:var(--mute);line-height:1.5}
.facts b{color:#fff;font-weight:600}
.facts .ft{display:block;font-family:"IBM Plex Mono",monospace;font-size:.58rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:4px}
.nav{display:flex;flex-wrap:wrap;gap:7px;margin-top:22px;padding-top:20px;border-top:1px solid var(--line)}
.nav a{font-family:"IBM Plex Mono",monospace;font-size:.72rem;color:var(--pale);text-decoration:none;background:var(--bg2);border:1px solid var(--line);border-radius:99px;padding:7px 14px}
.nav a:hover{border-color:var(--gold);color:var(--gold)}
.mail{margin-top:42px;scroll-margin-top:16px}
.inbox{background:var(--bg2);border:1px solid var(--line);border-radius:12px 12px 0 0;padding:15px 18px;display:grid;grid-template-columns:78px 1fr;gap:14px}
.when{text-align:center}
.when .id{font-family:"IBM Plex Mono",monospace;font-size:.68rem;color:var(--gold);letter-spacing:.1em}
.when .d{font-family:"IBM Plex Mono",monospace;font-size:.86rem;color:#fff;font-weight:500;margin-top:3px}
.when .r{font-size:.62rem;color:var(--mute);margin-top:2px;line-height:1.3}
.meta .from{font-size:.72rem;color:var(--mute);font-family:"IBM Plex Mono",monospace}
.meta .s{font-size:1.04rem;font-weight:600;color:#fff;line-height:1.35;margin-top:4px}
.meta .p{font-size:.86rem;color:var(--mute);margin-top:3px}
.frame{border:1px solid var(--line);border-top:none;overflow:hidden}
.frame > table{width:100% !important}
.sample{background:#2A1F47;color:var(--mute);font-family:"IBM Plex Mono",monospace;font-size:.66rem;letter-spacing:.06em;padding:7px 14px;border-left:1px solid var(--line);border-right:1px solid var(--line)}
.vi{background:var(--bg2);border:1px solid var(--line);border-top:none;border-radius:0 0 12px 12px;padding:22px 24px 26px}
.vi-h{display:flex;flex-wrap:wrap;gap:10px;align-items:baseline;padding-bottom:14px;margin-bottom:16px;border-bottom:1px dashed var(--line)}
.vi-h .tag{font-family:"IBM Plex Mono",monospace;font-size:.58rem;letter-spacing:.14em;text-transform:uppercase;background:rgba(198,161,91,.15);color:var(--gold);padding:4px 9px;border-radius:4px}
.vi-h .note{font-size:.78rem;color:var(--mute)}
.vi-sub{font-size:.85rem;color:var(--mute);margin-bottom:16px;line-height:1.5}
.vi-sub b{color:#fff;font-weight:500}
.vi h4{margin:0 0 12px;font-size:1.12rem;font-weight:600;color:#fff;line-height:1.35}
.vi p{margin:0 0 11px;font-size:.94rem;line-height:1.68;color:#CFC8DF}
.vi p:last-child{margin-bottom:0}
.vi b{color:#fff;font-weight:600}
.vbox{background:rgba(255,255,255,.045);border-left:3px solid var(--gold);border-radius:0 8px 8px 0;padding:14px 16px;margin:0 0 11px}
.vbox.dark{background:rgba(0,0,0,.25)}
.vlab{display:inline-block;font-family:"IBM Plex Mono",monospace;font-size:.6rem;letter-spacing:.13em;text-transform:uppercase;color:var(--gold);margin-bottom:8px}
.vbig{font-size:1.7rem;font-weight:700;color:var(--gold);line-height:1.1;margin-left:6px}
.vdim{color:var(--mute) !important;font-size:.85rem !important}
.vcta{font-family:"IBM Plex Mono",monospace;font-size:.82rem !important;color:var(--gold) !important;background:rgba(198,161,91,.1);border-radius:6px;padding:9px 13px;display:inline-block}
.vwarn{font-family:"IBM Plex Mono",monospace;font-size:.62rem;letter-spacing:.06em;color:var(--warn);background:rgba(168,58,82,.22);padding:2px 7px;border-radius:4px;white-space:nowrap}
.switch{position:sticky;top:0;z-index:5;display:flex;gap:6px;padding:10px 0;margin-top:14px;background:var(--bg)}
.switch button{flex:1;font:600 .84rem "Be Vietnam Pro",sans-serif;color:var(--pale);background:var(--bg2);border:1px solid var(--line);border-radius:99px;padding:10px 14px;cursor:pointer}
.switch button.on{background:var(--gold);border-color:var(--gold);color:#150C2E}
.v19{display:none}
.wrap.show19 .v19{display:block}
.wrap.show19 .v490{display:none}
footer{margin-top:56px;padding-top:20px;border-top:1px solid var(--line);font-size:.8rem;color:var(--mute)}
footer code{font-family:"IBM Plex Mono",monospace;color:#CFC8DF}
@media (max-width:560px){.inbox{grid-template-columns:1fr;gap:9px}.when{text-align:left;display:flex;gap:9px;align-items:baseline}.vi{padding:18px 16px 22px}}
</style>"""


def build():
    logo = data_uri(LOGO_URL, "minespirit-logo-datauri.txt", (420, 420))
    prod = data_uri(PROD_URL, "minespirit-goi490-datauri.txt", (300, 300))
    prod19 = data_uri(PROD19_URL, "minespirit-goi19-datauri.txt", (300, 300))
    p = ['<title>Ba Mail Bỏ Giỏ Quiz</title>',
         '<link rel="preconnect" href="https://fonts.googleapis.com">',
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">',
         CSS, '<div class="wrap"><div class="top">',
         '<div class="kick">Mine Spirit · Klaviyo · Bản xem thử</div>',
         '<h1>Ba mail bỏ giỏ quiz — $4.90 và $19</h1><div class="rail"></div>',
         '<p class="lede">Gửi cho người <b>đã làm quiz, đã bấm mua gói $4.90 hoặc $19 và vào tới trang thanh toán</b> rồi bỏ dở. Một bộ 3 mail cho cả hai gói — <b>bấm nút bên dưới để xem khách mỗi gói thấy gì</b>, kèm bản dịch tiếng Việt.</p>',
         '<div class="facts">'
         '<div><span class="ft">Trigger</span><b>Checkout Started</b>, Items chứa <b>Your Full Spirit Map</b> (gói $4.90) <b>HOẶC</b> tên gói $19</div>'
         '<div><span class="ft">Công tắc trong mail</span>Giỏ có món <b>Your Full Spirit Map</b> → hiện gói $4.90; không có → hiện gói $19. Klaviyo tự chọn cho từng khách</div>'
         '<div><span class="ft">Link mọi nút</span><b>checkout_url</b> — trả khách về đúng giỏ cũ, email điền sẵn</div>'
         '<div><span class="ft">Bẫy phải tránh</span>C1 <b>tắt Smart Sending</b>, nếu không có thể bị nuốt ngay sau mail luồng quiz</div>'
         '</div>',
         '<nav class="nav">']
    for m in MAILS:
        p.append('<a href="#%s">%s · %s</a>' % (m[1], m[1], m[2]))
    p.append('</nav><div class="switch"><button class="on" data-v="v490">Khách bỏ giỏ $4.90 thấy</button>'
             '<button data-v="v19">Khách bỏ giỏ $19 thấy</button></div></div>')
    for f, mid, day, rel, subj, pre, vsubj, vpre, vbody in MAILS:
        raw = io.open(os.path.join(TPL, f + ".html"), encoding="utf-8").read()
        p.append('<div class="mail" id="%s">' % mid)
        p.append('<div class="inbox"><div class="when"><div class="id">%s</div><div class="d">%s</div><div class="r">%s</div></div>'
                 '<div class="meta"><div class="from">Mine Spirit &lt;support@minespirit.com&gt;</div>'
                 '<div class="s">%s</div><div class="p">%s</div></div></div>' % (mid, day, rel, subj, pre))
        for key, is490, lab in (("v490", True, "Khách bỏ giỏ gói $4.90 thấy bản này"),
                                ("v19", False, "Khách bỏ giỏ gói $19 thấy bản này")):
            html = render_sample(raw, logo, prod, prod19, is490)
            body = VI_SWITCH.sub(lambda m, a=is490: m.group(1) if a else m.group(2), vbody)
            p.append('<div class="%s"><div class="sample">%s</div>' % (key, lab))
            p.append('<div class="frame">%s</div>' % html)
            p.append('<div class="vi"><div class="vi-h"><span class="tag">Bản dịch tiếng Việt</span>'
                     '<span class="note">Để chị đọc hiểu — mail gửi đi vẫn là bản tiếng Anh ở trên</span></div>'
                     '<div class="vi-sub"><b>Tiêu đề:</b> %s<br><b>Dòng xem trước:</b> %s</div>%s</div></div>' % (vsubj, vpre, body))
        p.append('</div>')
    p.append('<footer>Ba file gốc: <code>klaviyo-templates/QUIZCHECKOUT-C1..C3.html</code> · '
             'Bảng dựng: <code>klaviyo-flow-quizcheckout-BANG-DUNG.txt</code> · '
             'Link huỷ đăng ký và link giỏ thay bằng dấu # để xem thử; file template gốc giữ nguyên.</footer></div>'
             '<script>document.querySelectorAll(".switch button").forEach(function(b){b.onclick=function(){'
             'document.querySelector(".wrap").classList.toggle("show19",b.dataset.v==="v19");'
             'document.querySelectorAll(".switch button").forEach(function(x){x.classList.toggle("on",x===b)})}})</script>')
    out = "".join(p)
    io.open(OUT, "w", encoding="utf-8").write(out)
    return out


if __name__ == "__main__":
    o = build()
    print("da ghi", os.path.basename(OUT), "-", round(len(o) / 1024), "KB")
    print("so mail:", o.count('class="mail"'), "| so ban dich:", o.count('class="vi"'))
    print("con the klaviyo:", bool(re.search(r"{{|{%", o)), "| con anh ngoai:", "raw.githubusercontent" in o or "cdn.shopify.com" in o)
