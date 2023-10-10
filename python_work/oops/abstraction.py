from abc import ABC,abstractmethod
class car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def accelarate(self):
        pass
class swift(car):
    def start(self):
        print("swift start")
    def accelarate(self):
         print("swift accelarate")
    def stop(self):
         print("swift stop")
obj=swift()
obj.start()
obj.accelarate()
obj.stop()