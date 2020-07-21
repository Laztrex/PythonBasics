# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1

from engine_modules.mastermind_engine import make_number, check_number, game_over
from termcolor import cprint, colored

make_number()
count_steps = 0

while True:
    input_number = input(colored('Введите четырехзначное число -> ', color='magenta'))
    if input_number.isnumeric() and len(input_number) == 4:
        input_number_list = list(map(int, input_number))
        cprint('Вы ввели: {}'.format(input_number), color='cyan')
        cprint(check_number(input_number_list), color='blue')
        count_steps += 1
    else:
        cprint('Вы точно ввели четырехзначное число? Попробуйте еще раз!', color='red')
        continue

    if game_over():
        cprint('Угадали! Вам потребовалось шагов - {}'.format(count_steps), color='yellow')
        answer = input('Хотите еще партию? (Да/Нет)')
        if len(answer) == 3:
            break
        else:
            continue

