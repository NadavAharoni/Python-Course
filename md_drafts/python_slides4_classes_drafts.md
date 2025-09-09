

---

# Encapsulation & Name Mangling
- Use `_` or `__` to indicate private attributes.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```
