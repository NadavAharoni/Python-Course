class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        print("Hello from B")
        super().hello()

b = B()
b.hello()

exit()

class Animal:
    def __init__(self):
        # super().__init__()
        print("Animal.__init__ called")

    def speak(self):
        print("Some sound")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog.__init__ called")

    def speak(self):
        super().speak()  # call parent method
        print("Woof!")

d = Dog()
d.speak()

