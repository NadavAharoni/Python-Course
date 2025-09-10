def power_3(x):
    print("called power_3 with x:", x)
    return x**3

nums = [1, 2, 3, 4]
# squared = map(lambda x: x**2, nums)
iter_power_3 = map(power_3, nums)

# while True:
#     try:
#         print(iter_power_3.__next__())
#     except StopIteration:
#         break

class Power3:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        # print("calling Power3.__next__ current:", self.current)
        if self.current > self.end:
            raise StopIteration
        number = self.current
        value = number ** 3
        self.current += 1
        return number, value  # Return both the number and its cube
    
power3 = Power3(10, 50)

for number, val in power3:
    print(f"{number}^3 = {val}")


# print(list(squared))  # [1, 4, 9, 16]
