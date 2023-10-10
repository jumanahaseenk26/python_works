#f=open("C:\\Users\\hp\\Desktop\\python_works\\file_input_output\\data.txt","w")
#[f.write(str(y)+"\n") for y in range(1800,2026)]
fread=open("C:\\Users\\hp\\Desktop\\python_works\\file_input_output\\data.txt")
fwrite=open("C:\\Users\\hp\\Desktop\\python_works\\file_input_output\\lyear.txt","w")
for line in fread:
    year=int(line.rstrip("\n"))
    if(year%100==0) and (year%400==0):
        fwrite.write(str(year)+"\n")
    elif (year%100!=0) and (year%4==0):
        fwrite.write(str(year)+"\n")