employee={"name":"shabeer","gender":"male","age":33,"salary":2000}
#key:value pairs
#print(employee["name"])
#print(employee["gender"])
#print(employee["age"])

if("gender" in employee):
    print("present")
else:
    print("not present")

#employee["salary"]=20000
#print(employee["salary"])

employee["salary"]+=5000
print(employee["salary"])