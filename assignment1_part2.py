class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.display()

    def display(self):
        print(self.title + ", written by " + self.author)

if __name__ == "__main__":
    b1 = Book("John Steinbeck", "Of Mice and Men")
    b2 = Book("Harper Lee", "To Kill a Mockingbird")