from abc import ABC,abstractmethod
class banking_app(ABC):
    @abstractmethod
    def fundtransfer(self):
        pass
    @abstractmethod
    def balance_enquiry(self):
        pass
    @abstractmethod
    def transaction_history(self):
        pass
class googlepay(banking_app):
    def fundtransfer(self):
        print(" your a/c credited by")
    def balance_enquiry(self):
         print("balance is" )
    def transaction_history(self):
         print("history")
obj=googlepay()
obj.fundtransfer()
obj.balance_enquiry()
obj.transaction_history()