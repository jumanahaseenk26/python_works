text="ABBCDCE"
wc={}
dup_list=[]
for ch in text:
    if ch in wc:
        dup_list.append(ch)
    else:
        wc[ch]=1
print("Second duplicate charecter is:",dup_list[1])