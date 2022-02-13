class BankAccount:
    accounts= []

    def __init__(self, balance, rate):
        self.balance=balance
        self.rate=rate
        BankAccount.accounts.append(self)
    @classmethod
    def print_all(cls):
        for account in BankAccount.accounts:
            account.display_account_info()

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if  self.balance - amount >=0 :
            self.balance -= amount
        else:
            print(f"Insufficient funds: Charging a 5 fee")
            self.balance -= 5
            
        return self
        
    def display_account_info(self):
        return f"is power {self.balance}"

    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.rate

            return self

# church = BankAccount("church", 200, .02)
# school = BankAccount("school", 400, .02)

# BankAccount.print_all()




# church.deposit(200).deposit(200).deposit(200).withdraw(100000).yield_interest().display_account_info()
# school.deposit(4000).deposit(4000).withdraw(200).withdraw(500).withdraw(20).withdraw(280).yield_interest().display_account_info()


class User:
    def __init__(self, name):
        self.name=name
        self.account=BankAccount(4000, .02)

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self,amount):
        self.account.withdrawal(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name} Balance: {self.account.display_account_info()}")
        
        return self

deborah= User("Deborah/")

deborah.make_deposit(100)
deborah.display_user_balance()