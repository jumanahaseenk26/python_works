text="ABCDA"
wc={}
for ch in text:
    if ch in wc:
        print("The first recursive charecter is:",ch)
        break
    else:
        wc[ch]=1