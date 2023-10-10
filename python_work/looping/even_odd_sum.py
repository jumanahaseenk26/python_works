start=10
end=20
odd_sum=0
even_sum=0
while(start<=end):
    if start%2==0:
        odd_sum=odd_sum+start
    else:
        even_sum=even_sum+start
    start+=1
print("odd sum is :",odd_sum )
print("Even sum is :",even_sum)