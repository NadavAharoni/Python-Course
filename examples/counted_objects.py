# import time

class CountedObject:
    count = 0
    live_objects = 0

    def __init__(self):
        CountedObject.count += 1
        CountedObject.live_objects += 1
        self.serial_number = CountedObject.count

    @classmethod
    def get_count(cls):
        return cls.count
    
    @classmethod
    def num_allocated(cls):
        return cls.live_objects


    def __del__(self):
        print(F"deleting {self.serial_number}")
        CountedObject.live_objects -= 1


obj1 = CountedObject()
obj2 = CountedObject()
obj3 = CountedObject()
print(F"num_allocated={CountedObject.num_allocated()}")

obj1 = None
print(F"num_allocated={CountedObject.num_allocated()}")

obj4 = CountedObject()
print(CountedObject.count)

print("end of program")


