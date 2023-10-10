from re import *
text="abcdABCuoD7e9fk"
#Pattern="[0-9]"
#Pattern="[a-z]"
#Pattern="[A-Z]"
#Pattern="[a-zA-Z]"all alphabet
#Pattern="[a-zA-Z0-9]"#allalphabets and numbers
#Pattern="[^0-9]"#except numbers
#pattern="[^a-zA-Z0-9]"
#Pattern="[^AEIOUaeiou]"
Pattern="[b-df-hj-np-tv-z]"
matcher=finditer(Pattern,text)
for m in matcher:
        print(m.group())