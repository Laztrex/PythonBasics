# -*- coding: utf-8 -*-
import simple_draw as sd


# Создать пакет, в котором собрать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Каждую функцию разместить в своем модуле. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)


# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

from paint.rainbow import rainbow
from paint.house import house
from paint.wall import wall
from paint.snow import snow
from paint.tree import tree
from paint.tree2 import tree2
from paint.smile import smile
from paint.bat_signal import bat_signal
from paint.sun import SunPainting

sd.resolution = (1200, 600)

bat_signal()
house()
wall()
tree()
tree2()
sun = SunPainting(offset_ray=3)

while True:

    for animation_index in range(1, 7, 1):
        rainbow(color_index=animation_index)
        smile(add_wink=animation_index)
        snow(y_drop=25)
        sun.sun_core()

    if sd.user_want_exit():
        break
# зачет!
