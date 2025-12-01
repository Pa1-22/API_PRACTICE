from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def bank_details():
        pass
class Bankaccount(Bank):
    def bank_details(self):
        print("bank is anm")       
n=Bankaccount()
n.bank_details()