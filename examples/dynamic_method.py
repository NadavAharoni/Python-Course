def multiply_value(self, factor):
    self.value *= factor
    # print("This is a dynamically added method.")

class MyClass:
    def __init__(self, value):
        self.value = value

MyClass.multiply_value = multiply_value

obj = MyClass(10)
obj.multiply_value(5)
print(obj.value)
