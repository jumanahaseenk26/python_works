from re import *
text="abababcdab"
matcher=finditer("ab",text)
count=0
for m in matcher:
    print(m.start(),m.group())
    count+=1
print(count)