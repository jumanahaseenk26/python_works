tummy_size=int(input("Enter the tummy size :"))
buttok_size=int(input("Enter the buttok size :"))
gender=input("Enter the gender (male/female) :")
measurment=tummy_size/buttok_size
val=round(measurment,2)
print(val)
if gender=="male":
    if(val<=0.95):
        print("health risk low and body shape is pear")
    elif(val<=1.0):
        print("health risk moderate and body shape is avocado")
    else:
        print("health risk high and body shape is apple")
elif gender=="female":
     if(val<=0.80):
        print("health risk low and body shape is pear")
     elif(val<=0.85):
        print("health risk moderate and body shape is avocado")
     else:
        print("health risk high and body shape is apple")
else:
    print("enter a valid gender")