class BankAccount:
    accounts = []
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print("Balance:", self.balance)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


acct1 = BankAccount(int_rate=0.02, balance=1000)
acct1.deposit(100).deposit(200).deposit(300).withdraw(500).yield_interest()
acct2 = BankAccount(int_rate=0.01, balance=500)
acct2.deposit(50).deposit(100).withdraw(20).withdraw(30).withdraw(40).withdraw(50).yield_interest()
acct3 = BankAccount(int_rate=0.03, balance=2000)


BankAccount.print_all_accounts()