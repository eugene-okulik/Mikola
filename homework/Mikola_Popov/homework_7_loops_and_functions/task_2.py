def print_program(dictionary):
    for key, item in dictionary.items():
        print(key * item)


words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
print_program(words)
