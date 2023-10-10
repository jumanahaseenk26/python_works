from re import *
pan_no=input("Enter pancard no :")
rule="[A-Z]{3}[PFACHT]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}"
matcher=fullmatch(rule,pan_no)
print("invalid" if matcher==None else "valid")