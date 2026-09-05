import re

with open('wedding-visual-brief.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Current button: <button id="langToggle" style="background:none;border:1px solid var(--border);border-radius:6px;padding:4px 8px;font-size:12px;color:var(--text);cursor:pointer;font-family:var(--mono);">EN</button>
# New button: <button id="langToggle" style="background:var(--surface2);border:1px solid var(--border-active);border-radius:8px;padding:8px 16px;font-size:14px;font-weight:600;color:var(--accent);cursor:pointer;font-family:var(--mono);transition:all 0.2s;box-shadow:0 2px 8px rgba(37,99,235,0.1);">EN</button>
# Plus a hover effect via CSS, but since it's inline, it's easier to just add a CSS class or append it to the <style> block.

# Let's add a CSS class to the <style> block and use it.
style_addition = """
.lang-toggle-btn {
  background: var(--surface);
  border: 1.5px solid var(--accent);
  border-radius: 8px;
  padding: 8px 16px;
  font-size: 14px;
  font-weight: 700;
  color: var(--accent);
  cursor: pointer;
  font-family: var(--mono);
  transition: all 0.2s;
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.15);
}
.lang-toggle-btn:hover {
  background: var(--accent);
  color: #fff;
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(37, 99, 235, 0.25);
}
</style>
"""

html = html.replace('</style>', style_addition)

old_btn = r'<button id="langToggle" style="background:none;border:1px solid var\(--border\);border-radius:6px;padding:4px 8px;font-size:12px;color:var\(--text\);cursor:pointer;font-family:var\(--mono\);">EN</button>'
new_btn = '<button id="langToggle" class="lang-toggle-btn">EN</button>'
html = re.sub(old_btn, new_btn, html)

with open('wedding-visual-brief.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Button updated")
