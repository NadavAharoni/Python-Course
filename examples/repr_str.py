class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __repr__(self):
        return f"Book({self.title!r}, {self.pages})"

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

b = Book("Python 101", 200)
print(repr(b))
print(str(b))
print(b)