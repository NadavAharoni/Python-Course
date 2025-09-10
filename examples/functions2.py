def square(x):
    return x * x

def twice(x):
    return x + x

def apply(func, value):
    return func(value)

list_of_functions = [square, twice]

for func in list_of_functions: 
    print(func.__name__, ":", func(3))

# print(list_of_functions)

# for func in list_of_functions: 
#     print(func.__name__)

# print(apply(square, 5))  # 25
# print(apply(twice, 5))  # 10