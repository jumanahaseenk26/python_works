from re import *
text="aabbcaabdaaa"
#pattern="a+"#one or more occurance
pattern="a*"#zero or more occurance
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())
