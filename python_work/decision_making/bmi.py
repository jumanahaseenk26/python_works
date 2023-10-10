height_incm=int(input("Enter height in cm :"))
weight_inkg=int(input("Enter weight in kg :"))
height_mtr=height_incm/100
bmi=weight_inkg//height_mtr**2
print(bmi)
if(bmi<=19):
    print("under weight")
elif(bmi<=25):
    print("normal weight")
elif(bmi<=30):
    print("over weight")
else:
    print("obesity")