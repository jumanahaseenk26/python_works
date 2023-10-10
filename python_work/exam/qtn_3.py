lst1=[10,11,13,15]
lst2=[9,8,11,13,14]
lst1.sort()
lst2.sort()
l1,l2=0,0
print("Common numbers are: ")
while(l1<len(lst1) and l2<len(lst2)):
    if lst1[l1]==lst2[l2]:
        print(lst1[l1])
        l1+=1
        l2+=1
    elif lst1[l1]<lst2[l2]:
        l1+=1
    else:
        l2+=1
