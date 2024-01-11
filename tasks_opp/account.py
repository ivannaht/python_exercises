class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amt):
        self.balance += dep_amt
        return f"Added {dep_amt}$ to the account"

    def withdrawal(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            return "Withdrawal accepted."
        else:
            return "Sorry not enough funds!"

    def __str__(self):
        return f"Owner: {self.owner}\nBalance: {self.balance}$"


account_1 = Account("John", 1000)
print(account_1.owner)
print(account_1.balance)
print(account_1.deposit(200))
print(account_1.withdrawal(700))
print(account_1)
