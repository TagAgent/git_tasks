class Book:
    def __init__(self, title_pm: str, author_pm: str) -> None:
        self.title = title_pm
        self.author = author_pm

    def display_info(self):
        print(f"Название: {self.title}, Автор: {self.author}")

class Library:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, new_book: Book) -> None:
        self.books.append(new_book)

    def remove_book(self, remove_book: Book) -> None:
        self.books.remove(remove_book)

    def find_book(self, book: Book) -> Book:
        for item in self.books:
            if item.title == book.title:
                return item

    def list_book(self):
        return self.books

lib = Library()

book1 = Book(title_pm="Hoobit", author_pm="John Tolkin")
book2 = Book(title_pm="Война и мир", author_pm="Л. Н. Толстой")

book1.display_info()
lib.add_book(book1)
print(lib.list_book())
lib.add_book(book2)
print(lib.list_book())
lib.remove_book(book1)
print(lib.list_book())
print(lib.find_book(book2))
