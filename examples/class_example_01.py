class Dog:
    def __init__(self, name):
        self.name = name
        self._protected_str = "This is protected"
        self.__private_str = "This is private"

    def bark(self):
        # new attributes can be added dynamically
        self.barked = True
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy")
my_dog.bark()
my_dog.hair_color = "Brown"
del my_dog.hair_color # deleting dynamic attribute
del my_dog.name  # deleting regular attribute

# In python, private attributes are not truly private.
# A single underscore prefix is a convention to # indicate
# that an attribute is protected (should not be accessed directly
# outside the class).
# Attribute with double underscore is "name mangled" to be
# __ClassName__attribute.
# If an attribute with double underscore is
# accessed from outside the class, an AttributeError is raised.
# print(my_dog.__private_str)  # This will raise an AttributeError

# But if an attribute with double underscore is assigned outside
# the class, a new dynamic attribute with that name is created(!)
# and the original (so called private) attribute remains unchanged.
# This could be pretty confusing...
# The following line creates a new dynamic attribute(!)
my_dog.__private_str = "Hi"
print(my_dog.__private_str)

# The original private attribute is still there and can be accessed
# using the "mangled" name
print(my_dog._Dog__private_str)

# The protected attribute can be accessed directly, but
# it is discouraged by convention
print(my_dog._protected_str)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
print(account.get_balance()) # ok

# If an attribute with double underscore is
# accessed from outside the class, an AttributeError is raised.
# print(account.__balance)

# But if an attribute with double underscore is assigned outside
# the class, a new dynamic attribute with that name is created(!)
# and the original (so called private) attribute remains unchanged.
# This could be pretty confusing...
# The following line creates a new dynamic attribute(!)
account.__balance = 1000
print(account.__balance)  # prints 1000
print(account.get_balance())  # still prints 150    
# The original private attribute is still there and can be accessed
# using the "mangled" name
print(account._BankAccount__balance)  # prints 150(!)
# The mangled name can also be assigned
# which will change the original private attribute
account._BankAccount__balance = 200
print(account.get_balance())  # prints 200


