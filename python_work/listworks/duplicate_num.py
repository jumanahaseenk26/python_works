last=[2,1,5,5,3,6,3,4]
last.sort()
#print(last)
duplicate_list=[]
for i in range(0,len(last)-1):
    if (last[i]==last[i+1]):
        if last[i] not in duplicate_list:
            duplicate_list.append(last[i])
print("Duplicate numbers are: ",duplicate_list)
        

