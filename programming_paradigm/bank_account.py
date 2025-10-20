class BankAccount:
    def __init__(self, account_balance):
        if account_balance >= 0:
            self._account_balance = account_balance

    @property
    def account_balance(self):
        return self._account_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount

    def withdraw(self, amount):
        if amount < self._account_balance:
            self._account_balance -= amount
            return True
        else:
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")

