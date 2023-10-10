f=open("C:\\Users\hp\\Desktop\\python_works\\file_input_output\\data.txt","r")
#lst=[]
#for line in f:
#    lst.append(line.rstrip("\n"))
#print(lst)
#longest_word=max(lst,key=lambda w:len(w))
#print(longest_word)
word=[line.rstrip("\n") for line in f]
longest_word=max(word,key=lambda w:len(w))
print(longest_word)