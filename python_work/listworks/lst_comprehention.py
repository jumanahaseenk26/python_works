lst=[2,3,4,6,7,8]

years=[y for y in range(1800,2026)]
#print(years)

century_year=[y for y in years if y%100==0]
print(century_year)

noncentury_year=[y for y in years if y%100!=0]
print(noncentury_year)

#even=[n for n in lst if n%2==0]
#print(even)
#odd=[n for n in lst if n%2!=0]
#print(odd)

#cube=[n**3 for n in lst]
#print(cube)

#square=[n**2 for n in lst]
#print(square)

#add_two=[n+2 for n in lst]
#print(add_two)