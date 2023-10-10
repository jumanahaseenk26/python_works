from re import *
variable=input("Enter a variale name: ")
rule="[a-zA-Z][\w_]*"
matcher=fullmatch(rule,variable)
print("valid" if matcher!=None else "invalid")