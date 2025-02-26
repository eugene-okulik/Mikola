temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
    22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

lst_hottest_temp = list(filter(lambda x: x > 28, temperatures))
print(lst_hottest_temp)
print(max(lst_hottest_temp))
print(min(lst_hottest_temp))
print(round(sum(lst_hottest_temp) / len(lst_hottest_temp), 1))
