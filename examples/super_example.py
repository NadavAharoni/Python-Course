class A:
    def greet(self):
        print("A greet")

class B(A):
    def greet(self):
        print("B greet")
        print("In B.greet(), calling super().greet()")
        super().greet()

class C(A):
    def greet(self):
        print("C greet")
        print("In C.greet(), calling super().greet()")
        super().greet()

class D(B, C):
    def greet(self):
        print("D greet")
        print("In D.greet(), calling super().greet()")
        super().greet()

d = D()
print("calling d.greet()")
d.greet()

print(D.mro())

