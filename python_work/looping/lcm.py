num1=int(input("Enter the number1 :"))
num2=int(input("Enter the number2 :"))
if num1<=num2:
    for num in range(1,num1+1):
        if(num1%num==0)and(num2%num==0):
            lcm=num
    print("lcm is:",lcm)