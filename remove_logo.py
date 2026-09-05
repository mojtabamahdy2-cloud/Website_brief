import re

with open('wedding-visual-brief.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove initial HTML content for logoText
html = re.sub(r'<div class="logo" id="logoText">.*?</div>', '<div class="logo" id="logoText"></div>', html)

# Remove JS updates for logoText
html = re.sub(r'document\.getElementById\(\'logoText\'\)\.innerHTML = state\.lang === \'ar\'.*?: \'Client <span>Name</span> &mdash; Website Brief\';', '', html, flags=re.DOTALL)
html = re.sub(r'document\.getElementById\(\'logoText\'\)\.innerHTML = \'Client <span>Name</span> &mdash; Website Brief\';', '', html)

with open('wedding-visual-brief.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Logo removed")
