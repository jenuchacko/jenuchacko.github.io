from pathlib import Path
import html, re

base=Path(__file__).resolve().parent
text=(base/'cv.md').read_text(encoding='utf-8')
def inline(s):
    s=html.escape(s)
    s=re.sub(r"\*\*(.+?)\*\*",r"<strong>\1</strong>",s)
    return re.sub(r"\[([^]]+)\]\((https?://[^ )]+|mailto:[^ )]+)\)",r'<a href="\2">\1</a>',s)
out=[]
for block in text.strip().split('\n\n'):
    if block.startswith('# '): out.append('<h1>'+inline(block[2:])+'</h1>')
    elif block.startswith('## '):
        title=block[3:]; slug=re.sub('[^a-z0-9]+','-',title.lower()).strip('-')
        out.append('<h2 id="'+slug+'">'+inline(title)+'</h2>')
    elif block.startswith('- '): out.append('<ul>'+''.join('<li>'+inline(x[2:])+'</li>' for x in block.splitlines())+'</ul>')
    else: out.append('<p>'+inline(block).replace('\n','<br>')+'</p>')
first_section=next(i for i,v in enumerate(out) if v.startswith('<h2'))
out=['<div class="intro"><div>'+''.join(out[:first_section])+'</div><img class="portrait" src="profile.jpg" alt="Jenu Varghese Chacko" width="160" height="190"></div>']+out[first_section:]
template=(base/'template.html').read_text(encoding='utf-8')
(base/'index.html').write_text(template.replace('<!-- CV -->','\n'.join(out)),encoding='utf-8')
print('Built index.html from cv.md')
