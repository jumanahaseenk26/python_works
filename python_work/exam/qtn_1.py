txt="pycharm is an ide"
v_count=0
c_count=0
for ch in txt:
    if ch in ["a","e","i","o","u"]:
        v_count+=1
    elif ch not in [" "]:
        c_count+=1
print(len(txt))
print("vowel count:",v_count)
print("consenant count:",c_count)