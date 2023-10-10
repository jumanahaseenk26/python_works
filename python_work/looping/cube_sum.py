num=int(input("Enter the digit:"))
original=num
sum=0
while(num!=0):
    last_digit=num%10
    digit_cube=last_digit**3
    sum=sum+digit_cube
    num=num//10
if(original==sum):
    print("this is a amstong number")
else:
    print("Not amstrong number")
#print("Sum of the number cubes:",sum)