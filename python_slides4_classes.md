---
marp: true
theme: default
paginate: true
---

# Python Classes
- Python supports object-oriented programming.
- Define classes with the `class` keyword.

---

# Classes
- A **class** is a blueprint for creating objects.
- Defines attributes (data) and methods (behavior).
- Objects created from a class are called **instances**.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy")
my_dog.bark()
```

---

# The `__init__` Method
- Special method called when creating a new instance (constructor in other languages).
- Often used to initialize attributes.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
print(p.x, p.y)
```

---

# Attributes and Methods
- **Attributes**: Variables bound to an object.
  - Attributes must be refered to by `self.<attribute_name>`
- **Methods**: Functions defined inside a class.
  - The first argument of each (instance) must be `self`.
- Unlike other languages in which `this` is implicit.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand  # attribute

    def drive(self):       # method
        print(f"{self.brand} is driving!")
```


---

# Attributes are dynamic

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        # new attributes can be added dynamically
        self.barked = True
        print(f"{self.name} says Hau Hau!")

my_dog = Dog("Buddy")
my_dog.bark()
# new attributes can be added dynamically outside
# the class definition
my_dog.hair_color = "Brown"
# attributes can be deleted
del my_dog.hair_color # deleting dynamic attribute
del my_dog.name  # deleting regular attribute
```

---
# Methods are also dynamic

```python
def multiply_value(self, factor):
    self.value *= factor
    # print("This is a dynamically added method.")

class MyClass:
    def __init__(self, value):
        self.value = value

MyClass.multiply_value = multiply_value

obj = MyClass(10)
obj.multiply_value(5)
print(obj.value)
```

---

# Class vs Instance Attributes
- Instance attributes belong to each object.
- Class attributes are shared across all objects (similar, but not identical to `static` in other languages).

```python
class Circle:
    pi = 3.14159   # class attribute

    def __init__(self, r):
        self.r = r # instance attribute

c1 = Circle(1)
c2 = Circle(2)
print(c1.pi, c2.pi)
```

---

# Special Methods (Dunder Methods)
- Double underscore methods customize class behavior.
- Examples: `__str__`, `__len__`, `__add__`

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title} ({self.pages} pages)"

b = Book("Python 101", 200)
print(b)
```

---

# Inheritance
- A class can inherit attributes/methods from another class.

```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

d = Dog()
d.speak()
```

---

# Multiple Inheritance
- A class can inherit from multiple parents.

```python
class A:
    def hello(self):
        print("Hello from A")

class B:
    def hello(self):
        print("Hello from B")

class C(A, B):
    pass

c = C()
c.hello()  # Which hello is called?
```

---

# Method Resolution Order (MRO)
- Python follows **MRO** to decide which method to call.
- Check using `.mro()`

```python
print(C.mro())
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
```

---

# The `super()` method

- `super()` allows a class to **call methods from its parent class**.
- Useful for **extending behavior** without rewriting parent methods.
- Particularly important in **multiple inheritance**.

```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        super().speak()  # call parent method
        print("Woof!")

d = Dog()
d.speak()
```

Output:
```
Some sound
Woof!
```

---

# Using `super()`

- Ensures **parent class methods are properly called**.
- Avoids hardcoding the parent class name, which improves **maintainability**.
- Works well with **cooperative multiple inheritance**.

```python
class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        print("Hello from B")
        super().hello()
```

---

# Using `super()`
```python
b = B()
b.hello()
```

Output:
```
Hello from B
Hello from A
```

---

# `super()` with Multiple Inheritance

```python
class A:
    def greet(self):
        print("A greet")

class B(A):
    def greet(self):
        print("B greet")
        super().greet()

class C(A):
    def greet(self):
        print("C greet")
        super().greet()

class D(B, C):
    def greet(self):
        print("D greet")
        super().greet()
