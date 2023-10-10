from re import *
f=open("C:\\Users\\hp\\Desktop\\python_works\\aemail\\email.txt")
phone_rule="\d{10}"
mail_rule="\w+@(gmail.com)"
email=[]
contact=[]
for line in f:
    words=line.rstrip("\n").split()
    for w in words:
        matcher=fullmatch(phone_rule,w)
        email_matcher=fullmatch(mail_rule,w)
        if matcher!=None:
            contact.append(w)
        elif email_matcher!=None:
            email.append(w)
print(contact)
print(email)