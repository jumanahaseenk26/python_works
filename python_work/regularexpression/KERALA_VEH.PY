from re import *
vehicle_no=input("Enter vehicle no :")
rule="(kl)[\d]{2}[\w]{1,2}[\d]{4}"
matcher=fullmatch(rule,vehicle_no)
print("invalid" if matcher==None else "valid")