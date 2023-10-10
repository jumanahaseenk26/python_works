from re import *
tyre_code=input("Enter tyre code :")
rule="\d{3}[/]\d{2}R\d{2}[/]\d{2,3}[A_Z]"
matcher=fullmatch(rule,tyre_code)
print("invalid" if matcher==None else "valid")