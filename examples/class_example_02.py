class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        # new attributes can be added dynamically
        self.barked = True
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy")
my_dog.bark()
my_dog.hair_color = "Brown"
del my_dog.hair_color # deleting dynamic attribute
del my_dog.name  # deleting regular attribute


