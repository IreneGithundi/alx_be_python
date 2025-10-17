class BankAccount:
    def __init__(self, account_balance):
        self.acc_balance = account_balance
        account_balance = 0
    
    def deposit(self, amount):
        self.acc_balance += amount

    def withdraw(self, amount):
        if self.acc_balance >= amount:
            self.acc_balance -= amount
            return True
        else:
            return False
        
    def display_balance(self):
        return(f"Current Balance: ${self.acc_balance}")



