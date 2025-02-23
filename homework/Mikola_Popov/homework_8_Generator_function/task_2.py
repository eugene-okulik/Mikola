def fibb(n):
    f1, f2 = 0, 1
    count = 0
    while count < n:
        yield f1
        f1, f2 = f2, f1 + f2
        count += 1


n = int(input('Enter number: '))
search_number = []
for i in fibb(n + 1):
    if i == 5:
        search_number.append(i)
    if 200 <= i < 300:
        search_number.append(i)
    if 1000 <= i < 2000:
        search_number.append(i)
    if 100000 <= i < 200000:
        search_number.append(i)
print(search_number)
