student={"Roll No":"NJ17BCAR13","Name":"Jumana","Course":"django"}
print(student["Course"])

if "total" in student:
    print("present")
else:
    print("not present")
student["grade"]="A"
print(student)