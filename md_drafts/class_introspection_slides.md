# Class Introspection in Python

---

# What is Introspection?

- **Introspection**: examining objects at runtime to discover attributes, methods, and type.
- Useful for:
  - Debugging
  - Dynamic programming
  - Frameworks (e.g., Django, SQLAlchemy)
  - Testing, serialization, and IDE support

---

# Built-in Functions for Introspection

- `type(obj)` → returns the type (class) of an object.
- `isinstance(obj, cls)` → check if object is instance of class.
- `issubclass(cls, parent)` → check class inheritance.
- `id(obj)` → returns the identity (memory address) of the object.

```python
class Animal:
    pass

dog = Animal()
print(type(dog))          # <class '__main__.Animal'>
print(isinstance(dog, Animal))  # True
print(issubclass(Animal, object))  # True
```

---

# Inspecting Attributes

- `dir(obj)` → lists all attributes and methods.
- `vars(obj)` or `obj.__dict__` → dictionary of instance attributes.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof")

d = Dog("Buddy")
print(dir(d))       # ['__class__', '__delattr__', ..., 'bark', 'name']
print(vars(d))      # {'name': 'Buddy'}
```

---

# Using the `inspect` Module

- The `inspect` module provides detailed introspection capabilities.
- Common functions:
  - `inspect.getmembers(obj)` → all members (attributes/methods)
  - `inspect.isfunction(obj)`, `inspect.ismethod(obj)`, `inspect.isclass(obj)`

```python
import inspect

class Cat:
    def meow(self):
        pass

print(inspect.getmembers(Cat, predicate=inspect.isfunction))
# [('meow', <function Cat.meow at 0x...>)]
```

---

# Real-world Use Cases

- **Testing frameworks**: discover test methods dynamically.
- **ORMs**: map class attributes to database columns.
- **Serialization libraries**: automatically serialize object attributes.
- **IDEs**: provide autocomplete suggestions using introspection.

---

# Summary

- Python allows runtime examination of objects and classes.
- Use `type`, `isinstance`, `issubclass`, `dir`, `vars` for basic introspection.
- The `inspect` module provides advanced tools.
- Introspection is widely used in testing, frameworks, and dynamic code.
- Enhances flexibility and reduces boilerplate in Python programs.