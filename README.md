# Simple Banking Program

This project simulates basic banking operations using Python classes. It includes functionalities for creating bank accounts, depositing, withdrawing, transferring funds between accounts, and handling different types of accounts including basic and interest-earning accounts.

## Features

- BankAccount: Basic banking operations.
- InterestAccount: Inherits from BankAccount, adds interest to deposits.
- SavingsAccount: Inherits from InterestAccount, applies a withdrawal fee.

## Usage

Ensure Python is installed on your system. This application consists of two main files: main.py and BankAccount.py.

### Main Operations

- Create accounts with initial balances.
- Perform deposits and withdrawals.
- Transfer funds between accounts.
- Specialized account types accrue interest on deposits and may have fees on withdrawals.

### Example:

```python
from bank_account import *

# Creating accounts
Juan = BankAccount(1000, "Juan")
Naomi = BankAccount(1000, "Naomi")
JC = InterestAccount(1000, "JC")
Ellena = SavingsAccount(1000, "Ellena")

# Performing transactions
Juan.deposit(500)
Naomi.transfer(500, Juan)
JC.deposit(100)
Ellena.transfer(10000, Juan)
```

### Account Types

- BankAccount: The standard account for basic transactions.
- InterestAccount: A type of account that gives an interest bonus on every deposit.
- SavingsAccount: Similar to InterestAccount but also charges a fee for withdrawals.

### Running the Application

Run the application using Python:

```zsh
python main.py
```


