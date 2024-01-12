class BankAccount():
    """
    The class should have the following restrictions:
    - account_number should not be accessible from outside the class
    - balance should not be directly accessible from outside the class,
    it should only be accessible through the methods deposit() and withdraw()
    - account_holder should be accessible from outside the class but should not be modifiable
    """

    def __init__(self, account_number, account_holder, balance=0):
        self.__account_number = account_number
        self._account_holder = account_holder
        self.__balance = balance

    @property
    def account_holder(self):
        return self._account_holder

    def deposit(self, dep_amt):
        self.__balance += dep_amt
        return f"Added {dep_amt}$ to the account"

    def withdraw(self, wd_amt):
        if self.__balance >= wd_amt:
            self.__balance -= wd_amt
            return "Withdrawal accepted."
        else:
            return "Insufficient funds"

    def check_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account number: {self.__account_number}\nHolder: {self._account_holder}\nBalance: {self.__balance}$"


my_account = BankAccount("123456789", "John First", 1000.0)
print(my_account)
print(my_account.account_holder)

try:
    _ = my_account.account_number
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")

try:
    _ = my_account.balance
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")

try:
    my_account.account_holder = "Jane Doe"
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")

print(my_account.deposit(500.0))
print(my_account.check_balance())
print(my_account.withdraw(250.0))
print(my_account.check_balance())
print(my_account.withdraw(5000.0))
