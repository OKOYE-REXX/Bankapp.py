from Account import Account

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02, withdrawal_limit=100):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        self.withdrawal_limit = withdrawal_limit

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest:.2f} applied.")

    def withdrawal(self, amount):
        if amount > self.withdrawal_limit:
            print(f"Withdrawal denied: Savings account limit is ${self.withdrawal_limit}")
            return
        super().withdraw(amount)


print("--- Savings Account ---")
print("--- Withdrawal limit not exceeded ---")
savings = SavingsAccount("REXX", 5000)
print(f"Initial Balance: ${savings.get_balance()}")
savings.withdrawal(100)
savings.apply_interest()

print("") # or print("\n")

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02, withdrawal_limit=100):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        self.withdrawal_limit = withdrawal_limit

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest:.2f} applied.")

    def withdrawal(self, amount):
        if amount > self.withdrawal_limit:
            print(f"$150 Withdrawal denied: Savings account limit is ${self.withdrawal_limit}")
            return
        super().withdraw(amount)


print("--- Savings Account ---")
print("--- Transaction 2 ---")
print("--- Withdrawal limit exceeded ---")
savings = SavingsAccount("REXX", 6000)
print(f"Initial Balance: ${savings.get_balance()}")
savings.withdrawal(150)
savings.apply_interest()