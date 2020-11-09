class Account:
    """A bank account that has no negative balance
    class attributes: balance, holder, interest
    """

    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance"""
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        return self.balance


class CheckingAccount(Account):
    """inherit from Account
    class attributes: balance, holder, interest, withdraw_charge
    """

    interest = 0.01
    withdraw_charge = 1
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)

class PremiumChecking(CheckingAccount):
    withdraw_charge = 0.5




class SavingAccount(Account):
    deposit_charge = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)

class AsSeenOnTVAccount(CheckingAccount, SavingAccount):
    def __init__(self, account_holder):
        self.balance = 1
        self.holder = account_holder





