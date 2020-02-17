from BankAccount import BankAccount


ba = BankAccount("Denzil")

ba.deposit(50)
ba.deposit(50)

ba.withdraw(20)
ba.withdraw(30)
ba.withdraw(40)
ba.withdraw(50)
 
print(ba)