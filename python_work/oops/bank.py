from datetime import datetime
class bank:
    bank_name:str
    acno:int
    person_name:str
    ac_type:str
    balance:int

    def create(self,b_name,acno,p_name,ac_type,bal):
        self.bank_name=b_name
        self.acno=acno
        self.person_name=p_name
        self.ac_type=ac_type
        self.balance=bal
    def deposite(self,amount):
        self.balance+=amount
        print(f"your {self.bank_name} has been credited with {amount} available balance is{self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("transaction failed insufficient balance")
        else:
            self.balance-=amount
            print(f"your{self.bank_name} has been debited {amount} available balance is {self.balance}")
    def get_balance(self):
        print(f"your {self.bank_name} a/c {self.ac_type} available balance on {datetime.today()} is {self.balance}")
obj1=bank()
obj1.create("sbi","10234","vijay","savings",10002)

obj1.deposite(3000)
obj1.withdraw(5000)
obj1.get_balance()