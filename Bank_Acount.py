
class BankAccount:
    def __init__(self, account_number, account_holder_name, account_type, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. Current balance: {self.balance}")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. Current balance: {self.balance}")
    
    def check_balance(self):
        print(f"Current balance: {self.balance}")

account1 = BankAccount(1234567890, "Alice", "Savings", 5000)
account2 = BankAccount(2345678901, "Bob", "Current", 10000)
