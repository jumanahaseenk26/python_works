def product(*args):
    res=1
    for n in args:
        res*=n
    return res 

print(product(1,3,2))
