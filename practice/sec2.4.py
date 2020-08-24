

def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""

    def withdraw(amount):
        if amount > balance:
            return 'Insufficient funds.'
        balance = balance - amount
        return balance
    return withdraw
