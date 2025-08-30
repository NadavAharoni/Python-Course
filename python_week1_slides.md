---
marp: true
theme: default
paginate: true
---

# Python Programming – Week 1
## Session 1 & 2: Basics, Collections, Pythonic Thinking

**Course Goals**  
- Learn Python syntax & idioms  
- Practice with hands-on coding  
- Use AI tools (CoPilot, ChatGPT) productively  
- Understand and explain code  

---

# Session 1
## Python Basics & Syntax

**Learning Goals**  
- Run Python interactively and via scripts  
- Use variables and dynamic typing  
- Write conditionals and loops  
- Practice with small programs  

---

# Python vs C/C++/C#/Java – Key Differences

- No type declarations (dynamic typing)  
- Indentation defines blocks (no `{}`)  
- Built-in high-level data structures  
- Functions are first-class citizens  
- Batteries included: rich standard library  

---

# Running Python

- **Interactive REPL:** type `python` in terminal  
- **Scripts:** run `python myscript.py`  
- **Notebooks (Jupyter, Colab):** mix code + text  

Try it:  
```python
print("Hello, Python!")
```

---

# Variables & Types

- No type declarations  
- Types are inferred at runtime  

```python
x = 42        # int
y = 3.14      # float
name = "Ana"  # str
flag = True   # bool
z = None      # NoneType
```

---

# Strings & f-strings

```python
name = "Ana"
age = 22
print(f"My name is {name} and I am {age} years old.")
```

- Strings are sequences  
- Indexing: `s[0]`, slicing: `s[1:4]`, reverse: `s[::-1]`

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

while x > 0:
    x -= 1
    print(x)
```

---

# 📝 Exercises (AI encouraged)

1. Write a program that asks for a number and prints whether it is positive, negative, or zero.  
2. Print the squares of numbers 1–10 using a `for` loop.  
3. Extend #2 using a **list comprehension**.  
4. Write a program that keeps asking for input until the user types `"stop"`.  

*Tip: Use CoPilot/ChatGPT to get a draft solution, then explain each line yourself.*

---

# Session 2 (Wed)  
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

# Sets

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)   # union
print(A & B)   # intersection
print(A - B)   # difference
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
