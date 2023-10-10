text="fast"
out="facts"
text_sot=sorted(text)
out_sot=sorted(out)
if text_sot==out_sot:
    print("texts are anagram")
else:
    print("not anagram")