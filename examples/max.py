import sys

max_val = None

for line in sys.stdin:
    s = line.strip()
    if s == "":              # Skip empty lines
        continue
    try:
        x = float(s)         # Try to convert the strong to a number (including floats)
    except ValueError:       # Not a number – exit
        break
    
    if max_val is None or x > max_val:
        max_val = x

if max_val is None:
    print("empty list - no maximum")
else:
    print(F"max is {max_val}")


