import sys

for line in sys.stdin:
    s = line.strip()
    if s == "":              # Skip empty lines
        continue
    print(">", s)

