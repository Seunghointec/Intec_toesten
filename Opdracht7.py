class BankAccount:

    def __init__(self, name):
        self.balance = 0
        self.owner = name

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def getBalance(self):
        return self.balance


account = BankAccount('Alex')
account.owner(account)
account.deposit(10)
account.withdraw(3)
account.getBalance()
