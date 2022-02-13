class BankAccount:
    accounts= []

    def __init__(self, name, balance, rate):
        self.balance=balance
        self.rate=rate
        self.name=name
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
        #print(f"BankAccount: {self.balance}, {self.name}")
        print("hello.world")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.rate

            return self

church = BankAccount("church", 200, .02)
school = BankAccount("school", 400, .02)

BankAccount.print_all()




church.deposit(200).deposit(200).deposit(200).withdraw(100000).yield_interest().display_account_info()
school.deposit(4000).deposit(4000).withdraw(200).withdraw(500).withdraw(20).withdraw(280).yield_interest().display_account_info()


