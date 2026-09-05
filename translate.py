import re
import os

file_path = 'wedding-visual-brief.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# HTML Dir
content = content.replace('<html lang="en" dir="ltr">', '<html lang="ar" dir="rtl">')
content = content.replace('<title>Visual Onboarding Brief</title>', '<title>موجز التصميم المرئي | Visual Onboarding Brief</title>')

# Header Logo
content = content.replace('<div class="logo">Client <span>Name</span> &mdash; Website Brief</div>', '<div class="logo">العميل <span>الاسم</span> &mdash; موجز الموقع / Website Brief</div>')

# Nav buttons
content = content.replace('\'<button class="btn btn-ghost" id="bBack">Back</button>\'', '\'<button class="btn btn-ghost" id="bBack">رجوع / Back</button>\'')
content = content.replace('\'<button class="btn btn-primary" id="bNext">Submit Brief</button>\'', '\'<button class="btn btn-primary" id="bNext">إرسال / Submit</button>\'')
content = content.replace('\'<button class="btn btn-primary" id="bNext">Continue</button>\'', '\'<button class="btn btn-primary" id="bNext">متابعة / Continue</button>\'')

# Step 0
content = content.replace('<p class="step-eyebrow" style="text-align:center;">Welcome to your</p>', '<p class="step-eyebrow" style="text-align:center;" dir="auto">مرحباً بك في / Welcome to your</p>')
content = content.replace('<h1 class="step-title" style="text-align:center;font-size:42px;">Visual Onboarding Brief</h1>', '<h1 class="step-title" style="text-align:center;font-size:42px;" dir="auto">موجز التصميم المرئي<br><span style="font-size:32px">Visual Onboarding Brief</span></h1>')
content = content.replace('<p class="step-desc" style="text-align:center;max-width:50ch;margin:0 auto 0;">Hello! This short visual form helps us understand your taste, style, and goals so we can build a website that truly feels like <em>you</em>.</p>', '<p class="step-desc" style="text-align:center;max-width:50ch;margin:0 auto 0;" dir="auto">مرحباً! يساعدنا هذا النموذج القصير على فهم ذوقك وأسلوبك وأهدافك لنتمكن من بناء موقع يعبر عنك حقاً.<br><br>Hello! This short visual form helps us understand your taste, style, and goals so we can build a website that truly feels like <em>you</em>.</p>')

# Step 1
content = content.replace('<div class="step-badge">Step 2 of 6</div>', '<div class="step-badge">الخطوة 2 من 6 / Step 2 of 6</div>')
content = content.replace('<p class="step-eyebrow">Colour Palette</p>', '<p class="step-eyebrow" dir="auto">لوحة الألوان / Colour Palette</p>')
content = content.replace('<h1 class="step-title">What colours feel like <em>you</em>?</h1>', '<h1 class="step-title" dir="auto">ما هي الألوان التي تعبر عنك؟<br><span style="font-size:28px">What colours feel like <em>you</em>?</span></h1>')
content = content.replace('<p class="step-desc">Click any colour swatch below to open the colour wheel picker. You can also type a hex code directly or choose a quick preset.</p>', '<p class="step-desc" dir="auto">اضغط على أي لون أدناه لفتح عجلة الألوان. يمكنك أيضاً كتابة كود اللون مباشرة أو اختيار مجموعة جاهزة.<br>Click any colour swatch below to open the colour wheel picker. You can also type a hex code directly or choose a quick preset.</p>')
content = content.replace('<span class="section-label">Quick mood presets</span>', '<span class="section-label" dir="auto">مجموعات جاهزة / Quick mood presets</span>')
content = content.replace('<span class="section-label">Saved palette combinations</span>', '<span class="section-label" dir="auto">لوحات الألوان المحفوظة / Saved palette combinations</span>')
content = content.replace('placeholder="Purpose (optional)"', 'placeholder="الهدف (اختياري) / Purpose (optional)"')
content = content.replace('Save current palette</button>', 'حفظ اللوحة الحالية / Save current palette</button>')
content = content.replace('<span style="font-size:12px;color:var(--text3);">None saved yet</span>', '<span style="font-size:12px;color:var(--text3);" dir="auto">لم يتم حفظ شيء بعد / None saved yet</span>')

