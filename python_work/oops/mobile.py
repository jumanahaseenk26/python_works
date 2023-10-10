class mobile:
    model:str
    color:str
    memory:int
    price:int

    def __init__(self,model,color,memory,price):
        self.model=model
        self.color=color
        self.memory=memory
        self.price=price

    def get(self):
        print(self.model,"\n",self.color,"\n",self.memory,"\n",self.price)
mob=mobile("samsung","black",64,24000)    
mob.get()