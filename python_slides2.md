---
marp: true
theme: default
paginate: true

---
# Python


---
# Python Syntax

No semicolon `;` - one command in each line
No curly braces `{}` - block are defined by:
- a "block opening" line, which ends with colon `:`
- indentation, block ends with the next non-indeneted line.

Example:
```python
i = 1
while i<=10:
    j = 1
    while j<=10:
        print(i*j, end=",")
        j += 1
    print()
    i += 1
```

---
# Python Syntax

Comments: anything after `#`

```python
i = 1
while i<=10:
    j = 1
    while j<=10:
        print(i*j, end=",")
        j += 1
    # end of while loop, because
    # the next line is not indented
    print()
    i += 1
```



