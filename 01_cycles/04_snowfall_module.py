# -*- coding: utf-8 -*-

import simple_draw as sd
from paint.snowfall_engine import snowflake_gen, snowflake_color, snowflake_shift, check_snowflakes, \
    snowflake_background, snowflake_freeze

sd.resolution = (1200, 600)
# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall_engine.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

snowflake_gen(20)
while True:
    sd.start_drawing()
    snowflake_background(color=sd.background_color)
    snowflake_shift()
    snowflake_color()
    if check_snowflakes():
        snowflake_freeze(snowflakes_freeze=check_snowflakes())
    sd.finish_drawing()
    sd.sleep(0.09)
    if sd.user_want_exit():
        break

sd.pause()


# зачет!
