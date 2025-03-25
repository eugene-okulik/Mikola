import collections


class Flower:
    stem = True  # ствол
    petals = True  # лепестки
    leaves = True  # листья
    stamen = True  # тычинка
    pestle = True  # пестик

    def __init__(
        self,
        color_petals,
        length_stem,
        number_of_petals,
        flower_name,
        day_of_live,
        price,
    ):
        self.flower_name = flower_name
        self.color_petals = color_petals  # цвет лепестков
        self.length_stem = length_stem  # длина ствола
        self.number_of_petals = number_of_petals  # количество лепестков
        self.day_of_live = day_of_live
        self.price = price

    def __str__(self):
        return f"{self.flower_name}, {self.color_petals}"


class Tulip(Flower):
    def __init__(
        self,
        color_petals,
        length_stem,
        number_of_petals,
        flower_name,
        time_of_live,
        price,
    ):
        super().__init__(
            color_petals,
            length_stem,
            number_of_petals,
            flower_name,
            time_of_live,
            price,
        )


class Rose(Flower):
    def __init__(
        self,
        color_petals,
        length_stem,
        number_of_petals,
        flower_name,
        time_of_live,
        price,
    ):
        super().__init__(
            color_petals,
            length_stem,
            number_of_petals,
            flower_name,
            time_of_live,
            price,
        )


class Chamomile(Flower):
    def __init__(
        self,
        color_petals,
        length_stem,
        number_of_petals,
        flower_name,
        time_of_live,
        price,
    ):
        super().__init__(
            color_petals,
            length_stem,
            number_of_petals,
            flower_name,
            time_of_live,
            price,
        )


class Bouquet:
    def __init__(self):

        self.lst_flowers = []
        self.bouguet = []

    def add_flowers(self, name):
        self.lst_flowers.append(name)

    def display_flowers(self):
        for name in self.lst_flowers:
            print(name.flower_name)

    def sort_by_color(self):
        lst_color = []
        for color in self.lst_flowers:
            lst_color.append(color.color_petals + "-" + color.flower_name)
        return sorted(lst_color)

    def sort_by_length_stem(self):
        print("Сортировка цветов по длине стебля")
        sort_by = {}
        for length in self.lst_flowers:
            sort_by[int(length.length_stem[:-2])] = length.flower_name
            sort_by = collections.OrderedDict(
                sorted(sort_by.items(), reverse=True))
        for key, item in sort_by.items():
            print(f"{item} - {key}см")

    def sort_by_price(self):
        sorted_lst = []
        max_price = 0
        for flower in self.bouguet:
            if max_price < flower.price:
                sorted_lst.insert(
                    0, (f"{flower.flower_name} - {flower.price} руб."))
                max_price = flower.price
            else:
                sorted_lst.append(
                    (f"{flower.flower_name} - {flower.price} руб."))
        for object_flower in sorted_lst:
            print(object_flower)

    # Продолжительность жизни букета
    def average_live_of_flowers(self):
        day_live = 0
        for flower in self.bouguet:
            day_live += flower.day_of_live
        return (
            f"Средняя продолжительность жизни букета в днях:"
            f"  {day_live // len(self.bouguet)}"
        )

    # Собираем букет, сохраняя его содержимое в list.
    def collect_bouguet(self, flower):
        self.bouguet.append(flower)
        return self.bouguet

    # Подсчитываем стоимость букета, по стоимости каждого цветка.
    def calc_cost_of_the_bouguets(self):
        summa = 0
        for flower in self.bouguet:
            summa += flower.price
        print(f"Сумма вашего букета состовляет: {summa} бел/руб.")

    def search_by_parameters(self):
        print("Поиск по времени увядания: - 'в днях'")
        param = int(input("Введите количество дней: "))
        result = []
        for flower in self.lst_flowers:
            if flower.day_of_live == param:
                result.append(flower.flower_name)
        for name in result:
            print(f"------{name}------")


flower_tulip = Tulip("Жёлтый", "25см", "6", "Тюльпан", 4, 4.5)
flower_rose = Rose("Красный", "35см", "8", "Роза", 4, 4.0)
flower_chamomile = Chamomile("Белый", "20см", "10", "Ромашка", 6, 1.0)

bouguets = Bouquet()
bouguets.add_flowers(flower_rose)
bouguets.add_flowers(flower_chamomile)
bouguets.add_flowers(flower_tulip)
bouguets.collect_bouguet(flower_tulip)
bouguets.collect_bouguet(flower_rose)
bouguets.collect_bouguet(flower_chamomile)
bouguets.collect_bouguet(flower_chamomile)
bouguets.display_flowers()
print(20 * "*")
bouguets.calc_cost_of_the_bouguets()
print(20 * "*")
print(bouguets.average_live_of_flowers())
print(20 * "*")
bouguets.sort_by_price()
print(20 * "*")
print(bouguets.sort_by_color())
print(20 * "*")
bouguets.sort_by_length_stem()
print(20 * "*")
bouguets.search_by_parameters()
