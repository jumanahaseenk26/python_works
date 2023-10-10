class student:
    reg_no:int
    name:str
    gender:str
    course:str

    def __init__(self,reg_no,name,gender,course):
        self.reg_no=reg_no
        self.name=name
        self.gender=gender
        self.course=course

    def display_student(self):
        print(self.reg_no,self.name,self.gender,self.course)

    def __str__(self):
        return self.name
    
stud=student(13,"jumana","female","python")
stud.display_student()
print(stud)