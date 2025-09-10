class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1
        self.count = MyClass.count

    def get_count_o(s):
        return s.count
    
    def set_count_o(self, value):
        self.count = value

    @classmethod
    def get_count(c):
         return c.count

    @staticmethod
    def greet():
        print("Hello!")
        # count += 1

obj1 = MyClass()
obj2 = MyClass()
print(F"obj2.get_count_o() = {obj2.get_count_o()}" )
obj2.set_count_o(17)
print(F"obj2.get_count_o() = {obj2.get_count_o()}" )

exit()
# obj2 = MyClass()
obj3 = obj2
print(F"MyClass.get_count() = {MyClass.get_count()}" )
print()
print(F"obj1.get_count_o() = {obj1.get_count_o()}" )
print(F"obj2.get_count_o() = {obj2.get_count_o()}" )
print(F"obj3.get_count_o() = {obj3.get_count_o()}" )

list1 = []
for i in range(10):
    list1.append( MyClass() )

# print(list1)
print(list1[0].get_count())

print(list1[0].get_count_o())
print(list1[len(list1)-1].get_count_o())

MyClass.greet()

MyClass.count = 53
# print(obj1.count)  # Output: 2
# print(obj2.count)  # Output: 2
# print(MyClass.count)  # Output: 2
# obj3 = MyClass()
# print(obj1.count)