import sys

print(sys.argv)
if ( len(sys.argv) < 2 ):
    print(F"usage: {sys.argv[0]} file_name")
    exit()

f = open(sys.argv[1], 'r', encoding='windows-1255')

# print the first 5 lines, to inspect the output
for i in range(5):
    line = f.readline()
    print(line.strip())

f.close()



