text=input("Enter the text:")

def alphcount(text):
    v_count=0
    c_count=0
    for i in range(len(text)):
        if text[i] in ["a","e","i","o","u"]:
            v_count+=1
        else:
            c_count+=1
    print(v_count)
    print(c_count)
alphcount(text)