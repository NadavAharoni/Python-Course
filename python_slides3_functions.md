---
marp: true
theme: default
paginate: true
---

# Python Functions

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

## Function Arguments in Python
### Arguments can be passed in **two ways**:
- **Positional**: matched by order.  
    ```python
    def greet(name, age):
        print(f"{name} is {age} years old")
    greet("Alice", 20)  # name="Alice", age=20
    ```
- **Keyword (named)**: matched by name.  
    ```python
    greet(age=20, name="Alice")
    ```

---

## Default Arguments
### Functions can have **default values**:
  ```python
  def greet(name, age=18):
      print(f"{name} is {age}")
  greet("Bob")         # uses default age=18
  greet("Alice", 20)   # overrides default
  ```

⚠️ Be careful: default values are evaluated **once**, at definition time!  
```python
def add_item(item, container=[]):  # risky!
    container.append(item)
    return container
```

---

## Variable-Length Arguments
### Collect extra positional arguments with `*args`:
  ```python
  def add_all(*numbers):
      return sum(numbers)
  add_all(1, 2, 3, 4)  # 10
  ```

### Collect extra keyword arguments with `**kwargs`:
  ```python
  def show_info(**data):
      for key, value in data.items():
          print(key, value)
  show_info(name="Alice", age=20)
  ```

---

## Argument Ordering Rules
Python enforces a strict order when defining parameters:

```
def func(pos_only, /, pos_or_kwd, *, kwd_only):
    ...
```

1. **Positional-only** (`/`)  
2. **Positional-or-keyword** (default)  
3. **Keyword-only** (`*`)  

---
## Argument Ordering Rules
Python enforces a strict order when defining parameters:

```
def func(pos_only, /, pos_or_kwd, *, kwd_only):
    ...
```
Example:
```python
def f(a, b, /, c, *, d):
    print(a, b, c, d)

f(1, 2, 3, d=4)  # ✅
f(1, 2, c=3, d=4)  # ✅ c can be positional or keyword
f(a=1, b=2, c=3, d=4)  # ❌ a, b are positional-only
```

---

## Functions as First-Class Objects
- Functions can be **assigned to variables**, **passed as arguments**, and **returned from other functions**.

```python
def square(x):
    return x * x

def twice(x):
    return x + x

def apply(func, value):
    return func(value)

print(apply(square, 5))  # 25
print(apply(twice, 5))  # 10
```

---

## Defining Functions Inside Functions
### Functions can be **nested**:

```python
  def outer(x):
      def inner(y):
          return x + y
      return inner

adder5 = outer(5)
print(adder5(10))  # 15
```


### Useful for **closures** and limiting scope.

---
## Closures
- ### A **closure** is a function that "remembers" variables from its enclosing scope, even after that scope has finished executing.
- ### Inner functions are useful for creating closures because they capture values from the outer function.
 
---
## Closures

Another example:
```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor  # factor is remembered!
    return multiply

times3 = make_multiplier(3)
print(times3(10))  # 30
```
Here, `times3` remembers the value of `factor=3` even though `make_multiplier` has finished running.

---

## Lambda Functions
- Anonymous, single-expression functions:
  ```python
  double = lambda x: x * 2
  print(double(4))  # 8
  ```

- Often used with `map`, `filter`, `sorted`:
  ```python
  nums = [1, 2, 3, 4]
  print(list(map(lambda x: x**2, nums)))
  ```

---

## The `map` Function
### Applies a function to each item in an iterable:
  ```python
  nums = [1, 2, 3, 4]
  squared = map(lambda x: x**2, nums)
  print(list(squared))  # [1, 4, 9, 16]
  # note that map returns an iterator therefore we must convert it
  # to a list (in the line above) before we can print it
  ```

### Equivalent to a loop:
  ```python
  result = []
  for n in nums:
      result.append(n**2)
  ```

### Often combined with `lambda` for concise code.

---

## Summary
- Python supports flexible function signatures:
  - Positional, keyword, default, `*args`, `**kwargs`
  - Positional-only (`/`) and keyword-only (`*`) arguments
- Functions are **first-class objects**
- You can define **functions inside functions**
- **Closures** allow functions to "remember" variables from their context
- **Lambdas** provide short anonymous functions
- `map` applies a function to all items in a sequence
