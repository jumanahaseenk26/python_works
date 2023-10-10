class book:
    book_id:int
    name:str
    category:str
    price:int

    def create(self,id,name,category,price):
        self.id=id
        self.name=name
        self.category=category
        self.price=price

    def display_student(self):
        print(self.id,self.name,self.category,self.price)
        