
f_read=open("C:\\Users\\hp\\Desktop\\python_works\\file_input_output\\write.txt")
odd_write=open("C:\\Users\\hp\\Desktop\\python_works\\file_input_output\\odd_write.txt","w")
even_write=open("C:\\Users\\hp\\Desktop\python_works\\file_input_output\\even_write.txt","w")
for line in f_read:
    num=int(line.rstrip("\n"))
    if num%2==0:
        even_write.write(str(num)+"\n")
    else:
        odd_write.write(str(num)+"\n")