class BankAccount:
    def __init__ (self, account_balance=0)
        self.account_balance = account_balance

    def deposit (self, amount)
        updated_balance = self.account_balance + amount
        print (f"Deposited:{amount}$")



    def withdraw (self, amount)
        updated_balance = self.account_balance - amount
        print (f"Withdrew:{amount}$")


    def display_balance (self)     
        print (f"Current Balance: ${self.account_balance}")
