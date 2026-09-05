import re

with open('wedding-visual-brief.html', 'r', encoding='utf-8') as f:
    html = f.read()

formality_replacement = """function getFormalityLabels() { return [
  {max:10,label:T('عفوي وودي','Casual & Friendly'),mood:T('مريح، دافئ، عفوي','Relaxed, warm, conversational')},
  {max:25,label:T('مريح وودود','Relaxed & Approachable'),mood:T('ودود مع لمسة من الأناقة','Friendly with a touch of polish')},
  {max:40,label:T('متوازن ومرحب','Balanced & Welcoming'),mood:T('مهني ولكن شخصي','Professional yet personable')},
  {max:55,label:T('مهني عصري','Modern Professional'),mood:T('نظيف، واثق، منظم','Clean, confident, structured')},
  {max:70,label:T('أنيق وراقي','Refined & Polished'),mood:T('مظهر راقي ومتناسق','Sophisticated, curated look')},
  {max:85,label:T('فاخر وعصري','Elevated & Editorial'),mood:T('راقي، جمالية فاخرة','High-end, upscale aesthetic')},
  {max:100,label:T('فاخر ورسمي','Luxurious & Formal'),mood:T('مرموق، موثوق، خالد','Prestigious, authoritative, timeless')}
]; }"""

html = re.sub(r'var FORMALITY_LABELS=\[.*?\];', formality_replacement, html, flags=re.DOTALL)
html = html.replace('FORMALITY_LABELS.length', 'getFormalityLabels().length')
html = html.replace('FORMALITY_LABELS[i]', 'getFormalityLabels()[i]')
html = html.replace('FORMALITY_LABELS[FORMALITY_LABELS.length-1]', 'getFormalityLabels()[getFormalityLabels().length-1]')

with open('wedding-visual-brief.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Formality fixed")
