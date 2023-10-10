lst=[2,3,5,7,4]
lst.sort()
sum=9
lower=0
upper=len(lst)-1
while(lower<upper):
    cur_sum=lst[lower]+lst[upper]
    if cur_sum==sum:
        print("pairs are: ",lst[lower],lst[upper])
        lower+=1
    elif cur_sum<sum:
        lower+=1
    else:
        upper-=1

