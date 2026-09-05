import re

with open('wedding-visual-brief.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update state object
html = re.sub(
    r'var state={',
    'var state={\n  groomName:"", brideName:"",',
    html
)

# 2. Update step0
new_step0_html = """function step0(){
  var h = '<div style="text-align:center;padding:10px 0 30px;">'+
  '<p class="step-eyebrow" style="text-align:center;" dir="auto">'+T('مرحباً بك في','Welcome to your')+'</p>'+
  '<h1 class="step-title" style="text-align:center;font-size:42px;" dir="auto">'+T('موجز التصميم المرئي','Visual Onboarding Brief')+'</h1>'+
  '<p class="step-desc" style="text-align:center;max-width:50ch;margin:0 auto 0;" dir="auto">'+T('مرحباً! يساعدنا هذا النموذج القصير على فهم ذوقك وأسلوبك وأهدافك لنتمكن من بناء موقع يعبر عنك حقاً.','Hello! This short visual form helps us understand your taste, style, and goals so we can build a website that truly feels like <em>you</em>.')+'</p>';
  
  h += '<div style="max-width:400px; margin: 36px auto 0; text-align: '+ (state.lang === 'ar' ? 'right' : 'left') +';">'+
    '<div style="margin-bottom: 20px;">'+
      '<label class="field-label" dir="auto">'+T('اسم العريس (بالإنجليزية)','Groom\\'s First Name (English)')+'</label>'+
      '<input type="text" id="groomNameInp" value="'+esc(state.groomName)+'" placeholder="e.g. Alex" dir="ltr">'+
    '</div>'+
    '<div>'+
      '<label class="field-label" dir="auto">'+T('اسم العروس (بالإنجليزية)','Bride\\'s First Name (English)')+'</label>'+
      '<input type="text" id="brideNameInp" value="'+esc(state.brideName)+'" placeholder="e.g. Taylor" dir="ltr">'+
    '</div>'+
  '</div>';
  
  h += '</div>';
  document.getElementById('stepContent').innerHTML=h;
  
  document.getElementById('groomNameInp').oninput=function(){state.groomName=this.value;save();};
  document.getElementById('brideNameInp').oninput=function(){state.brideName=this.value;save();};
  
  renderNav(true,false,false);
}"""
# replace old step0
html = re.sub(r'function step0\(\)\{.*?renderNav\(true,false,false\);\s*\}', new_step0_html, html, flags=re.DOTALL)

# 3. Update cleanData in done()
# Find the cleanData object definition and insert the names at the beginning
clean_data_replacement = """var cleanData = {
    "0a. Groom's Name": state.groomName,
    "0b. Bride's Name": state.brideName,
    "1. Color Palette": cList,"""
html = re.sub(r'var cleanData = \{\s*"1\. Color Palette": cList,', clean_data_replacement, html)

with open('wedding-visual-brief.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added names to step 0")
