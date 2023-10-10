#def sum(n1,n2):
#    return n1+n2
sub=lambda n1,n2:n1-n2
print(sub(10,2))

#def cube(n):
#    return n**3
cube=lambda n:n**3
print(cube(5))

max_two=lambda n1,n2:n1 if n1>n2 else n2
print(max_two(12,10))

odd_even=lambda n1:"even" if n1%2==0 else "odd"
print(odd_even(5))

smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
print(smart_sub(25,35))

get_len=lambda w:len(w)
print(get_len("jeza"))




