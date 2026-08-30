class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Na konto bankowe o numerze " + self.account_number + " wpłynęła kwota " + amount + " zł")
    def withdraw(self, amount):
        if amount > 0:
            if amount < self.balance:
                self.balance -= amount
                print(f"Z konta bankowego o numerze " + self.account_number + " wypłacono kwotę " + amount + " zł")
    
                