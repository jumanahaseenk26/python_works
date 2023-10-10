lst=[10,11,10,11,12,13]
lst.sort()
duplicate_list=[]
for i in range(0,len(lst)-1):
    if (lst[i]==lst[i+1]):
        if lst[i] not in duplicate_list:
            duplicate_list.append(lst[i])
print("Duplicate numbers are: ",duplicate_list)
        