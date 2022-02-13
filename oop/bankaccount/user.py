class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawal(self, amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

        return self

    def transfer_money(self, other_user, amount):
        self.amount -= amount
        other_user.amount += amount

        return self



deborah = User("Deborah", 21)
tom = User("Tom", 25)
jello = User("Jello", 15)


deborah.make_deposit(5000000000).make_deposit(2000).make_deposit(4000).make_withdrawal(2000).display_user_balance()

tom.make_deposit(549).make_deposit(25).make_withdrawal(500).make_withdrawal(1).display_user_balance()

jello.make_deposit(10000).make_withdrawal(1).make_withdrawal(3000).make_withdrawal(409).display_user_balance()

deborah.transfer_money(jello, 50000).display_user_balance()
jello.display_user_balance()




