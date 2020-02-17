
class BankAccount():
    
    def __init__ (self, owner):
        self.balance = 0
        self.owner = owner

    def __repr__ (self):
        return f"Account for {self.owner}. Balance is {self.balance}" 

    def deposit(self, amt):
        self.balance += amt
        print(f"Activity for account : {self.owner}. A deposit of {amt} was successifuly, new balance is {self.balance}")
        return self.balance

    def withdraw(self, amt):
        if amt > self.balance :
            print( f"Activity for account : {self.owner}. Cannot withdraw, amount {amt}, is greater than available balance {self.balance}!" )
            return f"Activity for account : {self.owner}. Withdraw amount {amt}, is greater than available balance {self.balance}!"
        else:
            self.balance -= amt
            print(f"Activity for account : {self.owner}. A withdrawal of {amt} was successifuly, new balance is {self.balance}")
            return self.balance
            
