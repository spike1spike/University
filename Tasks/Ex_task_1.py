from random import randint

k_tries = 1
c_num = randint(0, 100)
g_num = input('Введите число: ')
while g_num.isdigit() == False:
    print('Число введено неверно!')
    g_num = input('Введите число: ')
while g_num != 'Выход':
    if g_num.isdigit():
        g_num = int(g_num)
        if g_num < c_num:
            print('Ваше число меньше!')
        elif g_num > c_num:
            print('Ваше число больше!')
        else:
            break
        k_tries += 1
    else:
        print('Число введено неверно!')
    g_num = input('Введите число: ')

if g_num == 'Выход':
    print('Вы вышли из программы!')
else:
    if k_tries%10 == 1:
        print(f'Поздравляем, вы угадали число за {k_tries} попытку!')
    elif 2 <= k_tries%10 <= 4:
        print(f'Поздравляем, вы угадали число за {k_tries} попытки!')
    else:
        print(f'Поздравляем, вы угадали число за {k_tries} попыток!')
input()
