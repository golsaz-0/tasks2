from random import *

health = 3

correct_ans = 0

while health != 0:
    a = randint(1, 100 + 1)

    b = randint(1, 100 + 1)

    print(f'{a} + {b}')

    ans = int(input())

    if ans == (a + b):
        print('Правильно!')

        correct_ans += 1
    else:
        print('Ответ неверный')

        health -= 1

print(f'Игра окончена. Правильный ответов: {correct_ans}')
