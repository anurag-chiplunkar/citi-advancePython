# Abstraction

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance.")


class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


# Creating objects of SavingsAccount and CurrentAccount
savings_acc = SavingsAccount("SA-123", 5000)
current_acc = CurrentAccount("CA-456", 8000)

# Using the abstraction to deposit and withdraw
savings_acc.deposit(2000)
current_acc.withdraw(3000)

print(savings_acc.balance)  # Output: 7000
print(current_acc.balance)  # Output: 5000