# Step 2
content = content.replace('<div class="step-badge">Step 3 of 6</div>', '<div class="step-badge">الخطوة 3 من 6 / Step 3 of 6</div>')
content = content.replace('<p class="step-eyebrow">Typography</p>', '<p class="step-eyebrow" dir="auto">الخطوط / Typography</p>')
content = content.replace('<h1 class="step-title">Choose your fonts</h1>', '<h1 class="step-title" dir="auto">اختر خطوطك<br><span style="font-size:28px">Choose your fonts</span></h1>')
content = content.replace('<p class="step-desc">Select one English font and one Arabic font. Each live preview updates as you choose.</p>', '<p class="step-desc" dir="auto">اختر خطاً إنجليزياً واحداً وخطاً عربياً واحداً. يتم تحديث المعاينة المباشرة مع كل اختيار.<br>Select one English font and one Arabic font. Each live preview updates as you choose.</p>')
content = content.replace('<span class="section-label">English preview</span>', '<span class="section-label" dir="auto">المعاينة بالإنجليزية / English preview</span>')
content = content.replace('<span class="section-label">English fonts</span>', '<span class="section-label" dir="auto">الخطوط الإنجليزية / English fonts</span>')
content = content.replace('<span class="section-label">Arabic preview</span>', '<span class="section-label" dir="auto">المعاينة بالعربية / Arabic preview</span>')
content = content.replace('<span class="section-label">Arabic fonts</span>', '<span class="section-label" dir="auto">الخطوط العربية / Arabic fonts</span>')

# Step 3
content = content.replace('<div class="step-badge">Step 4 of 6</div>', '<div class="step-badge">الخطوة 4 من 6 / Step 4 of 6</div>')
content = content.replace('<p class="step-eyebrow">Style & Mood</p>', '<p class="step-eyebrow" dir="auto">الأسلوب والمزاج / Style & Mood</p>')
content = content.replace('<h1 class="step-title">What\'s the vibe?</h1>', '<h1 class="step-title" dir="auto">ما هو الطابع العام؟<br><span style="font-size:28px">What\'s the vibe?</span></h1>')
content = content.replace('<p class="step-desc">Select all styles that resonate — you can pick more than one.</p>', '<p class="step-desc" dir="auto">اختر جميع الأساليب التي تناسبك — يمكنك اختيار أكثر من واحد.<br>Select all styles that resonate — you can pick more than one.</p>')
content = content.replace('<span class="section-label">Formality vs personality</span>', '<span class="section-label" dir="auto">الرسمية مقابل الشخصية / Formality vs personality</span>')
content = content.replace('<span>Casual &amp; Friendly</span><span>Luxurious &amp; Formal</span>', '<span dir="auto">عفوي وودي<br>Casual &amp; Friendly</span><span dir="auto" style="text-align:left;">فاخر ورسمي<br>Luxurious &amp; Formal</span>')
content = content.replace('<label class="field-label">Websites or brands that inspire you <span class="field-optional">optional</span></label>', '<label class="field-label" dir="auto">مواقع أو علامات تجارية تلهمك / Websites or brands that inspire you <span class="field-optional">اختياري / optional</span></label>')

# Step 4
content = content.replace('<div class="step-badge">Step 5 of 6</div>', '<div class="step-badge">الخطوة 5 من 6 / Step 5 of 6</div>')
content = content.replace('<p class="step-eyebrow">Inspiration Gallery</p>', '<p class="step-eyebrow" dir="auto">معرض الإلهام / Inspiration Gallery</p>')
content = content.replace('<h1 class="step-title">Tell us what you love</h1>', '<h1 class="step-title" dir="auto">أخبرنا بما يعجبك<br><span style="font-size:28px">Tell us what you love</span></h1>')
content = content.replace('<p class="gallery-desc">Eight example website aesthetics across four style directions. Label each one and add an optional comment.</p>', '<p class="gallery-desc" dir="auto">ثمانية أمثلة لتصاميم مواقع. قيم كل منها وأضف تعليقاً اختيارياً.<br>Eight example website aesthetics. Label each one and add an optional comment.</p>')
content = content.replace('[\'love\',\'Love\'],[\'inspire\',\'Inspire\'],[\'meh\',\'Meh\'],[\'avoid\',\'Avoid\']', '[\'love\',\'أعجبني<br>Love\'],[\'inspire\',\'مُلهم<br>Inspire\'],[\'meh\',\'عادي<br>Meh\'],[\'avoid\',\'تجنب<br>Avoid\']')
content = content.replace('placeholder="Optional comment"', 'placeholder="تعليق اختياري / Optional comment"')

# Step 5
content = content.replace('<div class="step-badge">Step 6 of 6</div>', '<div class="step-badge">الخطوة 6 من 6 / Step 6 of 6</div>')
content = content.replace('<p class="step-eyebrow">Final thoughts</p>', '<p class="step-eyebrow" dir="auto">أفكار أخيرة / Final thoughts</p>')
content = content.replace('<h1 class="step-title">Final thoughts</h1>', '<h1 class="step-title" dir="auto">أفكار أخيرة<br><span style="font-size:28px">Final thoughts</span></h1>')
content = content.replace('placeholder="Anything else you\'d like us to know? This is your open canvas."', 'placeholder="هل هناك أي شيء آخر تود أن نعرفه؟ المساحة لك. / Anything else you\'d like us to know?"')

# Final Thank you modifications
content = content.replace('<h1 class="ty-title">Thank you!</h1>', '<h1 class="ty-title">شكراً لك! / Thank you!</h1>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Translation applied successfully!')
