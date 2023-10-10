year=int(input("Enter the year :"))
print(year)
if(year%100==0 and year%400==0):
    print("this year is a leap year")
elif(year%100!=0 and year%4==0):
    print("This year is a leap year")
else:
    print("This year not a leap year")

#print("leap year" if year%100==0 and year%400==0 else "leap year" if year%100==0 and year%4==0 else "not leap year")