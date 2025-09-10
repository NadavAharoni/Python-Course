---
marp: true
theme: default
paginate: true
---

# Type Hints and Duck Typing in Python

---

# Introduction to Type Hints

- Type hints help describe the expected types of variables, function arguments, and return values.
- Introduced in **PEP 484**.
- They are **not enforced at runtime**, but can be checked with tools (e.g., `mypy`).

```python
def add(x: int, y: int) -> int:
    return x + y

result: int = add(3, 4)
```

---

# Benefits of Type Hints

- Improve code readability and documentation.
- Help IDEs with autocomplete and error detection.
- Enable static analysis (e.g., `mypy`, `pyright`).
- Useful for large codebases and teamwork.

---

# Basic Type Hints

- Built-in types: `int`, `float`, `str`, `bool`.
- Generic collections: `list`, `dict`, `set`, `tuple`.
- `Optional` for values that may be `None`.

```python
from typing import List, Dict, Optional

names: List[str] = ["Alice", "Bob"]
ages: Dict[str, int] = {"Alice": 30, "Bob": 25}

maybe_age: Optional[int] = None
```

---

# Advanced Type Hints

- `Union`: multiple possible types.
- `Any`: any type allowed.
- `Callable`: function signatures.
- `TypeVar`: generics.

```python
from typing import Union, Any, Callable, TypeVar

T = TypeVar("T")

def stringify(x: Union[int, float, str]) -> str:
    return str(x)

value: Any = 42
```

---

# Advanced Type Hints

```python
from typing import Union, Any, Callable, TypeVar

Fn = Callable[[int, int], int]
def operate(f: Fn, a: int, b: int) -> int:
    return f(a, b)
```


---

# Type Hints and Inheritance

- Use base classes or `Protocol` for duck typing.
- Functions can accept any subclass of the hinted type.

```python
class Animal:
    def speak(self) -> None:
        ...

class Dog(Animal):
    def speak(self) -> None:
        print("Woof!")

def make_speak(animal: Animal) -> None:
    animal.speak()

make_speak(Dog())  # ✅ Works
```

---

# Duck Typing with Protocols

- The `Protocol` class allows structural subtyping.
- Focuses on behavior, not explicit inheritance.

```python
from typing import Protocol

class Quackable(Protocol):
    def quack(self) -> None: ...

class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending!")

def make_it_quack(obj: Quackable):
    obj.quack()

make_it_quack(Duck())
make_it_quack(Person())
```

---

# isinstance Checks

- Sometimes runtime type checking is necessary.
- Use `isinstance` to guard against unexpected types.

```python
def safe_add(x: object, y: object) -> int:
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    raise TypeError("Both arguments must be int")

print(safe_add(3, 4))   # 7
print(safe_add(3, "hi"))  # ❌ raises TypeError
```

---

# Casting in Python?

- Python does not require explicit *upcasting* or *downcasting*.
- Any subclass instance can be used where a base class is expected.
- Downcasting is unsafe — works only if the object is truly a subclass.

```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

animal: Animal = Dog()  # ✅ upcast works
dog: Dog = Animal()     # ❌ invalid downcast
```

---

# Duck Typing

- In Python, behavior matters more than type.
- "If it looks like a duck and quacks like a duck, it’s a duck."

```python
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending!")

def make_it_quack(obj):
    obj.quack()

make_it_quack(Duck())
make_it_quack(Person())
```

---

# Dataclasses with Type Hints

- Dataclasses automatically generate `__init__`, `__repr__`, `__eq__`, and more.
- Type hints define the fields of the dataclass.
- Can enforce immutability with `frozen=True`.

```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str
    active: bool = True

u = User(1, "Alice", "alice@example.com")
print(u)
```

- With `frozen=True`, the instance becomes immutable and hashable:

```python
@dataclass(frozen=True)
class Point:
    x: int
    y: int

p1 = Point(1, 2)
# p1.x = 10  # ❌ Error: frozen dataclass is immutable
```

---

# Summary

- **Type hints** improve readability and enable static checking.
- **Protocols** allow structural typing (duck typing with type hints).
- **isinstance** is still useful for runtime safety checks.
- **Dataclasses** use type hints to define fields and can enforce immutability.
- Python avoids explicit casting — rely on duck typing instead.