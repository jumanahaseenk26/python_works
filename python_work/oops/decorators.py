class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @property
    def get_name(self):
        return self.name
    @property
    def get_age(self):
        return self.age
obj=student("jumana",23)
print(obj.get_name)
print(obj.get_age)        