from abc import ABC,abstractmethod
class atm(ABC):
    @abstractmethod
    def reset_pin():
        pass
    def deposite():
        pass
    def withdraw():
        pass
    def check_balance():
        pass
class new_atm(atm):
    def __init__(self,pin,balance):
        self.pin = pin
        self.balance = balance
    def reset_pin(self):
        p = int(input("Enter your current pin : "))
        if self.pin == p:
            new = int(input("Enter your new pin : "))
            self.pin = new
            print("pin reset successfull")
        else:
            print("Invalid pin")

    def deposite(self):
        p = int(input("Enter your current pin : "))
        if self.pin == p:
            amt = int(input("Enter the Amount to deposite : "))
            if amt > 0:
                self.balance += amt
                print("Your")
            else:
                print("invalid amount")
        else:
            print("Invalid pin")

ob = new_atm(1234,10000)
# ob.reset_pin()
ob.deposite()