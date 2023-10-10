from re import *
variable=input("Enter variable name:")
rule="[klm][369][\w]*"
matcher=fullmatch(rule,variable)
print("invalid" if matcher==None else "valid")