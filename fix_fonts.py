import re

with open('wedding-visual-brief.html', 'r', encoding='utf-8') as f:
    html = f.read()

en_fonts_replacement = """function getEnFonts() { return [
  {id:'cormorant',name:'Cormorant Garamond',tag:T('أنيق / Serif','Elegant / Serif'),desc:T('إحساس كلاسيكي راقي. ممتاز للعلامات الشخصية الفاخرة.','Timeless editorial feel. Great for high-end personal brands.'),sample:'Aa Bb Cc'},
  {id:'playfair',name:'Playfair Display',tag:T('كلاسيكي / Serif','Classic / Serif'),desc:T('قوي وموثوق. مثالي للمدربين والمتحدثين.','Strong, authoritative. Perfect for coaches and speakers.'),sample:'Aa Bb Cc'},
  {id:'dm-sans',name:'DM Sans',tag:T('عصري / Sans','Modern / Sans'),desc:T('نظيف وودود. يناسب أي موقع مهني.','Clean and approachable. Works for any professional site.'),sample:'Aa Bb Cc'},
  {id:'montserrat',name:'Montserrat',tag:T('جريء / Sans','Bold / Sans'),desc:T('واثق وأنيق. ممتاز للعناوين.','Confident and stylish. Excellent for headings.'),sample:'Aa Bb Cc'},
  {id:'lato',name:'Lato',tag:T('ودود / Sans','Friendly / Sans'),desc:T('دافئ ومقروء. مثالي للمواقع الغنية بالمحتوى.','Warm and readable. Ideal for content-heavy sites.'),sample:'Aa Bb Cc'}
]; }"""
ar_fonts_replacement = """function getArFonts() { return [
  {id:'cairo',name:'Cairo',tag:T('عصري / Arabic','Modern / Arabic'),desc:T('نظيف ومتعدد الاستخدامات — الخط العربي الأكثر توافقاً مع الويب.','Clean and versatile — the most web-friendly Arabic font.'),sample:'أ ب ج — مرحباً'},
  {id:'tajawal',name:'Tajawal',tag:T('خفيف / Arabic','Light / Arabic'),desc:T('أنيق وخفيف، رائع للمواقع ثنائية اللغة.','Elegant and airy, great for bilingual sites.'),sample:'أ ب ج — مرحباً'},
  {id:'almarai',name:'Almarai',tag:T('دائري / Arabic','Rounded / Arabic'),desc:T('جريء وودود، طابع عصري للعلامات التجارية.','Bold and friendly, modern brand feel.'),sample:'أ ب ج — مرحباً'},
  {id:'noto-kufi',name:'Noto Kufi Arabic',tag:T('كلاسيكي / Arabic','Classic / Arabic'),desc:T('خط كوفي تقليدي بوضوح عالي.','Traditional Kufi style with great legibility.'),sample:'أ ب ج — مرحباً'}
]; }"""

html = re.sub(r'var EN_FONTS=\[.*?\];', en_fonts_replacement, html, flags=re.DOTALL)
html = re.sub(r'var AR_FONTS=\[.*?\];', ar_fonts_replacement, html, flags=re.DOTALL)
html = html.replace('EN_FONTS.forEach', 'getEnFonts().forEach')
html = html.replace('AR_FONTS.forEach', 'getArFonts().forEach')

with open('wedding-visual-brief.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fonts fixed")
