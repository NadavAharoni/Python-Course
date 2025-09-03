---
marp: true
theme: default
paginate: true
---

# Python I/O: `sys.stdin` and File Reading

---

## `sys.stdin`

- `sys.stdin` is a **file-like object** in Python.
- It represents the **standard input stream** (keyboard or redirected input).
- Import it from the `sys` module:

```python
import sys

for line in sys.stdin:
    print("You entered:", line.strip())
```

- Reads until **EOF** (End of File).

---

## Using `sys.stdin` Interactively

- In an **interactive session** (running `python` in Windows CMD/PowerShell):
  - `sys.stdin` waits for user input.
  - Input is typed line by line, pressing <kbd>Enter</kbd>.
  - To stop, press:
    - <kbd>Ctrl+Z</kbd> + <kbd>Enter</kbd> (Windows)

Example:

```python
import sys
for line in sys.stdin:
    print("Got:", line.strip())
```

👉 Program pauses until you type something.

---

## Using `sys.stdin` in a Script

- When running a script, input can be **redirected from a file**:

**CMD example:**
```bat
python script.py < input.txt
```

**PowerShell example:**
```powershell
python script.py < input.txt
```

- In this case:
  - `sys.stdin` reads from `input.txt`.
  - Script processes all lines automatically.

---

## Using `sys.stdin` with Pipes

- You can also connect programs with a pipe (`|`):

**CMD:**
```bat
type input.txt | python script.py
```

**PowerShell:**
```powershell
Get-Content input.txt | python script.py
```

- `sys.stdin` reads from the previous program’s output.

---

## Key Difference: Interactive vs Script

| Mode        | Source of Input           | End Condition  |
|-------------|---------------------------|----------------|
| Interactive | Keyboard (typed by user) | User sends EOF |
| Script/File | Redirected file or pipe   | File ends      |

---

# Working with Files in Python

---

## Opening and Closing Files

- Use the built-in `open()` function:

```python
f = open("data.txt", "r")   # open file for reading
content = f.read()          # read entire file
print(content)
f.close()                   # important: close the file
```

- Modes:
  - `"r"` → read (default)
  - `"w"` → write (overwrites file)
  - `"a"` → append
  - `"rb"` / `"wb"` → binary

---

## Reading Files Line by Line

```python
f = open("data.txt", "r")

for line in f:
    print(line.strip())

f.close()
```

👉 This way the file is read **line by line**.

---

## The Problem with Manual `close()`

- If you forget `f.close()`, the file stays open.
- This may cause:
  - Memory usage issues
  - Problems writing to the same file
  - Resource leaks

✅ Python provides a better way: the **`with` statement**.

---

# The `with` Statement in Python

---

## What is `with`?

- `with` is a **context manager**.
- It ensures resources are cleaned up automatically.
- General form:

```python
with expression as variable:
    # use variable
# resource is automatically closed here
```

- Example with a generic resource:

```python
with open("data.txt", "r") as f:
    content = f.read()
# file is automatically closed
```

---

## Using `with` for Files

- Equivalent to `open()` + `close()`, but safer:

```python
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
# file is already closed here
```

- Advantages:
  - No need to remember `close()`
  - Safer in case of errors

---

## Comparing Approaches

**Without `with`:**

```python
f = open("data.txt", "r")
data = f.read()
f.close()
```

**With `with`:**

```python
with open("data.txt", "r") as f:
    data = f.read()
```

👉 Both work, but `with` is more reliable.

---

# Summary

✅ `sys.stdin` → standard input (keyboard or redirected input)  
✅ Interactive mode → waits for user input until EOF (<kbd>Ctrl+Z</kbd> + <kbd>Enter</kbd> on Windows)  
✅ Script mode → reads from files or pipes automatically  
✅ File handling with `open` and `close`  
✅ `with` statement → automatic cleanup, safer resource management  
