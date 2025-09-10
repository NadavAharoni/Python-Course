class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return F"({self.x},{self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
        

def tests():
    v1 = Vector(20,30)
    v2 = Vector(30,80)

    print(v1)
    v3 = v1 + v2
    v4 = v1.__add__(v2)
    print(v3)
    print(v4)


if __name__ == "__main__":
    print(__name__)
    tests()
else:
    print(__name__)
