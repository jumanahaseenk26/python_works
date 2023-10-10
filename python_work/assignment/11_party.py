num=int(input("how many people you want to invite: "))
start=1
while(start<=num):
    if num<10:
        name=input("what is thier names: ")
        print(name," has been invited")
        start+=1
    else:
        print("Too many people")
        break