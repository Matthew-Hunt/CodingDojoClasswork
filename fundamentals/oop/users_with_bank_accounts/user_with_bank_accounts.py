from bank_account import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}

    def create_account(self, account_name, int_rate=0.01, balance=0):
        self.accounts[account_name] = BankAccount(int_rate, balance)
        return self

    def make_deposit(self, account_name, amount):
        self.accounts[account_name].deposit(amount)
        return self

    def make_withdrawal(self, account_name, amount):
        self.accounts[account_name].withdraw(amount)
        return self

    def display_user_balance(self):
        for account_name, account in self.accounts.items():
            print(f"{self.name}'s {account_name} account balance: ${account.balance}")
        return self

    def transfer_money(self, amount, other_user, from_account, to_account):
        self.accounts[from_account].withdraw(amount)
        other_user.accounts[to_account].deposit(amount)
        return self


john = User("John", "john@example.com")
jane = User("Jane", "jane@example.com")

john.create_account("checking", 0.01, 1000)
john.create_account("savings", 0.02, 5000)
jane.create_account("savings", 0.02, 2000)

john.make_deposit("checking", 100)
john.make_withdrawal("savings", 500)

jane.make_deposit("savings", 100)

john.display_user_balance()
jane.display_user_balance()

john.transfer_money(200, jane, "checking", "savings")

john.display_user_balance()
jane.display_user_balance()