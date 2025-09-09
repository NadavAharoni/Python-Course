class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def greet():
        print("Hello!")
        # count += 1  # This will raise an error because 'count' is not defined in this scope

obj1 = MyClass()
obj2 = MyClass()
print(MyClass.get_count())  # Output: 2
MyClass.greet()  # Output: Hello!

print(obj1.count)  # Output: 2
print(obj2.count)  # Output: 2
print(MyClass.count)  # Output: 2
