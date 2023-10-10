lst=[10,2,13,14,5]
element=6
i=0
is_present=False
limit=len(lst)
while(i<limit):
    cur_val=lst[i]
    if cur_val==element:
        is_present=True
        break
    i+=1
print(is_present)