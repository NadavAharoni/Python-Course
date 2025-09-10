def greet(name, age=18):
    print(f"{name} is {age} years old")

def add_item(item, container=None):
    if container is None:
        container = []
    container.append(item)
    return container

def add_all(*numbers):
    print(type(numbers))
    first_item = numbers[0]
    print("First item:", first_item)
    for n in numbers:
        print(n)


def show_info(**data):
    print(type(data))
    for key, value in data.items():
        print(key, value)


def f1(a, b=2, /, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)


def f2(a, b, /, c, *, d):
    print(a, b, c, d)

f2(1, 2, 3, d=4)
f2(1, 2, c=3, d=4)
# f2(1, b=2, c=3, d=4)
# f2(1, 2, 3, d)

print("Hello", [1,2,3], (4,5,6), sep="|", end="\n\n")
print("---------------")

print("f1(1)")
f1(1)
print()

print("f1(1, 3, 4, 5)")
f1(1, 3, 4, 5)
print()

print("f1(1, 4, 5, x=9, y=10)")
f1(1, 4, 5, x=9, y=10)
print()

print("f1(1, b=3, x=9, y=10)")
f1(1, b=3, x=9, y=10)

print("f1(1, c=3, b=7, x=9, y=10)")
f1(1, c=3, b=7, x=9, y=10)


# show_info(name="Alice", age=20, city="New York", school="Michlala")
# add_all(1, 2, 3, 4)  # 10

# list1 = [ 1 , 2 ]
# list3 = add_item(3, list1)
# print("list1=", list1) 
# print("list3=", list3)
# print("list1 is list3:", list1 is list3)

# list2 = add_item(3)
# print("list2=", list2)
# list4 = add_item(4)
# print("list4=", list4)
# print("list2=", list2)
# print("list2 is list4:", list2 is list4)

# strings are immutable
def add_word_to_sentence(word, sentence):
    if sentence:
        sentence += " " + word
    else:
        sentence = word

    return sentence

# sentence1 = "Hello"
# sentence2 = add_word_to_sentence("World", sentence1)
# print("sentence1=", sentence1)
# print("sentence2=", sentence2)

# greet(age=20, name="Ana")
# greet("Bo")
# val = greet("Cathy")
# print(val)  # None
# str1 = "Hello" + " World" + "! " + str(888)
# greet(str1)
