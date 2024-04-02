
class BalanceException(Exception):
  pass

class BankAccount:
  def __init__(self, initialAmount, accountName):
    self.balance = initialAmount
    self.name = accountName
    print(f"\nAccount created: '{self.name}'\nAccount balance: ${self.balance:.2f}")

  def getBalance(self):
    print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

  def deposit(self, amount):
    self.balance = self.balance + amount
    print("\nDeposit successful!")
    self.getBalance()

  def viableTransaction(self, amount):
    if self.balance >= amount:
      return 
    else:
      raise BalanceException(
        f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
      )

  def withdraw(self, amount):
    try:
      self.viableTransaction(amount)
      self.balance = self.balance - amount
      print("\nWithdraw successful!")
      self.getBalance()
    except BalanceException as error:
      print(f"\nWithdraw interrupted: {error}")

  def transfer(self, amount, account):
    try:
      print("\n************\n\nBeginning Transfer... ")
      self.viableTransaction(amount)
      self.withdraw(amount)
      account.deposit(amount)
      print("\nTransfer successful!\n\n************")
    except BalanceException as error:
      print(f"\nTransfer interrupted: {error}")

class InterestAccount(BankAccount):
  def deposit(self, amount):
    self.balance = self.balance + (amount * 1.05)
    print("\nDeposit successful!")
    self.getBalance()

class SavingsAccount(InterestAccount):
  def __init__(self, initialAmount, accountName):
    super().__init__(initialAmount, accountName)
    self.fee = 5

  def withdraw(self, amount):
    try:
      self.viableTransaction(amount + self.fee)
      self.balance = self.balance - (amount + self.fee)
      print("\nWithdraw successful!")
      self.getBalance()
    except BalanceException as error:
      print(f"\nWithdraw interrupted: {error}")
