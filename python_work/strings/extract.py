text="ihave one car 2 bikes and 3 cycles"
word=text.split(" ")
for w in word:
    if w.isdigit():
        print(w)