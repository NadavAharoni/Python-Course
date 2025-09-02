---
marp: true
theme: default
paginate: true

---
# Python

---
# The Python Language
- Easy to learn and readable – relatively simple syntax
- Interpreted
- Multi-paradigm:
    - supports multiple programming styles, including object-oriented, procedural, and functional programming.
- Dynamically typed
- Garbage collected
- Batteries included: rich standard library

---
# The Python Language
## Extensible and embeddable:
- Python code can be extended with modules written in other languages, like C or C++, to optimize performance.
- It can also be embedded in other applications to provide scripting functionality

---
# The Python Language
## Community and ecosystem attributes
- Free and open-source: Python is freely available to use, modify, and distribute, even for commercial purposes.
- Large community support
- Rich ecosystem of third-party libraries (beyond the standard library)
    - The Python Package Index (PyPI) contains thousands of third-party packages:
        - web development (Django, Flask)
        - data science (NumPy, Pandas)
        - machine learning (TensorFlow, PyTorch)

---
# Python vs C/C++/C#/Java – Key Differences
- No type declarations (dynamic typing)  
- Indentation defines blocks (no `{}`)  
- Built-in high-level data structures  
- Functions are first-class citizens  

---
# Running Python
- **Interactive REPL (Read–Eval–Print Loop):**  
    - run `python` in terminal
- **Scripts:**
    - run `python myscript.py`  
- **Notebooks (Jupyter, Colab):**
    - mix code + text  

---
# Running Python - Interactive REPL  
## Example:

``` shell
python <enter>
```
<br>

```
>>> 2 + 3
5
>>> "hi".upper()
'HI'
```

---
# Variables & Types

- No type declarations  
- Types are inferred at runtime

```python
x = 42        # int
y = 3.14      # float
name = "Ana"  # string
flag = True   # bool
z = None      # NoneType

# type function returns type of a variable
print(type(name))
```

---
# Converting between string and other types
## Number to string

```python
y = 3.14      # float
y_str = str(y)
```

## String to number

```python
y2 = float(y_str)
```
Can throw an exception!

---
# The print function
```python
print(2+3)
print("2" + str(3))
print("Hello", "World")  # prints with a space
```

---
# Lists

A list is defined by `value_list = [val1, val2, ...]`  
0 indexed. Negative indices start from the end.  
Slicing: `[start:end]` end is not included.

```python
nums = [10, 20, 30]
nums.append(40)
nums[1] = 25

print(nums[0])     # first item
print(nums[-1])    # last item
print(nums[1:2])   # slice with one element

list1 = [1, 2]
list2 = [3, 4]
new_list = list1 + list2   # new_list is now [1, 2, 3, 4]
```

---
# Lists can contain any type

## Lists can be heterogeneous
```python
a_list = [1, 2, "hello"]
```
## Lists can contain lists

```python
list1 = [1, 2]
list2 = [3, 4]
list1.append(list2)
list1.append(list2)
print(list1)
```

---
# Lists variables are references

```python
list1 = [1, 2]
list2 = [3, 4]
list1.append(list2)
list1.append(list2)
print(list1)
list2.append(5)
print(list1)
```

---
# Strings

Strings can be concatenated.
```python
s1 = "hello"
s2 = "world"
s3 = s1 + s2

message = "Python is "
message2 = message
message += "awesome!"
print(message)
print(message2)
```

---
# Strings

There is a rich set of string methods:  
https://docs.python.org/3/library/stdtypes.html#string-methods

```python
s1 = "  hello, world  "
print(s1.split(" "))
print(s1.strip().split(" "))
```

---
# Join

## str.join(list)

list can be any "iterable" – will be explained later

```python
words = ["Hello", "world", "this", "is", "Python"]
sentence1 = " ".join(words)
print(sentence1)

sentence2 = ",".join(words)
print(sentence2)
```

---
# F-Strings

**f-strings = formatted string literals**  
- Introduced in Python 3.6  
- Prefix string with `f` or `F`  
- Place expressions inside `{}` which are evaluated at runtime  

---
# F-strings example
```python
name = "Ana"
age = 22
print(f"My name is {name} and I am {age} years old.")
print(f"My age next year will be: {age + 1}")
```

Output:  
```
My name is Ana and I am 22 years old.
My age next year will be: 23
```

---
# Strings as Sequences

- Strings behave like sequences of characters  
- **Indexing**: `s[i]` → returns the i-th character (0-based)  
- **Slicing**: `s[start:end]` → substring from start (inclusive) to end (exclusive)  
- **Step**: `s[start:end:step]` → take every `step` characters  
- **Reverse**: `s[::-1]` → entire string, step = -1  

