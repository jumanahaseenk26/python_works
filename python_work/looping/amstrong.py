number=int(input("Enter the number:"))
original=number
digit_count=len(str(number))
sum=0
while(number!=0):
    last_digit=number%10
    exponent=last_digit**digit_count
    sum=sum+exponent
    number=number//10
print("amstrong number" if sum==original else "not amstrong number")