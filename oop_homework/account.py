class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit

    def withdraw(self, amount):
        if amount > self.balance:
            return "Funds Unavailable!"
        else:
            self.balance -= amount


a = Account("Ljuba", 1000)
print(a.balance)
a.withdraw(500)
print(a.balance)
a.deposit(300)
print(a.balance)
print(a.withdraw(1200))
print(a.balance)