---
# String indexing/slicing/step/reverse

Example:  
```python
s = "python"
print(s[0])     # 'p'
print(s[1:4])   # 'yth'
print(s[::2])   # 'pto'
print(s[::-1])  # 'nohtyp'
print(s[-2:])   # 'on'
```

---
# Conditionals

```python
x = 7
if x > 10:
    print("big")
elif x > 5:
    print("medium")
else:
    print("small")
```

---
# Loops

```python
# range will be explained later
for i in range(5):
    print(i)

names = ["Ana", "Bo", "Cai"]
for name in names:
    print(name)

x = 3
while x > 0:
    x -= 1
    print(x)   # prints 2, 1, 0
```

---
# 📝 Exercises

1. Write a program that asks for a number and prints whether it is positive, negative, or zero.  
2. Print the squares of numbers 1–10 using a `for` loop.  
3. Extend #2 using a **list comprehension**.  
4. Write a program that keeps asking for input until the user types `"stop"`.  
   - Hint: use `while True:` and `break`.

*Tip: Use CoPilot/ChatGPT to get a draft solution, then explain each line yourself.*

---
# List Comprehensions

- A concise way to create lists  
- Syntax:  
  ```python
  [expression for item in iterable if condition]
  ```

---
# List Comprehensions Examples
## Squares of numbers 0–9
```python
squares = [x**2 for x in range(10)]
```

## Even numbers
```python
evens = [x for x in range(10) if x % 2 == 0]
```

## First letters of names
```python
names = ["Ana", "Bo", "Cai"]
first_letters = [name[0] for name in names]
```

---
# Tuples

```python
point = (3, 4)   # tuple (immutable)
point3d = (2, 3, 4)
tuple1 = (3, )
```

- Lists = mutable sequences  
- Tuples = immutable sequences  

---
# Sets

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)   # union
print(A & B)   # intersection
print(A - B)   # difference

empty_set = set()   # {} creates an empty dict, not a set!
```

- Unique elements, no duplicates  
- Great for membership tests  

---
# Dictionaries

```python
grades = {"Ana": 95, "Bo": 82}
grades["Cai"] = 90

for name, grade in grades.items():
    print(name, grade)
```

- Key–value pairs  
- Fast lookups  
- Iterating over a dict yields keys by default

---
# Iteration Helpers

```python
names = ["Ana", "Bo", "Cai"]

for i, name in enumerate(names):
    print(i, name)

nums = [1, 2, 3]
squares = [n**2 for n in nums]
```

- `enumerate`, `zip`, `.items()`  
- Comprehensions for concise code  

---
# Built-in Functions

- `len`, `sum`, `min`, `max`, `sorted`  
- `any`, `all`  

Example:  
```python
nums = [1, -2, 3, -4]
print(any(n < 0 for n in nums))   # True
```

---
# Using libraries
## Use import to import a library

```python
import sys

for line in sys.stdin:
    s = line.strip()
    if s == "":              # Skip empty lines
        continue
    print(line)
```
---
# Using libraries

## Large list of standard libraries:
https://docs.python.org/3/library/index.html

## Examples:
math, os, sys, csv

---
# Functions

- Functions allow us to reuse code and organize programs.
- Defined with the `def` keyword.

```python
def greet(name):
    print(f"Hello {name}!")

greet("Ana")
greet("Bo")
```

- Functions can return values:

```python
def square(x):
    return x * x

print(square(5))   # 25
```

---
# Exceptions

- Errors in Python raise **exceptions**.
- Use `try`/`except` to handle them.

```python
try:
    num = int("abc")  # invalid conversion
except ValueError as e:
    print("That was not a number:", e)
```

- `finally` block always runs:

```python
try:
    f = open("file.txt")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Done trying")
```

---
# Classes

- Python supports object-oriented programming.
- Define classes with the `class` keyword.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

p = Person("Ana", 22)
p.greet()
```

- Classes bundle **data (attributes)** and **behavior (methods)** together.

---
# 📝 Exercises

1. Create a list of numbers 1–20.  
   - Print only even numbers.  
   - Print their squares using a list comprehension.  

2. Count the frequency of each character in `"hello world"`.  
   - Compare your solution with `collections.Counter`.  

3. Given two lists, find all common elements without duplicates.  
   - Solve once with loops, once with sets.  

---
# 📝 Exercises (contd.)

4. Write a program that maps each name in a list to its length using a dict comprehension.  

5. Challenge: write `is_palindrome(word)` using slicing.  
