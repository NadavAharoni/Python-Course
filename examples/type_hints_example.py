import math
from typing import Any, List, Dict, Optional, Union, Callable

def add(x: int, y: int) -> int:
    return x + y

def sub(x ,y):
    return x - y

def minus(x):
    return -x

result: str = add(3, 4)
print( type(result) )
print(result)

names: List[ Union[str,int] ] = ["Alice", "Bob", 1 ]

f1 : Callable[ [Any, Any], Any] = add
print("f1 = add")
print( f1(2,4) )

f2 = add
f1 = math.pow

print("f1 = math.pow")
print( f1(2,4) )


# math.pow(4,5)

print( f2(5,6) )

F2_1 = Callable[ [Any, Any], Any ]

def apply_functions(x : float, y : float, list_of_functions : List[ F2_1]):
    for func in list_of_functions:
        result = func(x,y)
        print(result)


i : int = 6

functions : List[ F2_1 ] = [add, sub, math.pow]
a = 100
b = 50

apply_functions(a,b,functions)