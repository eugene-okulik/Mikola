from task_1 import Book


class SchoolBook(Book):
    availability_of_task = True

    def __init__(self, title, author, count_page, ISBN, reserve, item, classroom):
        super().__init__(title, author, count_page, ISBN, reserve)
        self.item = item
        self.classroom = classroom

    def display_schoolbook(self):
        print(20 * '*')
        if self.reserve:
            return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.count_page}, '
                f'Предмет: {self.item}, Класс: {self.classroom}, {self.reservation()}')
        return f'Название: {self.title}, Автор: {self.author}, страниц: {self.count_page}, Предмет: {self.item}, Класс: {self.classroom}'



schoolbook_1 = SchoolBook('Алгебра', 'Ерёменко', 120, '342-000', True, 'Математика', 9)
print(schoolbook_1.display_schoolbook())
schoolbook_2 = SchoolBook('История Беларуси', 'Щёлков', 200, '534-012', False, 'История', 8)
print(schoolbook_2.display_schoolbook())
schoolbook_3 = SchoolBook('Социально-экономическая география мира', '', 231, '919-982', False, 'География', 10)
print(schoolbook_3.display_schoolbook())
