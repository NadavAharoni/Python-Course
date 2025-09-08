# Python Classes

---

# What Are Classes?
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
- Special method called when creating a new instance.
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
- **Methods**: Functions defined inside a class.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand  # attribute

    def drive(self):       # method
        print(f"{self.brand} is driving!")
```

---

# Class vs Instance Attributes
- Instance attributes belong to each object.
- Class attributes are shared across all objects.

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
        self._name = value
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
- Boilerplate reduction for classes storing data.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p1 = Point(1, 2)
print(p1)
```

---

# Metaclasses (Advanced)
- Classes **themselves** are instances of a metaclass.
- `type` is the default metaclass.

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass
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

