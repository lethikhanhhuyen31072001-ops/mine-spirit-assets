# -*- coding: utf-8 -*-
"""Dung trang xem thu 6 mail Quiz -> $4.90, kem ban dich tieng Viet."""
import io, os, base64, tempfile, urllib.request

TPL = r"D:\DOCUMENT 1\US\klaviyo-templates"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mine-spirit-XEM-TRUOC-QUIZ.html")
LOGO_URL = ("https://raw.githubusercontent.com/lethikhanhhuyen31072001-ops/"
            "mine-spirit-assets/main/Logo%20Mine%20Spirit/for-email/minespirit-logo-dark.jpg")

def logo_data_uri():
    cache = os.path.join(tempfile.gettempdir(), "minespirit-logo-datauri.txt")
    if os.path.exists(cache):
        return io.open(cache, encoding="utf-8").read().strip()
    raw = urllib.request.urlopen(LOGO_URL, timeout=45).read()
    try:
        from PIL import Image
        im = Image.open(io.BytesIO(raw)).convert("RGB")
        im.thumbnail((420, 420))
        buf = io.BytesIO(); im.save(buf, "JPEG", quality=72, optimize=True)
        raw = buf.getvalue()
    except Exception:
        pass
    uri = "data:image/jpeg;base64," + base64.b64encode(raw).decode()
    io.open(cache, "w", encoding="utf-8").write(uri)
    return uri

