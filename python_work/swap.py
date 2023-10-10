num1=10
num2=20

#logic1

#num1,num2=num2,num1
#print(f"value after swapping num1 = {num1} num2 = {num2}")

#logic 2

#temp=num1
#num1=num2
#num2=temp
#print(f"value after swapping num1 = {num1} num2 = {num2}")

#logic 3

num1=num1+num2
num2=num1-num2
num1=num1-num2
print(f"value after swapping num1 = {num1} num2 = {num2}")