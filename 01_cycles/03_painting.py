# -*- coding: utf-8 -*-
import simple_draw as sd


# Создать пакет, в котором собрать функции отрисовки
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# Анимировать картину.

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

