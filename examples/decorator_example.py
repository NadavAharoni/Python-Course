from datetime import datetime

def measure_time(func):
    def wrapper(*args, **kwargs):
        time1 = datetime.now()
        result = func(*args, **kwargs)
        time2 = datetime.now()
        print(F"{func} took {time2 - time1}")
        return result
    return wrapper

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def add(x,y):
    print(F"calculating {x}+{y}")
    return x+y

@measure_time
@my_decorator
def multiply(x,y):
    result = 0
    for i in range(y):
        result += x
    return result

# result = add(4,5)
# print(result)

print( multiply(4,500000) )