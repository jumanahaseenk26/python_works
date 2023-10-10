num=int(input("Enter the number:"))
prev=0
current=1
fibo_num=0
start=1
is_fibo=False
while(fibo_num<=num):
    fibo_num=prev+current
    prev=current
    current=fibo_num
    if(fibo_num==num):
        is_fibo=True
        break
print(is_fibo)