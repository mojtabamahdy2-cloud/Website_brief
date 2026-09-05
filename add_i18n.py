import re

with open('wedding-visual-brief.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add T function and state.lang
html = html.replace('var state={', 'function T(ar, en) { return state.lang === "ar" ? ar : en; }\nvar state={\n  lang:"ar",')

# 2. Update toggle button and HTML dir
html = html.replace('<html lang="ar" dir="rtl">', '<html lang="ar" dir="rtl" id="htmlDoc">')
header_replacement = """<header class="site-header">
  <div class="logo" id="logoText">العميل <span>الاسم</span> &mdash; موجز الموقع</div>
  <div style="display:flex;gap:16px;align-items:center;">
    <button id="langToggle" style="background:none;border:1px solid var(--border);border-radius:6px;padding:4px 8px;font-size:12px;color:var(--text);cursor:pointer;font-family:var(--mono);">EN</button>
    <div class="step-pills" id="stepPills"></div>
  </div>
</header>"""
html = re.sub(r'<header class="site-header">.*?</header>', header_replacement, html, flags=re.DOTALL)

# Add event listener for langToggle in INIT section
init_replacement = """
  document.getElementById('langToggle').onclick = function() {
    state.lang = state.lang === 'ar' ? 'en' : 'ar';
    document.getElementById('htmlDoc').dir = state.lang === 'ar' ? 'rtl' : 'ltr';
    document.getElementById('htmlDoc').lang = state.lang;
    this.innerText = state.lang === 'ar' ? 'EN' : 'عربي';
    document.getElementById('logoText').innerHTML = state.lang === 'ar' 
        ? 'العميل <span>الاسم</span> &mdash; موجز الموقع' 
        : 'Client <span>Name</span> &mdash; Website Brief';
    go(); // re-render the current step
  };
  if(state.lang === 'en') {
    document.getElementById('htmlDoc').dir = 'ltr';
    document.getElementById('htmlDoc').lang = 'en';
    document.getElementById('langToggle').innerText = 'عربي';
    document.getElementById('logoText').innerHTML = 'Client <span>Name</span> &mdash; Website Brief';
  }
load();go();
"""
html = html.replace('load();go();', init_replacement)

# 3. Replace strings in JS
replacements = [
    # Nav
    ("'<span></span>':'<button class=\"btn btn-ghost\" id=\"bBack\">رجوع / Back</button>'", 
     "'<span></span>':'<button class=\"btn btn-ghost\" id=\"bBack\">'+T('رجوع','Back')+'</button>'"),
    ("'<button class=\"btn btn-primary\" id=\"bNext\">إرسال / Submit</button>':'<button class=\"btn btn-primary\" id=\"bNext\">متابعة / Continue</button>'", 
     "'<button class=\"btn btn-primary\" id=\"bNext\">'+T('إرسال','Submit')+'</button>':'<button class=\"btn btn-primary\" id=\"bNext\">'+T('متابعة','Continue')+'</button>'"),
    
    # Step 0
    ("'<p class=\"step-eyebrow\" style=\"text-align:center;\" dir=\"auto\">مرحباً بك في / Welcome to your</p>'", "'<p class=\"step-eyebrow\" style=\"text-align:center;\" dir=\"auto\">'+T('مرحباً بك في','Welcome to your')+'</p>'"),
    ("'<h1 class=\"step-title\" style=\"text-align:center;font-size:42px;\" dir=\"auto\">موجز التصميم المرئي<br><span style=\"font-size:32px\">Visual Onboarding Brief</span></h1>'", "'<h1 class=\"step-title\" style=\"text-align:center;font-size:42px;\" dir=\"auto\">'+T('موجز التصميم المرئي','Visual Onboarding Brief')+'</h1>'"),
    ("'<p class=\"step-desc\" style=\"text-align:center;max-width:50ch;margin:0 auto 0;\" dir=\"auto\">مرحباً! يساعدنا هذا النموذج القصير على فهم ذوقك وأسلوبك وأهدافك لنتمكن من بناء موقع يعبر عنك حقاً.<br><br>Hello! This short visual form helps us understand your taste, style, and goals so we can build a website that truly feels like <em>you</em>.</p>'", "'<p class=\"step-desc\" style=\"text-align:center;max-width:50ch;margin:0 auto 0;\" dir=\"auto\">'+T('مرحباً! يساعدنا هذا النموذج القصير على فهم ذوقك وأسلوبك وأهدافك لنتمكن من بناء موقع يعبر عنك حقاً.','Hello! This short visual form helps us understand your taste, style, and goals so we can build a website that truly feels like <em>you</em>.')+'</p>'"),
    
    # Step 1
    ("'<div class=\"step-badge\">الخطوة 2 من 6 / Step 2 of 6</div>'", "'<div class=\"step-badge\">'+T('الخطوة 2 من 6','Step 2 of 6')+'</div>'"),
    ("'<p class=\"step-eyebrow\" dir=\"auto\">لوحة الألوان / Colour Palette</p>'", "'<p class=\"step-eyebrow\" dir=\"auto\">'+T('لوحة الألوان','Colour Palette')+'</p>'"),
    ("'<h1 class=\"step-title\" dir=\"auto\">ما هي الألوان التي تعبر عنك؟<br><span style=\"font-size:28px\">What colours feel like <em>you</em>?</span></h1>'", "'<h1 class=\"step-title\" dir=\"auto\">'+T('ما هي الألوان التي تعبر عنك؟','What colours feel like <em>you</em>?')+'</h1>'"),
    ("'<p class=\"step-desc\" dir=\"auto\">اضغط على أي لون أدناه لفتح عجلة الألوان. يمكنك أيضاً كتابة كود اللون مباشرة أو اختيار مجموعة جاهزة.<br>Click any colour swatch below to open the colour wheel picker. You can also type a hex code directly or choose a quick preset.</p>'", "'<p class=\"step-desc\" dir=\"auto\">'+T('اضغط على أي لون أدناه لفتح عجلة الألوان. يمكنك أيضاً كتابة كود اللون مباشرة أو اختيار مجموعة جاهزة.','Click any colour swatch below to open the colour wheel picker. You can also type a hex code directly or choose a quick preset.')+'</p>'"),
    ("'<span class=\"section-label\" dir=\"auto\">مجموعات جاهزة / Quick mood presets</span>'", "'<span class=\"section-label\" dir=\"auto\">'+T('مجموعات جاهزة','Quick mood presets')+'</span>'"),
    ("'<span class=\"section-label\" dir=\"auto\">لوحات الألوان المحفوظة / Saved palette combinations</span>'", "'<span class=\"section-label\" dir=\"auto\">'+T('لوحات الألوان المحفوظة','Saved palette combinations')+'</span>'"),
    ("'<span style=\"font-size:12px;color:var(--text3);\" dir=\"auto\">لم يتم حفظ شيء بعد / None saved yet</span>'", "'<span style=\"font-size:12px;color:var(--text3);\" dir=\"auto\">'+T('لم يتم حفظ شيء بعد','None saved yet')+'</span>'"),
    ("حفظ اللوحة الحالية / Save current palette</button>'", "'+T('حفظ اللوحة الحالية','Save current palette')+'</button>'"),
    ("placeholder=\"الهدف (اختياري) / Purpose (optional)\"", "placeholder=\"'+T('الهدف (اختياري)','Purpose (optional)')+'\""),
    
    # Step 2
    ("'<div class=\"step-badge\">الخطوة 3 من 6 / Step 3 of 6</div>'", "'<div class=\"step-badge\">'+T('الخطوة 3 من 6','Step 3 of 6')+'</div>'"),
    ("'<p class=\"step-eyebrow\" dir=\"auto\">الخطوط / Typography</p>'", "'<p class=\"step-eyebrow\" dir=\"auto\">'+T('الخطوط','Typography')+'</p>'"),
    ("'<h1 class=\"step-title\" dir=\"auto\">اختر خطوطك<br><span style=\"font-size:28px\">Choose your fonts</span></h1>'", "'<h1 class=\"step-title\" dir=\"auto\">'+T('اختر خطوطك','Choose your fonts')+'</h1>'"),
    ("'<p class=\"step-desc\" dir=\"auto\">اختر خطاً إنجليزياً واحداً وخطاً عربياً واحداً. يتم تحديث المعاينة المباشرة مع كل اختيار.<br>Select one English font and one Arabic font. Each live preview updates as you choose.</p>'", "'<p class=\"step-desc\" dir=\"auto\">'+T('اختر خطاً إنجليزياً واحداً وخطاً عربياً واحداً. يتم تحديث المعاينة المباشرة مع كل اختيار.','Select one English font and one Arabic font. Each live preview updates as you choose.')+'</p>'"),
    ("'<span class=\"section-label\" dir=\"auto\">المعاينة بالإنجليزية / English preview</span>'", "'<span class=\"section-label\" dir=\"auto\">'+T('المعاينة بالإنجليزية','English preview')+'</span>'"),
    ("'<span class=\"section-label\" dir=\"auto\">الخطوط الإنجليزية / English fonts</span>'", "'<span class=\"section-label\" dir=\"auto\">'+T('الخطوط الإنجليزية','English fonts')+'</span>'"),
    ("'<span class=\"section-label\" dir=\"auto\">المعاينة بالعربية / Arabic preview</span>'", "'<span class=\"section-label\" dir=\"auto\">'+T('المعاينة بالعربية','Arabic preview')+'</span>'"),
    ("'<span class=\"section-label\" dir=\"auto\">الخطوط العربية / Arabic fonts</span>'", "'<span class=\"section-label\" dir=\"auto\">'+T('الخطوط العربية','Arabic fonts')+'</span>'"),
    
    # Step 3
    ("'<div class=\"step-badge\">الخطوة 4 من 6 / Step 4 of 6</div>'", "'<div class=\"step-badge\">'+T('الخطوة 4 من 6','Step 4 of 6')+'</div>'"),
    ("'<p class=\"step-eyebrow\" dir=\"auto\">الأسلوب والمزاج / Style & Mood</p>'", "'<p class=\"step-eyebrow\" dir=\"auto\">'+T('الأسلوب والمزاج','Style & Mood')+'</p>'"),
    ("'<h1 class=\"step-title\" dir=\"auto\">ما هو الطابع العام؟<br><span style=\"font-size:28px\">What\\'s the vibe?</span></h1>'", "'<h1 class=\"step-title\" dir=\"auto\">'+T('ما هو الطابع العام؟','What\\'s the vibe?')+'</h1>'"),
    ("'<p class=\"step-desc\" dir=\"auto\">اختر جميع الأساليب التي تناسبك — يمكنك اختيار أكثر من واحد.<br>Select all styles that resonate — you can pick more than one.</p>'", "'<p class=\"step-desc\" dir=\"auto\">'+T('اختر جميع الأساليب التي تناسبك — يمكنك اختيار أكثر من واحد.','Select all styles that resonate — you can pick more than one.')+'</p>'"),
    ("'<span class=\"section-label\" dir=\"auto\">الرسمية مقابل الشخصية / Formality vs personality</span>'", "'<span class=\"section-label\" dir=\"auto\">'+T('الرسمية مقابل الشخصية','Formality vs personality')+'</span>'"),
    ("'<span dir=\"auto\">عفوي وودي<br>Casual &amp; Friendly</span><span dir=\"auto\" style=\"text-align:left;\">فاخر ورسمي<br>Luxurious &amp; Formal</span>'", "'<span dir=\"auto\">'+T('عفوي وودي','Casual &amp; Friendly')+'</span><span dir=\"auto\" style=\"text-align:'+(state.lang==='ar'?'left':'right')+';\">'+T('فاخر ورسمي','Luxurious &amp; Formal')+'</span>'"),
    ("'<label class=\"field-label\" dir=\"auto\">مواقع أو علامات تجارية تلهمك / Websites or brands that inspire you <span class=\"field-optional\">اختياري / optional</span></label>'", "'<label class=\"field-label\" dir=\"auto\">'+T('مواقع أو علامات تجارية تلهمك','Websites or brands that inspire you')+' <span class=\"field-optional\">'+T('اختياري','optional')+'</span></label>'"),
    
    # Step 4
    ("'<div class=\"step-badge\">الخطوة 5 من 6 / Step 5 of 6</div>'", "'<div class=\"step-badge\">'+T('الخطوة 5 من 6','Step 5 of 6')+'</div>'"),
    ("'<p class=\"step-eyebrow\" dir=\"auto\">معرض الإلهام / Inspiration Gallery</p>'", "'<p class=\"step-eyebrow\" dir=\"auto\">'+T('معرض الإلهام','Inspiration Gallery')+'</p>'"),
    ("'<h1 class=\"step-title\" dir=\"auto\">أخبرنا بما يعجبك<br><span style=\"font-size:28px\">Tell us what you love</span></h1>'", "'<h1 class=\"step-title\" dir=\"auto\">'+T('أخبرنا بما يعجبك','Tell us what you love')+'</h1>'"),
    ("'<p class=\"gallery-desc\" dir=\"auto\">ثمانية أمثلة لتصاميم مواقع. قيم كل منها وأضف تعليقاً اختيارياً.<br>Eight example website aesthetics. Label each one and add an optional comment.</p>'", "'<p class=\"gallery-desc\" dir=\"auto\">'+T('ثمانية أمثلة لتصاميم مواقع. قيم كل منها وأضف تعليقاً اختيارياً.','Eight example website aesthetics. Label each one and add an optional comment.')+'</p>'"),
    ("['love','أعجبني<br>Love']", "[ 'love', T('أعجبني','Love') ]"),
    ("['inspire','مُلهم<br>Inspire']", "[ 'inspire', T('مُلهم','Inspire') ]"),
    ("['meh','عادي<br>Meh']", "[ 'meh', T('عادي','Meh') ]"),
    ("['avoid','تجنب<br>Avoid']", "[ 'avoid', T('تجنب','Avoid') ]"),
    ("placeholder=\"تعليق اختياري / Optional comment\"", "placeholder=\"'+T('تعليق اختياري','Optional comment')+'\""),
    
    # Step 5
    ("'<div class=\"step-badge\">الخطوة 6 من 6 / Step 6 of 6</div>'", "'<div class=\"step-badge\">'+T('الخطوة 6 من 6','Step 6 of 6')+'</div>'"),
    ("'<p class=\"step-eyebrow\" dir=\"auto\">أفكار أخيرة / Final thoughts</p>'", "'<p class=\"step-eyebrow\" dir=\"auto\">'+T('أفكار أخيرة','Final thoughts')+'</p>'"),
    ("'<h1 class=\"step-title\" dir=\"auto\">أفكار أخيرة<br><span style=\"font-size:28px\">Final thoughts</span></h1>'", "'<h1 class=\"step-title\" dir=\"auto\">'+T('أفكار أخيرة','Final thoughts')+'</h1>'"),
    ("placeholder=\"هل هناك أي شيء آخر تود أن نعرفه؟ المساحة لك. / Anything else you\\'d like us to know?\"", "placeholder=\"'+T('هل هناك أي شيء آخر تود أن نعرفه؟ المساحة لك.','Anything else you\\'d like us to know?')+'\""),
    
    # Thank you
    ("'<h1 class=\"ty-title\">شكراً لك! / Thank you!</h1>'", "'<h1 class=\"ty-title\">'+T('شكراً لك!','Thank you!')+'</h1>'"),
    ("'<p class=\"ty-subtitle\">تم إرسال موجز التصميم المرئي الخاص بك. سنقوم بمراجعة كل التفاصيل ونبدأ العمل قريباً.<br><br>Your visual brief has been submitted. We\\'ll review every detail and get started very soon.</p>'", "'<p class=\"ty-subtitle\">'+T('تم إرسال موجز التصميم المرئي الخاص بك. سنقوم بمراجعة كل التفاصيل ونبدأ العمل قريباً.','Your visual brief has been submitted. We\\'ll review every detail and get started very soon.')+'</p>'")
]

for old, new in replacements:
    html = html.replace(old, new)

# Special handling for STYLES array
styles_replacement = """var STYLES=[
  {id:'elegant',label:T('أنيق','Elegant'),desc:T('راقي، فاخر','Refined, upscale, editorial'),vis:'sc-vis-elegant',icon:'✦ ✦ ✦'},
  {id:'bold',label:T('جريء','Bold'),desc:T('قوي، تباين عالي','Strong, high contrast'),vis:'sc-vis-bold',icon:'◼ ◼ ◼'},
  {id:'soft',label:T('ناعم ودافئ','Soft & Warm'),desc:T('ألوان دافئة، أشكال عضوية','Warm tones, organic shapes'),vis:'sc-vis-soft',icon:'◌ ◌ ◌'},
  {id:'minimal',label:T('بسيط','Minimal'),desc:T('مساحات بيضاء، خطوط نظيفة','White space, clean lines'),vis:'sc-vis-minimal',icon:'— — —'},
  {id:'playful',label:T('مرح','Playful'),desc:T('ملون، معبر','Colourful, expressive'),vis:'sc-vis-playful',icon:'★ ★ ★'},
  {id:'corporate',label:T('تقليدي','Traditional'),desc:T('كلاسيكي، منظم','Professional, structured'),vis:'sc-vis-corporate',icon:'▪ ▪ ▪'},
  {id:'earthy',label:T('طبيعي','Earthy'),desc:T('طبيعي، أصيل','Natural, grounded, artisan'),vis:'sc-vis-earthy',icon:'◉ ◉ ◉'},
  {id:'luxe',label:T('فاخر','Luxurious'),desc:T('لمسات ذهبية، خلفية داكنة','Gold accents, dark canvas'),vis:'sc-vis-luxe',icon:'◈ ◈ ◈'}
];"""
html = re.sub(r'var STYLES=\[.*?\];', styles_replacement, html, flags=re.DOTALL)

with open('wedding-visual-brief.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done")
