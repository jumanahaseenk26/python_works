lst=[10,2,13,14,5]
element=2
lst.sort()
low=0
upper=len(lst)-1
is_present=False
while(low<upper):
    mid=(low+upper)//2
    if element==lst[mid]:
        is_present=True
        break
    elif element<lst[mid]:
        upper=mid-1
    elif element>mid:
        low=mid+1
print(is_present)
