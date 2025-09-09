
---

# Metaclasses (Advanced)
- A **metaclass** defines how classes are created.
- Default metaclass is `type`.
- Useful for enforcing rules, auto-registering classes, or modifying definitions.

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

# Output: Creating class MyClass
```

### Key Idea
- Instances are created from classes.
- Classes are created from **metaclasses**.

### Real-World Example
- Enforcing class naming conventions:

```python
class NameCheckMeta(type):
    def __new__(cls, name, bases, dct):
        if not name[0].isupper():
            raise TypeError("Class name must start with uppercase!")
        return super().__new__(cls, name, bases, dct)

class goodClass(metaclass=NameCheckMeta):
    pass  # ❌ will raise TypeError

class GoodClass(metaclass=NameCheckMeta):
    pass  # ✅ works fine
```
