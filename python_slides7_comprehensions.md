---
marp: true
paginate: true
theme: default
---

# Python Comprehensions

------------------------------------------------------------------------

## What are Comprehensions?

-   Concise way to create new sequences (lists, sets, dicts).
-   Transform or filter existing iterables.
-   Improve readability compared to `for` loops.

------------------------------------------------------------------------

## List Comprehensions

**Syntax:**

``` python
[expression for item in iterable if condition]
```

**Example:**

``` python
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]          # [1, 4, 9, 16, 25]
evens = [n for n in numbers if n % 2 == 0] # [2, 4]
```

------------------------------------------------------------------------

## Set Comprehensions

-   Same syntax as lists, but with `{ }`.
-   Automatically removes duplicates.

``` python
words = ["apple", "banana", "apple", "cherry"]
unique_lengths = {len(word) for word in words}
# {5, 6}
```

------------------------------------------------------------------------

## Dictionary Comprehensions

**Syntax:**

``` python
{key_expr: value_expr for item in iterable if condition}
```

**Example:**

``` python
numbers = [1, 2, 3, 4]
square_map = {n: n**2 for n in numbers}
# {1: 1, 2: 4, 3: 9, 4: 16}
even_map = {n: n**2 for n in numbers if n % 2 == 0}
# {2: 4, 4: 16}
```

------------------------------------------------------------------------

## Nested Comprehensions

-   Multiple `for` loops inside one comprehension.

**Flatten a matrix:**

``` python
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6]
```

------------------------------------------------------------------------

## Nested Comprehensions (cont.)

**With condition:**

``` python
pairs = [(x, y) for x in [1, 2] for y in [3, 4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 4)]
```

**Dictionary from nested data:**

``` python
matrix = [[1, 2], [3, 4]]
index_map = {(i, j): matrix[i][j]
             for i in range(len(matrix))
             for j in range(len(matrix[i]))}
# {(0, 0): 1, (0, 1): 2, (1, 0): 3, (1, 1): 4}
```

------------------------------------------------------------------------

## Generator Expressions

-   Use `()` instead of `[]`.
-   Lazily evaluated (saves memory).

``` python
gen = (n**2 for n in range(5))
print(next(gen))  # 0
print(next(gen))  # 1
```

------------------------------------------------------------------------

## Pros & Cons

✅ **Pros** - Concise & readable. - Often faster than explicit loops. -
Expresses "map/filter + build collection" clearly.

⚠️ **Cons** - Hard to read if too nested. - Avoid overly complex
comprehensions → use loops.

------------------------------------------------------------------------

# ✅ Summary

-   **List comprehensions** → new lists.
-   **Set comprehensions** → unique elements.
-   **Dict comprehensions** → key-value mappings.
-   **Nested comprehensions** → powerful but keep simple.
-   **Generators** → memory-efficient, lazy evaluation.
