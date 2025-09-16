t1 = (1,2,3)
a,b,c = t1
print(a,b,c,"moshe","yaakov")

a=1
b=1
for i in range(10):
    a,b = b,a+b
    print(a, b)

print("---------")

numbers = [ i+1 for i in range(10) ]
print(numbers)
squares = [ (i+1)**2 for i in range(10) ]
print(squares)

for i, item in enumerate( zip(numbers, squares) ):
    print(i, item)

list1 = [ None ] * 6
# print( list1 )

empty_list = []
list1 = [ empty_list ] * 5
print( F"list1 = [ empty_list ] * 5 = ", list1 )
print()

for i, sub_list in enumerate(list1):
    sub_list.append(i)
    list1[i] = sub_list.copy()

for l in list1:
    print(l)

print( *list1 )

# print("=====")
# list1 = [ [] for i in range(5) ]
# print( list1 )
# for i, sub_list in enumerate(list1):
#     sub_list += [i]

# for l in list1:
#     print(l)

# print("=====")
# list1 = [ [] for i in range(5) ]
# for i, sub_list in enumerate(list1):
#     new_list = list1[i] + [i]
#     list1[i] = new_list

# for l in list1:
#     print(l)