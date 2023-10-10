lst=[2,3,6,4,2,8,6,7,8,12,10]
print("the original list is: ",lst)
res = [lst[n] for n in range(1, len(lst)-1) if lst[n+1] >
           lst[n] <lst[n-1] or lst[n+1] < lst[n] > lst[n-1]]
print(res)
print("Peaks and Valleys count : ", len(res))
