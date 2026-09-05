import re

with open('wedding-visual-brief.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace var STYLES=[...] with function getStyles() { return [...] }
html = re.sub(r'var STYLES=\[.*?\];', lambda m: m.group(0).replace('var STYLES=', 'function getStyles() { return ').replace('];', ']; }'), html, flags=re.DOTALL)

# Update references to STYLES to getStyles()
html = html.replace('STYLES.forEach', 'getStyles().forEach')

with open('wedding-visual-brief.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Styles fixed")