```

---

# `super()` with Multiple Inheritance

- Output follows the **Method Resolution Order (MRO)**:

``` python
d = D()
d.greet()
```

- Output:
```
D greet
B greet
C greet
A greet
```

- `super()` ensures methods are called in **MRO order**, not just the direct parent.

---

# Summary

- `super()` is used to **call parent class methods**.
- Avoids hardcoding parent class names, improving maintainability.
- Works seamlessly with **multiple inheritance** and Python’s **MRO**.
- Recommended to use `super()` in all new-style classes (Python 3+).

---
# Encapsulation & Name Mangling (1)
- Attributes that start with a single underscore are by convention "protected".
- The underscore prefix indicates that the attributed should not be accessed outside the class.
- This is not enforced by the Python interpreter.

---
# Encapsulation & Name Mangling (2)
- Attributes that start with two underscore are "name mangled", and considered "private"

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

---

# Encapsulation & Name Mangling (3)

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

If an attribute with double underscore is accessed from outside the class, an AttributeError is raised.
```python
# print(account.__balance) # raises an AttributeError
```

---
# Encapsulation & Name Mangling (4)

But if an attribute with double underscore is assigned outside the class, a new dynamic attribute with that name is created(!)

The original (so called private) attribute remains unchanged.

This could be pretty confusing...

```python
# The following line creates a new dynamic attribute(!)
account.__balance = 1000
print(account.__balance)  # prints 1000

print(account.get_balance())  # still prints 150
```

---

# Encapsulation & Name Mangling (5)

```python
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
```

---
# Class Methods and Static Methods
- **@classmethod**: Receives class as first argument.
- **@staticmethod**: Does not receive class or instance.

```python
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def greet():
        print("Hello!")
```
---

# Class Methods and Static Methods

```python
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def greet():
        print("Hello!")
        # count += 1 
        # ^ This will raise an error because 'count' is not defined in this scope
```

---

# Properties
- Use `@property` for controlled attribute access.

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        if len(value) < 2:
            raise ValueError("Name must be at least 2 characters long")
        self._name = value
```
---

# Properties

- Example usage

```python
p = Person("Alice")
print(p.name)  # Accessing the property
p.name = "Bob"  # Using the setter
print(p.name)
# p.name = "Bo"  # This will raise a ValueError
```

See: https://www.geeksforgeeks.org/python/python-property-decorator-property/

---

# Properties
- The "backing attribute" can have any name
- It is a common practice to use `_<name>`

```python
class Person:
    def __init__(self, name):
        self._n = name

    @property
    def name(self):
        return self._n

    @name.setter
    def name(self, value):
        if not value or len(value) < 2:
            raise ValueError("Name must be at least 2 characters long")
        self._n = value
```

---

# Properties
- Can also define a "deleter"

```python
class Person:
    def __init__(self, name):
        self._n = name

    @property
    def name(self):
        return self._n

    @name.setter
    def name(self, value):
        # removed check for brevity
        self._n = value

    @name.deleter
    def name(self):
       del self.__n

```


---

# Abstract Base Classes (ABC)
- Define abstract methods that subclasses must implement.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
```

---

# Dataclasses
- Reduce boilerplate for classes mainly used to store data.
- Automatically adds `__init__`, `__repr__`, `__eq__`, and more.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1)        # Point(x=1, y=2)
print(p1 == p2)  # True
```

---

### Features
- Default values and type hints.
- `frozen=True` makes instances immutable.
- `order=True` adds comparison operators.

```python
@dataclass(order=True, frozen=True)
class Student:
    id: int
    name: str
```

---

### Real-World Example
```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    username: str
    email: str
    is_active: bool = True

user1 = User(1, "nadav", "nadav@example.com")
print(user1)
```


---

# Inner Classes
- Classes can be defined inside other classes.
- Often used for logical grouping or helper structures.

```python
class Outer:
    class Inner:
        def greet(self):
            print("Hello from Inner class")

outer = Outer()
inner = Outer.Inner()
inner.greet()
```

### Use Cases
- Represent objects tightly coupled with the outer class.
- Hide implementation details.

### Real-World Example
```python
class Database:
    class Connection:
        def __init__(self, host):
            self.host = host

        def connect(self):
            print(f"Connecting to {self.host}")

# Usage
conn = Database.Connection("localhost")
conn.connect()
```

---

# Summary
- Classes define structure & behavior.
- Attributes: instance vs class.
- Special methods (`__str__`, etc.).
- Inheritance, MRO.
- Encapsulation, properties.
- Class & static methods.
- ABCs, dataclasses, metaclasses.
- Inner classes for logical grouping.

