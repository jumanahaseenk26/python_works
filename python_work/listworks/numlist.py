numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_list=[]
odd_list=[]
for n in numbers:
    if n%2==0:
        even_list.append(n)
    else:
        odd_list.append(n)
print(even_list)
print(odd_list)