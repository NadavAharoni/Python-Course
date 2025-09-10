class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self._name = value

p = Person("Alice")
print(p.name)  # Accessing the property
p.name = "Bob"  # Using the setter
print(p.name)
p.name = "Bo"  

exit()

class Person2:
    def __init__(self, name):
        self._n = name

    @property
    def name(self):
        return self._n

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        if len(value) < 2:
            raise ValueError("Name must be at least 2 characters long")
        self._n = value

p2 = Person2("Charlie")
print(p2.name)  # Accessing the property
p2.name = "Dave"  # Using the setter
print(p2.name)
# p2.name = "D"  # This will raise a ValueError