def multiply_value(self, factor):
    self.value *= factor
    # print("This is a dynamically added method.")

class MyClass:
    def __init__(self, value):
        self.value = value

MyClass.multiply_value = multiply_value

obj = MyClass(10)
# obj.multiply_value = multiply_value.__get__(obj)
obj.multiply_value(5)
print(obj.value)

obj2 = MyClass(20)
obj2.multiply_value(3)  # This would raise an AttributeError
print(obj2.value)