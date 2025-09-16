import sys

if len(sys.argv) < 2:
    print(F"Usage: {sys.argv[0]} file_name")
    exit()

file_name = sys.argv[1]
print(file_name)


