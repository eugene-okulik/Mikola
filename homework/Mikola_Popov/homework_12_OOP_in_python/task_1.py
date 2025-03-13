import collections


class Flower:
    stem = True  # ствол
    petals = True  # лепестки
    leaves = True  # листья
    stamen = True  # тычинка
    pestle = True  # пестик

    def __init__(self, color_petals, length_stem, number_of_petals, flower_name, day_of_live):
        self.flower_name = flower_name
        self.color_petals = color_petals  # цвет лепестков
        self.length_stem = length_stem  # длина ствола
        self.number_of_petals = number_of_petals  # количество лепестков
        self.day_of_live = day_of_live

    def __str__(self):
        return f'{self.flower_name}, {self.color_petals}'


class Tulip(Flower):

    def __init__(self, color_petals, length_stem, number_of_petals, flower_name, time_of_live):
        super().__init__(color_petals, length_stem, number_of_petals, flower_name, time_of_live)
        # self.cost_of_one_flower_tulip = 4.50


class Rose(Flower):

    def __init__(self, color_petals, length_stem, number_of_petals, flower_name, time_of_live):
        super().__init__(color_petals, length_stem, number_of_petals, flower_name, time_of_live)
        # self.cost_of_one_flower_rose = 4.0


class Chamomile(Flower):

    def __init__(self, color_petals, length_stem, number_of_petals, flower_name, time_of_live):
        super().__init__(color_petals, length_stem, number_of_petals, flower_name, time_of_live)
        # self.cost_of_one_flower_tulip = 1.0


class Bouquet:
    cost_of_one_flower_tulip = 4.5
    cost_of_one_flower_rose = 4.0
    cost_of_one_flower_chamomile = 1.0

    def __init__(self):
        self.lst_flowers = []
        self.bouguet = {}

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
        sort_by = []
        for length in self.lst_flowers:
            sort_by.append(length.length_stem + ': ' + length.flower_name)
        print(*sorted(sort_by), sep="\n")

    def sort_by_price(self):
        sorted_lst = {}
        for key1 in self.bouguet:
            if isinstance(key1, Rose):
                sorted_lst[key1.flower_name] = (self.cost_of_one_flower_rose * self.bouguet[key1])
            if isinstance(key1, Chamomile):
                sorted_lst[key1.flower_name] = (self.cost_of_one_flower_chamomile * self.bouguet[key1])
            if isinstance(key1, Tulip):
                sorted_lst[key1.flower_name] = (self.cost_of_one_flower_tulip * self.bouguet[key1])
        for key, value in sorted_lst.items():
            print(f"{key}: {value} руб")

    # Продолжительность жизни букета
    def average_live_of_flowers(self):
        day_live = 0
        count = 0
        for flower in self.lst_flowers:
            if flower in self.bouguet:
                if flower.flower_name == "Роза":
                    day_live += flower.day_of_live
                    count += 1
                elif flower.flower_name == "Ромашка":
                    day_live += flower.day_of_live
                    count += 1
                elif flower.flower_name == "Тюльпан":
                    day_live += flower.day_of_live
                    count += 1
        return f'Средняя продолжительность жизни букета - {day_live // count}'

    # Собираем букет, сохраняя его содержимое в словарь.
    def collect_bouguet(self, flower, count):
        if self.bouguet is True:
            if flower.flower_name not in self.bouguet[flower]:
                self.bouguet[flower] = count
            else:
                self.bouguet[flower] += count
        else:
            self.bouguet[flower] = self.bouguet.setdefault(flower, 0) + count

    # Подсчитываем стоимость букета, по стоимости каждого цветка.
    def calc_cost_of_the_bouguets(self):
        res = []
        for key, value in self.bouguet.items():
            if isinstance(key, Tulip):
                res.append(value * self.cost_of_one_flower_tulip)
            elif isinstance(key, Rose):
                res.append(value * self.cost_of_one_flower_rose)
            elif isinstance(key, Chamomile):
                res.append(value * self.cost_of_one_flower_chamomile)
        print(f'Сумма вашего букета состовляет: {sum(res)} бел/руб.')

    def search_by_parameters(self):
        print("Поиск по времени увядания: - 'Имя цветка'")
        param = input("Name flower: ")
        for flower in self.lst_flowers:
            if flower.flower_name == param:
                return f'{flower.day_of_live} дней'
        return "Данных о цветке нет!!!"


flower_tulip = Tulip("Жёлтый", "25см", "6", "Тюльпан", 4)
flower_rose = Rose("Красный", "35см", "8", "Роза", 5)
flower_chamomile = Chamomile("Белый", "20см", "10", "Ромашка", 6)

bouguets = Bouquet()
bouguets.add_flowers(flower_rose)
bouguets.add_flowers(flower_chamomile)
bouguets.add_flowers(flower_tulip)
bouguets.display_flowers()
bouguets.collect_bouguet(flower_tulip, 5)
bouguets.collect_bouguet(flower_rose, 3)
bouguets.collect_bouguet(flower_chamomile, 3)
bouguets.collect_bouguet(flower_chamomile, 3)
print(bouguets.bouguet.__str__())
bouguets.calc_cost_of_the_bouguets()
print(bouguets.average_live_of_flowers())
bouguets.sort_by_price()
print(bouguets.sort_by_color())
bouguets.sort_by_length_stem()
print(bouguets.search_by_parameters())
