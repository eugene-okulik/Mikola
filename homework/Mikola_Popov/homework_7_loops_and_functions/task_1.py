from random import randint


def guess_the_number_game():
    print('Что-бы угадать число, у вас есть пять попыток!!!')
    random_number = randint(1, 10)
    attemts = 5
    while attemts != 0:
        print('-' * 20)
        print(f'Попытка № {attemts}')
        user_input = int(input('Enter number: '))
        attemts -= 1
        if user_input == 'exit':
            print('User, good bye!!!')
            break
        elif user_input < random_number:
            print('Искомое число больше!!!')
        elif user_input > random_number:
            print('Искомое число меньше!!!')
        elif user_input == random_number:
            print(f'Поздравляю!!! Вы угадали! Искомое число {random_number}')
            break

    print('*' * 20)
    print('Попытки исчерпаны!')
    print('Вы проиграли!!!')


guess_the_number_game()
