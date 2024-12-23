import bs4 
import sys

# open file
with open(sys.argv[1]) as f:
    data = f.read()

s = bs4.BeautifulSoup(data, features="xml")

# get the style colours
styles = s.findAll( lambda tag:tag.name == "style" and 
                "tts:color" in tag.attrs)

# print(styles)

# make dict and merge
style = [{s.get("xml:id"): s.get("tts:color")[:7]} for s in styles]
style = {key:val for d in style for key,val in d.items()}

# print(style)

# get subtitles
subs = s.findAll( lambda tag:tag.name == "p" and "begin" in tag.attrs)
# print(subs[:5])

# reformat print out
num = 0
for ss in subs:
    num += 1
    b = f'{ss.get("begin")}'.replace(".",",")
    e = f'{ss.get("end")}'.replace(".",",")
    if not "," in b: b = b + ",000"
    if not "," in e: e = e + ",000"
    print(f'{num}\n{b} --> {e}')
    spans = ss.findAll("span")
    for sp in spans:
        c = sp.get("style")
        t = sp.text
        print(f'<font color="{style[c]}">{t}</font>')
    print()


