range=1
prev=0
current=1
num=int(input("Enter a number: "))
print(prev)
print(current)
while(range<=num):
    sum=prev+current
    print(sum)
    prev=current
    current=sum
    range+=1
