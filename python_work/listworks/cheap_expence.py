expences=[1100,1200,1000,1600,1800,900]
min_exp=expences[0]
for e in expences:
    if e<min_exp:
        min_exp=e
print("cheapest expence :",min_exp)