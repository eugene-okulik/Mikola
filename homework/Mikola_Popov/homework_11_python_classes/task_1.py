class Book:
    page_material = "paper"
    text_in_page = True

    def __init__(self, title, author, count_page, ISBN, reserve):
        self.title = title
        self.author = author
        self.count_page = count_page
        self.ISBN = ISBN
        self.reserve = reserve

    def reservation(self):
        if self.reserve:
            return "-- ЗАРЕЗЕРВИРОВАНА --"

    def __str__(self):
        if self.reserve:
            return (
                f"Название: {self.title}, Автор: {self.author},"
                f"страниц: {self.count_page}, материал: {self.page_material},"
                f"{self.reservation()}")
        print(20 * "*")
        return (
            f"Название: {self.title}, Автор: {self.author},"
            f" страниц: {self.count_page}, материал: {self.page_material}"
        )


book_1 = Book("Идиот", "Ф.Достоевский", 500, "143-345", True)
print(book_1)

book_2 = Book("Собачье сердце", "М.Булгаков", 653, "543-234", False)
print(book_2)

book_3 = Book("Анна Каренина", "Л.Толстой", 780, "764-111", False)
print(book_3)

book_4 = Book("Мёртвые души", "Н.Гоголь", 348, "213-932", False)
print(book_4)

book_5 = Book("Медведь", "А.Чехов", 345, "736-102", False)
print(book_5)
