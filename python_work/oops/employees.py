class employee:
    data=[
        {"id":1,"name":"jhon","dept":"hr","salary":34000},
        {"id":2,"name":"hari","dept":"it","salary":24000},
        {"id":3,"name":"ravi","dept":"qa","salary":64000},
        {"id":4,"name":"vijay","dept":"hr","salary":74000},
        {"id":5,"name":"tom","dept":"it","salary":24000},
        {"id":6,"name":"vipin","dept":"qa","salary":14000},]
    #print all the datas
    def get(self,*args,**kwargs):
        return self.data
    #print one employee data
    def retrieve(self,*args,**kwargs):
        id=kwargs.get("id")
        record=[emp for emp in self.data if emp.get("id")==id]
        return record
    #add one employee data
    def create(self,*args,**kwargs):
        self.data.append(kwargs)
    #delete one employee data
    def disroy(self,*args,**kwargs):
        id=kwargs.get("id")
        delete=[e for e in self.data if e.get("id")==id].pop()
        self.data.remove(delete)
    def update(self,id=None,*args,**kwargs):
        id=id
        obj=[emp for emp in self.data if emp.get("id")==id][0]
        obj.update(kwargs)
        print("employee object updated")
obj=employee()
#print(obj.retrieve(id=4))
#obj.disroy(id=4)
#obj.create(id=7,name="vishnu",dept="hr",salary=24000)
obj.update(id=4,salary=24000)
#print(obj.get())
print(obj.retrieve(id=4))
