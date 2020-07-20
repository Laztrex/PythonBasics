# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as bricks

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

bricks.resolution = (600, 600)
width = 100
height = 50
x = 0
y = 0
y1 = 0
y2 = 50

for horizontal in range(13):
    y += 50
    start_point = bricks.get_point(0, y)
    end_point = bricks.get_point(600, y)

    bricks.line(start_point, end_point, bricks.COLOR_RED, 5)

    if horizontal % 2 == 0:
        x1 = 0
        x2 = 0
    else:
        x1 = width / 2
        x2 = width / 2
    for vertical in range(7):
        start_point1 = bricks.get_point(x1, y1)
        end_point1 = bricks.get_point(x2, y2)
        bricks.line(start_point1, end_point1, bricks.COLOR_RED, 5)
        x1 += width
        x2 += width

    y1 += height
    y2 += height


bricks.pause()
# зачет!
