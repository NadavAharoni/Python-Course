class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
account = BankAccount(150)
print(account.get_balance())

# print(account.__balance)

account.__balance = 1000
print(account.__balance)
print(account.get_balance())
print(account._BankAccount__balance)