# ---- noi dung: (file, id, moc, cach mail truoc, subject EN, preview EN,
#                 subject VI, preview VI, than mail VI dang HTML) ----
MAILS = [
("QUIZ-Q1", "Q1", "+1 gi\u1edd", "Ngay sau khi l\u00e0m quiz",
 "Your reading is still open &#128367;&#65039;", "Nothing you entered is lost.",
 "B\u1ea3n \u0111\u1ecdc c\u1ee7a ch\u1ecb v\u1eabn \u0111ang m\u1edf &#128367;&#65039;", "Kh\u00f4ng m\u1ea5t g\u00ec c\u1ea3.",
 u"""<h4>B\u1ea3n \u0111\u1ecdc c\u1ee7a ch\u1ecb v\u1eabn \u0111ang m\u1edf</h4>
<p>Ch\u1ecb \u0111\u00e3 ng\u1ed3i v\u1edbi hai m\u01b0\u01a1i m\u1ed1t c\u00e2u h\u1ecfi v\u1ec1 tu\u1ea7n v\u1eeba r\u1ed3i c\u1ee7a m\u00ecnh, th\u1eadt l\u00f2ng. \u0110\u00f3 m\u1edbi l\u00e0 ph\u1ea7n kh\u00f3, v\u00e0 ch\u1ecb \u0111\u00e3 l\u00e0m xong.</p>
<p>B\u1ea3y t\u1ea7ng c\u1ee7a ch\u1ecb \u0111\u00e3 \u0111\u01b0\u1ee3c ch\u1ea5m \u0111i\u1ec3m, t\u1ea7ng m\u1ecfng nh\u1ea5t \u0111\u00e3 \u0111\u01b0\u1ee3c g\u1ecdi t\u00ean. <b>Kh\u00f4ng c\u00f3 g\u00ec ch\u1ecb nh\u1eadp b\u1ecb m\u1ea5t</b> \u2014 t\u1ea5t c\u1ea3 v\u1eabn \u1edf \u0111\u00f3, ch\u1edd \u0111\u00fang ch\u1ed7 ch\u1ecb r\u1eddi \u0111i.</p>
<div class="vbox"><span class="vlab">B\u1ea3Y T\u1ea6NG C\u1ee6A CH\u1eca</span>
<p>Ch\u1ecb \u0111\u00e3 th\u1ea5y t\u1ea7ng n\u00e0o m\u1ecfng nh\u1ea5t. Th\u1ee9 c\u00f2n \u0111ang \u0111\u00f3ng l\u00e0 <b>v\u00ec sao n\u00f3 m\u1ecfng</b> \u2014 v\u00e0 ph\u1ea3i l\u00e0m g\u00ec.</p>
<p class="vlist">N\u1ec1n t\u1ea3ng &amp; Ngh\u1ec9 ng\u01a1i &middot; Ni\u1ec1m vui &amp; C\u1ea3m x\u00fac &middot; Ranh gi\u1edbi c\u1ee7a ch\u1ecb &middot; Cho &amp; Nh\u1eadn &middot; Ti\u1ebfng n\u00f3i c\u1ee7a ch\u1ecb &middot; T\u00e2m tr\u00ed b\u1eadn r\u1ed9n &middot; \u00dd ngh\u0129a <span class="vdim">(c\u1ea3 b\u1ea3y \u0111ang kh\u00f3a)</span></p>
<p class="vdim">K\u00e8m b\u1ea3n \u0111\u1ed3 c\u1ee7a ch\u1ecb, \u0111\u1ecdc t\u1eeb b\u1ea7u tr\u1eddi th\u1eadt ng\u00e0y ch\u1ecb sinh \u2014 v\u00e0 nghi th\u1ee9c \u0111\u1ea7u ti\u00ean c\u00f3 th\u1ec3 l\u00e0m ngay t\u1ed1i nay</p></div>
<p>T\u1ea5t c\u1ea3 m\u1edf ra v\u1edbi <b>$4.90 \u2014 tr\u1ea3 m\u1ed9t l\u1ea7n, kh\u00f4ng gia h\u1ea1n</b>.</p>
<p class="vcta">N\u00fat: M\u1edf b\u1ea3n \u0111\u1ecdc \u0111\u1ea7y \u0111\u1ee7 \u2014 $4.90</p>
<p class="vdim">Ba cam k\u1ebft d\u01b0\u1edbi n\u00fat: Tr\u1ea3 m\u1ed9t l\u1ea7n, kh\u00f4ng gia h\u1ea1n &middot; Ho\u00e0n ti\u1ec1n n\u1ebfu tr\u1eadt &middot; Gi\u1eef \u0111\u01b0\u1ee3c \u0111\u1ec3 \u0111\u1ecdc l\u1ea1i</p>"""),

("QUIZ-Q2", "Q2", "+20 gi\u1edd", "H\u00f4m sau",
 "Something to try tonight &#127769;", "Yours to keep, whatever you decide.",
 "M\u1ed9t vi\u1ec7c \u0111\u1ec3 th\u1eed t\u1ed1i nay &#127769;", "C\u1ee7a ch\u1ecb, d\u00f9 ch\u1ecb quy\u1ebft th\u1ebf n\u00e0o.",
 u"""<h4>M\u1ed9t vi\u1ec7c \u0111\u1ec3 th\u1eed t\u1ed1i nay, tr\u01b0\u1edbc khi quy\u1ebft b\u1ea5t c\u1ee9 \u0111i\u1ec1u g\u00ec</h4>
<p>Trong t\u1ea5t c\u1ea3 c\u00e1c c\u00e2u c\u1ee7a b\u00e0i quiz, \u0111\u00e2y l\u00e0 c\u00e2u \u0111\u01b0\u1ee3c g\u1eadt \u0111\u1ea7u nhi\u1ec1u nh\u1ea5t:</p>
<div class="vbox dark"><span class="vbig">64%</span> <span class="vlab">s\u1ed1 ng\u01b0\u1eddi g\u1eadt</span>
<p class="vquote">\u201c\u0110\u1ea7u t\u00f4i c\u1ee9 ch\u1ea1y \u0111i ch\u1ea1y l\u1ea1i nh\u1eefng vi\u1ec7c ch\u01b0a xong, ngay c\u1ea3 khi c\u01a1 th\u1ec3 ch\u1ec9 mu\u1ed1n ngh\u1ec9.\u201d</p></div>
<p>N\u1ebfu \u0111i\u1ec1u \u0111\u00f3 c\u0169ng \u0111\u00fang v\u1edbi ch\u1ecb, \u0111\u00e2y l\u00e0 m\u1ed9t vi\u1ec7c gi\u00fap \u0111\u01b0\u1ee3c cho chuy\u1ec7n \u0111\u00f3 \u2014 <b>c\u1ee7a ch\u1ecb gi\u1eef lu\u00f4n, d\u00f9 ch\u1ecb quy\u1ebft th\u1ebf n\u00e0o v\u1ec1 ph\u1ea7n c\u00f2n l\u1ea1i</b>.</p>
<div class="vbox"><span class="vlab">T\u1ed0I NAY &middot; M\u01af\u1edcI PH\u00daT</span>
<p><b>\u0110\u1eb7t danh s\u00e1ch ra ngo\u00e0i \u0111\u1ea7u m\u00ecnh</b></p>
<p>Tr\u01b0\u1edbc khi \u0111i ng\u1ee7, vi\u1ebft nh\u1eefng vi\u1ec7c ch\u01b0a xong ra m\u1ed9t t\u1edd gi\u1ea5y. Kh\u00f4ng ph\u1ea3i k\u1ebf ho\u1ea1ch, kh\u00f4ng c\u1ea7n th\u1ee9 t\u1ef1 \u2014 ch\u1ec9 l\u00e0 danh s\u00e1ch.</p>
<p>\u0110\u1ec3 t\u1edd gi\u1ea5y tr\u00ean b\u00e0n b\u1ebfp r\u1ed3i \u0111i l\u00ean.</p></div>
<div class="vbox"><p>T\u00e2m tr\u00ed c\u1ee9 di\u1ec5n l\u1ea1i nh\u1eefng g\u00ec n\u00f3 s\u1ee3 m\u1ea5t. Khi danh s\u00e1ch \u0111\u00e3 n\u1eb1m \u1edf m\u1ed9t ch\u1ed7 kh\u00f4ng th\u1ec3 m\u1ea5t, ch\u1ecb b\u1edbt ph\u1ea3i gi\u1eef n\u00f3 su\u1ed1t \u0111\u00eam.</p></div>
<p>\u0110\u00f3 l\u00e0 m\u1ed9t vi\u1ec7c, cho m\u1ed9t trong b\u1ea3y t\u1ea7ng. B\u1ea3n \u0111\u1ecdc \u0111\u1ea7y \u0111\u1ee7 g\u1ecdi t\u00ean t\u1ea7ng m\u1ecfng nh\u1ea5t c\u1ee7a ri\u00eang <i>ch\u1ecb</i> v\u00e0 \u0111\u01b0a <b>l\u1ed9 tr\u00ecnh n\u0103m b\u01b0\u1edbc cho ch\u00ednh t\u1ea7ng \u0111\u00f3</b>, s\u1eafp theo \u0111\u00fang b\u1ea3n \u0111\u1ed3 c\u1ee7a ch\u1ecb \u2014 c\u00f9ng s\u00e1u t\u1ea7ng c\u00f2n l\u1ea1i \u0111\u1ecdc \u0111\u1ea7y \u0111\u1ee7.</p>
<p class="vcta">N\u00fat: Xem l\u1ed9 tr\u00ecnh n\u0103m b\u01b0\u1edbc c\u1ee7a t\u00f4i \u2014 $4.90</p>"""),

("QUIZ-Q3", "Q3", "Ng\u00e0y 3", "+2 ng\u00e0y",
 "Where this actually comes from &#128220;", "Not written from your star sign.",
 "C\u00e1i n\u00e0y th\u1eadt ra l\u1ea5y t\u1eeb \u0111\u00e2u &#128220;", "Kh\u00f4ng ph\u1ea3i vi\u1ebft t\u1eeb cung ho\u00e0ng \u0111\u1ea1o.",
 u"""<h4>C\u00e1i n\u00e0y th\u1eadt ra l\u1ea5y t\u1eeb \u0111\u00e2u</h4>
<p>M\u1ed9t c\u00e2u h\u1ecfi c\u00f4ng b\u1eb1ng, v\u00e0 x\u1ee9ng \u0111\u00e1ng c\u00f3 c\u00e2u tr\u1ea3 l\u1eddi th\u1eb3ng. B\u1ea3n \u0111\u1ecdc c\u1ee7a ch\u1ecb kh\u00f4ng vi\u1ebft t\u1eeb cung ho\u00e0ng \u0111\u1ea1o. <b>N\u00f3 \u0111\u01b0\u1ee3c ch\u1ea5m t\u1eeb ch\u00ednh nh\u1eefng \u00f4 ch\u1ecb t\u1ef1 tick</b> \u2014 hai m\u01b0\u01a1i m\u1ed1t c\u00e2u tr\u1ea3 l\u1eddi, t\u00ednh \u0111i\u1ec3m tr\u00ean b\u1ea3y t\u1ea7ng.</p>
<p>B\u1ea3y t\u1ea7ng \u0111\u00f3 c\u0169ng kh\u00f4ng ph\u1ea3i do ch\u00fang t\u00f4i ngh\u0129 ra. Ch\u00fang \u0111\u1ebfn t\u1eeb nh\u1eefng c\u00f4ng tr\u00ecnh ch\u1ea1y l\u00e2u h\u01a1n tu\u1ed5i \u0111\u1eddi l\u00e0m ngh\u1ec1 c\u1ee7a ph\u1ea7n l\u1edbn ch\u00fang t\u00f4i.</p>
<div class="vbox"><p>C\u00e1c m\u1ed1i quan h\u1ec7 g\u1ea7n g\u0169i d\u1ef1 b\u00e1o s\u1ee9c kho\u1ebb v\u00e0 h\u1ea1nh ph\u00fac t\u1ed1t h\u01a1n b\u1ea5t k\u1ef3 th\u1ee9 g\u00ec kh\u00e1c t\u1eebng \u0111\u01b0\u1ee3c \u0111o.</p><p class="vdim">Nghi\u00ean c\u1ee9u Harvard v\u1ec1 Ph\u00e1t tri\u1ec3n Ng\u01b0\u1eddi tr\u01b0\u1edfng th\u00e0nh &middot; ch\u1ea1y t\u1eeb 1938</p></div>
<div class="vbox"><p>T\u1eeb 40 \u0111\u1ebfn 56 ph\u1ea7n tr\u0103m ph\u1ee5 n\u1eef g\u1eb7p v\u1ea5n \u0111\u1ec1 gi\u1ea5c ng\u1ee7 quanh giai \u0111o\u1ea1n m\u00e3n kinh.</p><p class="vdim">Tr\u01b0\u1eddng Y Harvard &middot; 2024</p></div>
<div class="vbox"><p>N\u0103m m\u1ed1i quan h\u1ec7 g\u1ea7n g\u0169i \u2014 \u0111\u00f3 l\u00e0 con s\u1ed1 c\u00f3 ngh\u0129a.</p><p class="vdim">Robin Dunbar &middot; \u0110\u1ea1i h\u1ecdc Oxford &middot; 2025</p></div>
<p class="vdim"><i>Kh\u00f4ng ai trong s\u1ed1 h\u1ecd \u0111\u01b0\u1ee3c ch\u00fang t\u00f4i tr\u1ea3 ti\u1ec1n, v\u00e0 kh\u00f4ng ai b\u1ea3o tr\u1ee3 ch\u00fang t\u00f4i. Ch\u00fang t\u00f4i tr\u00edch c\u00f4ng tr\u00ecnh \u0111\u00e3 c\u00f4ng b\u1ed1, kh\u00f4ng m\u01b0\u1ee3n t\u00ean.</i></p>
<div class="vbox dark"><span class="vlab">V\u00c0 N\u1ebeU V\u1eaaN KH\u00d4NG TR\u00daNG</span>
<p>N\u1ebfu n\u00f3 \u0111\u1ecdc nh\u01b0 vi\u1ebft v\u1ec1 m\u1ed9t ng\u01b0\u1eddi kh\u00e1c, ch\u1ecb vi\u1ebft cho ch\u00fang t\u00f4i v\u00e0 <b>ch\u00fang t\u00f4i tr\u1ea3 l\u1ea1i $4.90</b>. Kh\u00f4ng c\u1ea7n \u0111i\u1ec1n form, kh\u00f4ng h\u1ecfi l\u00fd do.</p></div>
<p class="vcta">N\u00fat: M\u1edf b\u1ea3n \u0111\u1ecdc \u0111\u1ea7y \u0111\u1ee7 \u2014 $4.90</p>"""),

("QUIZ-Q4", "Q4", "Ng\u00e0y 5", "+2 ng\u00e0y",
 "You are not broken. You are tired. &#129293;", "84 in 100 still trust their own intuition.",
 "Ch\u1ecb kh\u00f4ng h\u1ecfng. Ch\u1ecb \u0111ang m\u1ec7t. &#129293;", "84 tr\u00ean 100 ng\u01b0\u1eddi v\u1eabn tin v\u00e0o tr\u1ef1c gi\u00e1c c\u1ee7a m\u00ecnh.",
 u"""<h4>Ch\u1ecb kh\u00f4ng h\u1ecfng. Ch\u1ecb \u0111ang m\u1ec7t, v\u00e0 kh\u00f4ng \u0111\u01b0\u1ee3c nh\u00ecn th\u1ea5y \u0111\u1ee7 nhi\u1ec1u.</h4>
<p>Ch\u00fang t\u00f4i g\u1ed9p c\u00e1c c\u00e2u tr\u1ea3 l\u1eddi l\u1ea1i, b\u1ecf t\u00ean \u0111i, \u0111\u1ec3 nh\u00ecn xem \u0111i\u1ec1u g\u00ec th\u1eadt s\u1ef1 \u0111\u00fang v\u1edbi nh\u1eefng ng\u01b0\u1eddi ph\u1ee5 n\u1eef l\u00e0m b\u00e0i n\u00e0y. K\u1ebft qu\u1ea3 kh\u00f4ng gi\u1ed1ng \u0111i\u1ec1u ng\u01b0\u1eddi ta v\u1eabn ngh\u0129.</p>
<div class="vbox dark">
<p><span class="vbig">84</span> tr\u00ean 100 ng\u01b0\u1eddi v\u1eabn tin v\u00e0o tr\u1ef1c gi\u00e1c c\u1ee7a m\u00ecnh</p>
<p><span class="vbig">82</span> v\u1eabn cho ph\u00e9p m\u00ecnh h\u01b0\u1edfng m\u1ed9t ni\u1ec1m vui nh\u1ecf</p>
<p><span class="vbig">72</span> v\u1eabn c\u00f3 l\u00fac c\u01b0\u1eddi th\u1eadt, nh\u1eb9 nh\u00f5m</p></div>
<p>Kh\u00f4ng \u0111i\u1ec1u n\u00e0o trong \u0111\u00f3 thu\u1ed9c v\u1ec1 m\u1ed9t ng\u01b0\u1eddi \u0111ang s\u1ee5p \u0111\u1ed5. <b>Ch\u00fang thu\u1ed9c v\u1ec1 m\u1ed9t ng\u01b0\u1eddi \u0111ang g\u00e1nh nhi\u1ec1u h\u01a1n nh\u1eefng g\u00ec ai \u0111\u00f3 \u0111\u1ebfm \u0111\u01b0\u1ee3c.</b></p>
<div class="vbox"><span class="vlab">KHI \u0110\u01af\u1ee2C H\u1eceI MU\u1ed0N L\u1ea4Y L\u1ea0I \u0110I\u1ec0U G\u00cc TRONG B\u1ea2Y NG\u00c0Y T\u1edaI</span>
<p>C\u00e2u \u0111\u01b0\u1ee3c ch\u1ecdn nhi\u1ec1u h\u01a1n m\u1ecdi c\u00e2u kh\u00e1c kh\u00f4ng ph\u1ea3i ngh\u1ec9 ng\u01a1i, c\u0169ng kh\u00f4ng ph\u1ea3i ti\u1ec1n. \u0110\u00f3 l\u00e0 <i>m\u1ed9t d\u1ea5u hi\u1ec7u r\u1eb1ng ch\u01b0\u01a1ng ti\u1ebfp theo v\u1eabn \u0111\u00e1ng \u0111\u1ec3 mong.</i></p>
<p class="vdim">55 tr\u00ean m\u1ed7i 100 ng\u01b0\u1eddi ch\u1ecdn</p></div>
<p>\u0110\u00f3 l\u00e0 \u0111i\u1ec1u ph\u1ea7n c\u00f2n l\u1ea1i c\u1ee7a b\u1ea3n \u0111\u1ecdc h\u01b0\u1edbng t\u1edbi. Kh\u00f4ng ph\u1ea3i m\u1ed9t ch\u1ea9n \u0111o\u00e1n \u2014 m\u00e0 m\u1ed9t h\u01b0\u1edbng \u0111i, b\u1eaft \u0111\u1ea7u t\u1eeb \u0111\u00fang t\u1ea7ng \u0111\u00e3 m\u1ecfng tr\u01b0\u1edbc nh\u1ea5t.</p>
<p class="vcta">N\u00fat: M\u1edf b\u1ea3n \u0111\u1ecdc \u0111\u1ea7y \u0111\u1ee7 \u2014 $4.90</p>"""),

("QUIZ-Q5", "Q5", "Ng\u00e0y 8", "+3 ng\u00e0y",
 "Everything behind the door &#128273;", "One payment. Nothing renews.",
 "M\u1ecdi th\u1ee9 m\u1edf ra c\u00f9ng c\u00e1nh c\u1eeda &#128273;", "Tr\u1ea3 m\u1ed9t l\u1ea7n. Kh\u00f4ng gia h\u1ea1n.",
 u"""<h4>M\u1ecdi th\u1ee9 m\u1edf ra c\u00f9ng c\u00e1nh c\u1eeda</h4>
<p>Ph\u00f2ng khi ch\u01b0a r\u00f5 kho\u1ea3n tr\u1ea3 m\u1ed9t l\u1ea7n \u0111\u00f3 g\u1ed3m nh\u1eefng g\u00ec \u2014 n\u00f3 nhi\u1ec1u h\u01a1n b\u1ea3n \u0111\u1ecdc.</p>
<div class="vbox"><p><b>To\u00e0n b\u1ed9 b\u1ea3y t\u1ea7ng, \u0111\u1ecdc \u0111\u1ea7y \u0111\u1ee7</b></p><p>Theo \u0111\u00fang th\u1ee9 t\u1ef1 n\u00ean ch\u0103m, b\u1eaft \u0111\u1ea7u t\u1eeb t\u1ea7ng m\u1ecfng nh\u1ea5t.</p></div>
<div class="vbox"><p><b>B\u1ea7u tr\u1eddi th\u1eadt ng\u00e0y ch\u1ecb sinh</b></p><p>M\u01b0\u1eddi h\u00e0nh tinh, t\u00ednh t\u1eeb ng\u00e0y v\u00e0 gi\u1edd sinh \u2014 kh\u00f4ng ph\u1ea3i \u0111o\u00e1n.</p></div>
<div class="vbox"><p><b>M\u01b0\u1eddi hai th\u1ebb th\u00e1ng cho 2026 v\u00e0 2027</b></p><p>Nh\u1eefng th\u00e1ng n\u1eb7ng nh\u1ea5t, m\u1ed7i th\u00e1ng k\u00e8m n\u00ean l\u00e0m g\u00ec v\u00e0 n\u00ean tr\u00e1nh g\u00ec.</p></div>
<div class="vbox"><p><b>L\u1ed9 tr\u00ecnh n\u0103m b\u01b0\u1edbc cho t\u1ea7ng m\u1ecfng nh\u1ea5t</b></p><p>S\u1eafp theo \u0111\u00fang b\u1ea3n \u0111\u1ed3 c\u1ee7a ch\u1ecb \u2014 b\u1eaft \u0111\u1ea7u b\u1eb1ng nghi th\u1ee9c ch\u00edn m\u01b0\u01a1i gi\u00e2y c\u00f3 th\u1ec3 l\u00e0m ngay t\u1ed1i nay.</p></div>
<p class="vdim">V\u00e0 k\u00e8m theo: m\u01b0\u1eddi n\u0103m t\u1edbi \u0111\u1ecdc t\u1eebng n\u0103m, c\u00f9ng s\u00e1u \u0111i\u1ec1u ch\u1ecb \u0111ang tr\u1ea3i qua v\u00e0 th\u00e1ng m\u00e0 m\u1ed7i \u0111i\u1ec1u quay l\u1ea1i.</p>
<div class="vbox dark"><span class="vlab">T\u1ea4T C\u1ea2, V\u1edaI</span> <span class="vbig">$4.90</span>
<p><b>Tr\u1ea3 m\u1ed9t l\u1ea7n. Kh\u00f4ng gia h\u1ea1n.</b> Thu\u1ed9c v\u1ec1 ch\u1ecb, gi\u1eef \u0111\u01b0\u1ee3c v\u00e0 \u0111\u1ecdc l\u1ea1i.</p></div>
<p class="vdim">C\u00f3 m\u1ed9t b\u1ea3n \u0111\u1ea7y \u0111\u1ee7 h\u01a1n gi\u00e1 <b>$19</b>, th\u00eam nh\u1ecbp th\u1ef1c h\u00e0nh h\u1eb1ng ng\u00e0y, l\u1ed9 tr\u00ecnh b\u1ea3y ng\u00e0y v\u00e0 b\u1ed1n v\u1eadt ph\u1ea9m ch\u1ecdn theo t\u1ea7ng y\u1ebfu nh\u1ea5t. Ch\u1ecb s\u1ebd th\u1ea5y c\u1ea3 hai khi m\u1edf c\u1eeda \u2014 ch\u01b0a c\u1ea7n quy\u1ebft b\u00e2y gi\u1edd.</p>
<p class="vcta">N\u00fat: M\u1edf t\u1ea5t c\u1ea3 \u2014 $4.90</p>"""),

("QUIZ-Q6", "Q6", "Ngày 11", "+3 ngày",
 "Ninety seconds, and nothing to buy &#129293;", "The last one from us. It is a gift, not an offer.",
 "Chín mươi giây, và không bán gì cả &#129293;", "Lá cuối. Là quà, không phải lời chào mời.",
 u"""<h4>Chín mươi giây, và không bán gì cả</h4>
<p>Đây là lá cuối chúng tôi gửi về bản đọc của chị. <b>Trong thư này không có gì để mua</b> — không nút bấm, không lời chào, không có gì ở cuối trang.</p>
<p>Chị đã trả lời hai mươi mốt câu hỏi thật lòng mà chúng tôi chưa từng đưa lại cho chị thứ gì. Vậy nên đây là nghi thức đầu tiên trong lộ trình, viết ra đầy đủ. Nó là của chị, dù chị có bao giờ mở phần còn lại hay không.</p>
<div class="vbox dark"><span class="vlab">TỐI NAY, TRƯỚC KHI ĐI NGỦ</span>
<p><b>Chín mươi giây, chia ba phần</b></p>
<p><span style="color:#C6A15B">0:30</span> &nbsp;<b>Cầm một vật có trọng lượng</b><br>Một viên đá, chùm chìa khoá, hay cốc trà còn ấm. Đặt nó vào lòng bàn tay đang mở và để tay cảm nhận nó nặng bao nhiêu. Không làm gì khác.</p>
<p><span style="color:#C6A15B">0:30</span> &nbsp;<b>Thở ra dài hơn lúc hít vào</b><br>Vào đếm bốn, ra đếm sáu. Bốn lần. Nếu lạc mất nhịp thì bắt đầu lại — lạc nhịp không phải là thất bại.</p>
<p><span style="color:#C6A15B">0:30</span> &nbsp;<b>Nói thành tiếng một việc đã xong</b><br>Một việc chị làm xong hôm nay, nhỏ thế nào cũng được. Nói thành lời, trong phòng, không nghĩ thầm. Chính việc nói ra mới là phần có tác dụng.</p></div>
<p>Phần thứ ba là phần người ta hay bỏ qua, và cũng là phần quan trọng nhất. Một cái đầu đã đếm những việc chưa xong suốt cả ngày cần được nghe, bằng chính giọng của chị, rằng có một việc đã xong.</p>
<div class="vbox"><p>Cảm ơn chị vì hai mươi mốt câu trả lời. Phần lớn mọi người sẽ không ngồi với những câu hỏi như thế trong bảy phút, còn chị thì có. <b>Mong chín mươi giây này có ích, và chúng tôi xin phép không làm phiền chị nữa.</b></p></div>
<p class="vdim">Không có nút bấm nào trong mail này — đó là chủ ý. Chân mail chỉ còn địa chỉ và link huỷ đăng ký theo luật.</p>"""),
]

