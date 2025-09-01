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
- **Interactive REPL (Read–Eval–Print Loop)**: **
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
- Variables are names bound to objects

```python
x = 42        # int
y = 3.14      # float
name = "Ana"  # string
flag = True   # bool
z = None      # NoneType
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
```

---
# Strings & f-strings

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

*Tip: Use CoPilot/ChatGPT to get a draft solution, then explain each line yourself.*

---
# Session 2
## Collections & Pythonic Programming

**Learning Goals**  
- Work with lists, tuples, sets, dictionaries  
- Use slicing, comprehensions, and iteration helpers  
- Solve problems in a Pythonic way  

---
# Lists & Tuples

```python
nums = [10, 20, 30]
nums.append(40)
nums[1] = 25

point = (3, 4)   # tuple (immutable)
```

- Lists = mutable sequences  
- Tuples = immutable sequences  

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
# 📝 Exercises (AI encouraged)

1. Create a list of numbers 1–20.  
   - Print only even numbers.  
   - Print their squares using a list comprehension.  

2. Count the frequency of each character in `"hello world"`.  
   - Compare your solution with `collections.Counter`.  

3. Given two lists, find all common elements without duplicates.  
   - Solve once with loops, once with sets.  

4. Write a program that maps each name in a list to its length using a dict comprehension.  

5. Challenge: write `is_palindrome(word)` using slicing.  

---
# Wrap-Up (Week 1)

- Python syntax is simple & concise  
- Collections are the foundation of Python  
- **AI is your coding assistant**:  
  - Use it for boilerplate or brainstorming  
  - But *you* must understand the code  
