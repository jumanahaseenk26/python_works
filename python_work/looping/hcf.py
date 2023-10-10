num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
#find hcf
for num in range(1,num2+1):
    
    if(num1%num==0)and(num2%num==0):
        hcf=num
print("hcf is:",hcf)