CSS = u"""<style>
:root{--bg:#150C2E;--bg2:#1E1440;--gold:#C6A15B;--pale:#EDE9F5;--mute:#9C93B5;--line:#2E2350}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--pale);
 font-family:"Be Vietnam Pro",-apple-system,"Segoe UI",sans-serif;font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
.wrap{max-width:760px;margin:0 auto;padding:0 18px 80px}
h1{margin:0;font-size:clamp(1.7rem,5vw,2.4rem);font-weight:700;letter-spacing:-.02em;line-height:1.1;color:#fff}
.top{padding:52px 0 30px}
.kick{font-family:"IBM Plex Mono",monospace;font-size:.64rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold)}
.lede{color:var(--mute);font-size:1.02rem;max-width:58ch;margin-top:12px}
.lede b{color:#fff}
.rail{height:2px;width:44px;background:var(--gold);border-radius:2px;margin:18px 0 0}
.nav{display:flex;flex-wrap:wrap;gap:7px;margin-top:26px;padding-top:22px;border-top:1px solid var(--line)}
.nav a{font-family:"IBM Plex Mono",monospace;font-size:.72rem;letter-spacing:.06em;color:var(--pale);
 text-decoration:none;background:var(--bg2);border:1px solid var(--line);border-radius:99px;padding:7px 14px}
.nav a:hover{border-color:var(--gold);color:var(--gold)}
.mail{margin-top:42px;scroll-margin-top:16px}
.inbox{background:var(--bg2);border:1px solid var(--line);border-radius:12px 12px 0 0;padding:15px 18px;
 display:grid;grid-template-columns:78px 1fr;gap:14px;align-items:start}
.when{text-align:center}
.when .id{font-family:"IBM Plex Mono",monospace;font-size:.68rem;color:var(--gold);letter-spacing:.1em}
.when .d{font-family:"IBM Plex Mono",monospace;font-size:.86rem;color:#fff;font-weight:500;margin-top:3px}
.when .r{font-size:.62rem;color:var(--mute);margin-top:2px;line-height:1.3}
.meta .from{font-size:.72rem;color:var(--mute);font-family:"IBM Plex Mono",monospace;letter-spacing:.04em}
.meta .s{font-size:1.04rem;font-weight:600;color:#fff;line-height:1.35;margin-top:4px}
.meta .p{font-size:.86rem;color:var(--mute);line-height:1.45;margin-top:3px}
.frame{border:1px solid var(--line);border-top:none;overflow:hidden}
.frame > table{width:100% !important}
/* ---- ban dich ---- */
.vi{background:var(--bg2);border:1px solid var(--line);border-top:none;border-radius:0 0 12px 12px;padding:22px 24px 26px}
.vi-h{display:flex;flex-wrap:wrap;gap:10px;align-items:baseline;padding-bottom:14px;margin-bottom:16px;border-bottom:1px dashed var(--line)}
.vi-h .tag{font-family:"IBM Plex Mono",monospace;font-size:.58rem;letter-spacing:.14em;text-transform:uppercase;
 background:rgba(198,161,91,.15);color:var(--gold);padding:4px 9px;border-radius:4px}
.vi-h .note{font-size:.78rem;color:var(--mute)}
.vi-sub{font-size:.85rem;color:var(--mute);margin-bottom:16px;line-height:1.5}
.vi-sub b{color:#fff;font-weight:500}
.vi h4{margin:0 0 12px;font-size:1.12rem;font-weight:600;color:#fff;line-height:1.35}
.vi p{margin:0 0 11px;font-size:.94rem;line-height:1.68;color:#CFC8DF}
.vi p:last-child{margin-bottom:0}
.vi b{color:#fff;font-weight:600}
.vi i{color:#DED7EC}
.vbox{background:rgba(255,255,255,.045);border-left:3px solid var(--gold);border-radius:0 8px 8px 0;
 padding:14px 16px;margin:0 0 11px}
.vbox.dark{background:rgba(0,0,0,.25)}
.vlab{display:inline-block;font-family:"IBM Plex Mono",monospace;font-size:.6rem;letter-spacing:.13em;
 text-transform:uppercase;color:var(--gold);margin-bottom:8px}
.vbig{font-size:1.7rem;font-weight:700;color:var(--gold);line-height:1.1;margin-right:6px}
.vquote{font-style:italic;color:#EDE9F5 !important}
.vlist{color:#DED7EC !important}
.vdim{color:var(--mute) !important;font-size:.85rem !important}
.vcta{font-family:"IBM Plex Mono",monospace;font-size:.82rem !important;color:var(--gold) !important;
 background:rgba(198,161,91,.1);border-radius:6px;padding:9px 13px;display:inline-block}
footer{margin-top:56px;padding-top:20px;border-top:1px solid var(--line);font-size:.8rem;color:var(--mute)}
footer code{font-family:"IBM Plex Mono",monospace;font-size:.92em;color:#CFC8DF}
@media (max-width:560px){.inbox{grid-template-columns:1fr;gap:9px}.when{text-align:left;display:flex;gap:9px;align-items:baseline}.vi{padding:18px 16px 22px}}
</style>"""

