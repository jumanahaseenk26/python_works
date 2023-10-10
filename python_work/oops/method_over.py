class calculator:
    def add(self,*args):
        return sum(args)
obj=calculator()
print(obj.add(10,20,30))