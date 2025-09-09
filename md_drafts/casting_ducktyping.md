# Casting and Duck Typing in Python

---

# Casting in Python?

- In languages like Java/C++, you can *upcast* (subclass → superclass) or *downcast* (superclass → subclass).
- **Python does not require explicit casting**:
  - Any `Dog` is automatically usable where an `Animal` is expected.
  - The reverse (treating an `Animal` as a `Dog`) only works if the object is truly a `Dog`.

```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

def make_speak(animal: Animal):
    animal.speak()

dog = Dog()
make_speak(dog)   # ✅ Works: Dog is-an Animal
```

---

# Upcasting vs Downcasting in Python

- **Upcasting**: automatic and implicit, no special syntax.
- **Downcasting**: unsafe — Python will not convert an `Animal` into a `Dog`.

```python
a = Animal()
d = Dog()

# Upcasting (Dog → Animal): automatic
animal: Animal = d
animal.speak()  # Woof!

# Downcasting (Animal → Dog): not supported
dog: Dog = a    # ❌ Only works if `a` is actually a Dog
```

⚠️ In Python, focus on **object behavior (duck typing)** rather than explicit casting.

---

# Duck Typing

- In Python, the type of an object matters less than the **methods/attributes it provides**.
- "If it looks like a duck and quacks like a duck, it’s a duck."

```python
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(obj):
    obj.quack()

make_it_quack(Duck())    # Quack!
make_it_quack(Person())  # I'm pretending to be a duck!
```

---

# Duck Typing vs Casting

- **Casting**: forces an object into a type (common in Java, C++).
- **Duck typing**: no casting, just call methods and trust the object.
- Benefits:
  - Flexible and dynamic.
  - Reduces boilerplate.
- Risks:
  - Errors appear only at runtime if the object lacks the expected method.

✅ Best practice: write functions that depend on **behavior, not type**.

