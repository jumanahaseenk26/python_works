num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
num3=int(input("Enter the number3:"))
def largest(num1,num2,num3):
    if(num1>num2)and(num1>num3):
        print("Largest number is ",num1)
    elif(num2>num1)and(num2>num3):
        print("Largest number is ",num2)
    else:
        print("Largest number is ",num3)
largest(num1,num2,num3)