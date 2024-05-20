class Book:
    def __init__(self, name_pm: str, author_pm: str, page_count_pm: int):
        self.name = name_pm
        self.author = author_pm
        self.page_count = page_count_pm

    def print_info(self) -> None:
        """Этот метод для вывода информации"""
        print(f"Название: {self.name}\nАвтор: {self.author}\nКоличество страниц: {self.name}")
        print()

book1 = Book(name_pm="Война и мир", author_pm="Лев Толстой", page_count_pm=1300)
book2 = Book(name_pm="Хоббит", author_pm="Джон Толкин", page_count_pm=256)

book1.print_info()
book2.print_info()