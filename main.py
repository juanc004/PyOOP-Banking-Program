from bank_account import *

Juan = BankAccount(1000, "Juan")
Juan.getBalance()
Juan.deposit(500)

Naomi = BankAccount(1000, "Naomi")
Naomi.getBalance()
Naomi.deposit(500)

Naomi.transfer(500, Juan)

JC = InterestAccount(1000, "JC")

JC.getBalance()
JC.deposit(100)
JC.transfer(100, Naomi)

Ellena = SavingsAccount(1000, "Ellena")
Ellena.getBalance()
Ellena.deposit(100)
Ellena.transfer(10000, Juan)