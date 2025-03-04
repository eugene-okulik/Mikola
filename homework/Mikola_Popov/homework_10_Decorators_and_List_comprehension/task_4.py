PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_file = [i for i in PRICE_LIST.split()]
new_dict = {new_file[i]: int(new_file[i + 1][:-1])
            for i in range(0, len(new_file), 2)}
print(new_dict)
