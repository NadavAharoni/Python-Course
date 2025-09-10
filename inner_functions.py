def outer(x):
    def inner(y):
        return x + y
    return inner


f1 = outer(10)
f2 = outer(20)

# f1:
# def inner(y):
#     return 10 + y

print("f1(5):", f1(5))
print("f2(5):", f2(5))

print(f1.__name__, f1)
print(f2.__name__, f2)
