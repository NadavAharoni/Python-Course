class skip_iterator:
    def __init__(self, list, k):
        self.list = list
        self.k = k
        self.index = k - 1  # Start at the k-th item (0-based index)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.list):
            raise StopIteration
        value = self.list[self.index]
        self.index += self.k
        return value

    def reset(self):
        self.index = self.k - 1


if __name__ == "__main__":
    print("Example with natural numbers, k=5:")

natural_numbers = [i for i in range(1, 50)]
for num in skip_iterator(natural_numbers, 5):
    print(num, end=",")
print(end="\n\n")

# example with reusing the iterator
items = [10, 20, 30, 40, 50, 60, 70]
k = 3
it = skip_iterator(items, k)
print("First iteration:")
for item in it:
    print(item, end=",")
    print(end="\n\n")

    it.reset()
    print("After reset:")
    for item in it:
        print(item, end=",")
