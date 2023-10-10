text="Sunil gavaskar has a no-holds-barred remark on overseas commentators"
vowels="a","e","i","o","u"
word=text.split(" ")
print(word)
for w in word:
    if w.casefold().startswith(vowels):
        print(w)