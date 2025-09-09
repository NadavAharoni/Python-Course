---
marp: true
theme: default
paginate: true
---


# Python Dunder (Magic) Methods

---

# What Are Dunder Methods?
- Special methods with double underscores (e.g., `__str__`).
- Define how objects behave with built-in operations.
- Allow customization of printing, comparison, arithmetic, iteration, etc.
- Called *implicitly* by Python, but can be called directly too.

---

# Object Representation: `__repr__` vs `__str__`
- `__repr__`: Unambiguous representation for developers.
- `__str__`: Readable representation for users.

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __repr__(self):
        return f"Book({self.title!r}, {self.pages})"

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

b = Book("Python 101", 200)
print(repr(b))  # Book('Python 101', 200)
print(str(b))   # Python 101 (200 pages)
```

---

# Comparison Methods (1)
- Define custom equality and ordering.
- Common methods: `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)
```

---

# Comparison Methods (2)

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(0, 5)
print(p1 == p2)  # True
print(p3 < p1)   # True
```

---

# Hashing: `__hash__`
- Needed when objects are used as keys in dictionaries or in sets.
- Should be consistent with `__eq__`.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # True
print({p1, p2})  # Only one element
```

---

# Arithmetic Overloading (1)
- Redefine operators for custom classes.
- Examples: `__add__`, `__sub__`, `__mul__`, `__truediv__`.

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
```

---


# Arithmetic Overloading (2)

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)   # Vector(4, 6)
print(v1 * 3)    # Vector(3, 6)
```


---


# Container Methods
- Make objects behave like sequences or mappings.
- `__len__`, `__getitem__`, `__setitem__`, `__delitem__`.

```python
class ShoppingCart:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

cart = ShoppingCart()
cart.items.append("apple")
cart.items.append("banana")
print(len(cart))      # 2
print(cart[0])        # apple
```

---

# Iteration: `__iter__` and `__next__`
- Define custom iteration.
- `__iter__` returns an iterator.
- `__next__` defines how to get next item.

```python
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for num in Countdown(3):
    print(num)
# 3, 2, 1
```

---

# Callable Objects: `__call__`
- Makes an object behave like a function.

```python
class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self, greeting):
        return f"{greeting}, {self.name}!"

g = Greeter("Alice")
print(g("Hello"))  # Hello, Alice!
```

---

# Context Managers: `__enter__` and `__exit__`
- Used in `with` statements.
- Useful for resource management.

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager("test.txt", "w") as f:
    f.write("Hello")
```

---

# Object Lifecycle
- `__new__`: Controls object creation (rarely used).
- `__del__`: Called when object is about to be destroyed.

```python
class Demo:
    def __new__(cls, *args, **kwargs):
        print("Creating instance")
        return super().__new__(cls)

    def __del__(self):
        print("Instance destroyed")

obj = Demo()
del obj
```

---

# Summary
- Dunder methods let objects integrate with Python’s built-in operations.
- Categories:
  - Representation (`__str__`, `__repr__`)
  - Comparison & hashing (`__eq__`, `__lt__`, `__hash__`)
  - Arithmetic (`__add__`, `__mul__`)
  - Containers & iteration (`__len__`, `__getitem__`, `__iter__`)
  - Callable objects (`__call__`)
  - Context managers (`__enter__`, `__exit__`)
  - Lifecycle (`__new__`, `__del__`)

