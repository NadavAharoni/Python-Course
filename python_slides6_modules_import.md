---
marp: true
theme: default
paginate: true
---


# Python Modules and Importing

---

# What is a Module?
- A **module** is a Python file containing functions, classes, or variables.
- Allows **code reuse** and organization.
- Can be a **single `.py` file** or a **package** (folder with `__init__.py`).

```python
# mymodule.py
PI = 3.14

def greet(name):
    print(f"Hello, {name}!")
```

---

# Importing Modules

- **Import the entire module**
```python
import mymodule
print(mymodule.PI)
mymodule.greet("Alice")
```

- **Import specific items**
```python
from mymodule import PI, greet
print(PI)
greet("Bob")
```

- **Import with alias**
```python
import mymodule as mm
print(mm.PI)
mm.greet("Charlie")
```

---

# Packages

- A **package** is a directory containing multiple modules.
- Must include an `__init__.py` file (can be empty).

```
mypackage/
├── __init__.py
├── module1.py
└── module2.py
```

- Import from packages:
```python
from mypackage import module1
module1.some_function()
```

---

# The `__name__ == "__main__"` Idiom

- Allows a file to be used **as a script or as a module**.

```python
# myscript.py
def main():
    print("This is the main program")

if __name__ == "__main__":
    main()
```

- When run directly: `python myscript.py` → executes `main()`.
- When imported: `import myscript` → `main()` does NOT run.

---

# Exploring Modules

- **Check available attributes/functions:** `dir(module)`
- **Get documentation:** `help(module)`
- **Module file location:** `module.__file__`

```python
import math
print(dir(math))
print(help(math.sqrt))
print(math.__file__)
```

---

# Common Standard Library Modules

- `os` → operating system functions
- `sys` → system-specific parameters and functions
- `math` → mathematical functions
- `random` → random number generation
- `datetime` → dates and times
- `json` → read/write JSON files
- `csv` → read/write CSV files

---

# Example: Combining Modules

- File structure:
```
project/
├── main.py
└── utils.py
```

```python
# utils.py
def add(x, y):
    return x + y

# main.py
import utils
print(utils.add(3, 4))
```

---

# Summary

- **Modules**: Python files for reusable code.
- **Packages**: directories containing modules.
- **Importing**: `import`, `from ... import ...`, aliasing.
- **`__name__ == '__main__'`**: run code only when script executed directly.
- Use **standard library** modules to extend functionality quickly.