def build():
    logo = logo_data_uri()
    p = [u'<title>S\u00e1u Mail Quiz \u2192 $4.90</title>',
         u'<link rel="preconnect" href="https://fonts.googleapis.com">',
         u'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
         u'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">',
         CSS, u'<div class="wrap">', u'<div class="top">',
         u'<div class="kick">Mine Spirit \u00b7 Klaviyo \u00b7 B\u1ea3n xem th\u1eed</div>',
         u'<h1>S\u00e1u mail Quiz \u2192 $4.90</h1>', u'<div class="rail"></div>',
         u'<p class="lede">G\u1eedi cho ng\u01b0\u1eddi <b>\u0111\u00e3 l\u00e0m h\u1ebft quiz, \u0111\u00e3 \u0111\u1ec3 l\u1ea1i email, ch\u01b0a m\u1edf kh\u00f3a b\u1ea3n \u0111\u1ecdc</b>. M\u1ed7i mail hi\u1ec7n \u0111\u00fang nh\u01b0 kh\u00e1ch s\u1ebd th\u1ea5y, <b>k\u00e8m b\u1ea3n d\u1ecbch ti\u1ebfng Vi\u1ec7t ngay b\u00ean d\u01b0\u1edbi</b>.</p>',
         u'<nav class="nav">']
    for m in MAILS:
        p.append(u'<a href="#%s">%s \u00b7 %s</a>' % (m[1], m[1], m[2]))
    p.append(u'</nav></div>')

    for f, mid, day, rel, subj, pre, vsubj, vpre, vbody in MAILS:
        html = io.open(os.path.join(TPL, f + ".html"), encoding="utf-8").read()
        html = html.replace("{% unsubscribe_link %}", "#").replace(LOGO_URL, logo)
        p.append(u'<div class="mail" id="%s">' % mid)
        p.append(u'<div class="inbox"><div class="when"><div class="id">%s</div><div class="d">%s</div><div class="r">%s</div></div>'
                 % (mid, day, rel))
        p.append(u'<div class="meta"><div class="from">Mine Spirit &lt;support@minespirit.com&gt;</div>'
                 u'<div class="s">%s</div><div class="p">%s</div></div></div>' % (subj, pre))
        p.append(u'<div class="frame">%s</div>' % html)
        p.append(u'<div class="vi"><div class="vi-h"><span class="tag">B\u1ea3n d\u1ecbch ti\u1ebfng Vi\u1ec7t</span>'
                 u'<span class="note">\u0110\u1ec3 ch\u1ecb \u0111\u1ecdc hi\u1ec3u \u2014 mail g\u1eedi \u0111i v\u1eabn l\u00e0 b\u1ea3n ti\u1ebfng Anh \u1edf tr\u00ean</span></div>')
        p.append(u'<div class="vi-sub"><b>Ti\u00eau \u0111\u1ec1:</b> %s<br><b>D\u00f2ng xem tr\u01b0\u1edbc:</b> %s</div>' % (vsubj, vpre))
        p.append(vbody)
        p.append(u'</div></div>')

    p.append(u'<footer>S\u00e1u file g\u1ed1c: <code>klaviyo-templates/QUIZ-Q1..Q6.html</code> &middot; '
             u'B\u1ea3n xem th\u1eed c\u1eadp nh\u1eadt 10/09/2026 &middot; '
             u'Link h\u1ee7y \u0111\u0103ng k\u00fd \u0111\u00e3 thay b\u1eb1ng d\u1ea5u # v\u00e0 logo nh\u00fang th\u1eb3ng v\u00e0o trang \u0111\u1ec3 xem th\u1eed; '
             u'file template g\u1ed1c gi\u1eef nguy\u00ean.</footer></div>')

    out = u"".join(p)
    io.open(OUT, "w", encoding="utf-8").write(out)
    return out

if __name__ == "__main__":
    o = build()
    print("da ghi", OUT)
    print("KB:", round(len(o) / 1024))
    print("so mail:", o.count('class="mail"'))
    print("so ban dich:", o.count('class="vi"'))
    print("con the klaviyo:", "{%" in o)
    print("con link anh ngoai:", "raw.githubusercontent" in o)
