lst=[3,1,5,6,4,]
lst.sort()
if lst[0]!=1:
    print("1 is missing")
else:
    for i in range(0,len(lst)):
        diff=lst[i+1]-lst[i]
        if diff!=1:
            print(lst[i]+1," is missing")
            break
