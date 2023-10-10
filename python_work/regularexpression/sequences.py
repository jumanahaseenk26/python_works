from re import *
text="abcd12KABC@#"
#Pattern="\d"[0-9]
#Pattern="\D"#except 0-9
#Pattern="\w"#alphanumeric
#Pattern="\W"#special charecters
Pattern="[^aeiou_\W\d]"#consanants
matcher=finditer(Pattern,text.casefold())
for m in matcher:
    print(m.group(),m.start())