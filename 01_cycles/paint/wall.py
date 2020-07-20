# -*- coding: utf-8 -*-

import simple_draw as bricks

def wall():
    width = 30
    height = 15
    y = 20
    y1 = 20
    y2 = 35

    for horizontal in range(13):
        y += 15
        start_point = bricks.get_point(300, y)
        end_point = bricks.get_point(510, y)

        bricks.line(start_point, end_point, bricks.COLOR_ORANGE, 2)

        if horizontal % 2 == 0:
            x1 = 300
            x2 = 300
        else:
            x1 = 630 / 2
            x2 = 630 / 2
        for vertical in range(7):
            start_point1 = bricks.get_point(x1, y1)
            end_point1 = bricks.get_point(x2, y2)
            bricks.line(start_point1, end_point1, bricks.COLOR_ORANGE, 2)
            x1 += width
            x2 += width

        y1 += height
        y2 += height

    start_point_end1 = bricks.get_point(510, 35)
    end_point_end1 = bricks.get_point(510, y1)
    bricks.line(start_point_end1, end_point_end1, bricks.COLOR_ORANGE, 2)

    start_point_end2 = bricks.get_point(300, 20)
    end_point_end2 = bricks.get_point(300, y1)
    bricks.line(start_point_end2, end_point_end2, bricks.COLOR_ORANGE, 2)

    left_bottom_window = bricks.get_point(360, 80)
    right_top_window = bricks.get_point(450, 185)
    bricks.rectangle(left_bottom_window, right_top_window, bricks.COLOR_YELLOW)

    bricks.line(bricks.get_point(385, 80), bricks.get_point(385, 185), bricks.COLOR_DARK_ORANGE, 2)
    bricks.line(bricks.get_point(360, 165), bricks.get_point(450, 165), bricks.COLOR_DARK_ORANGE, 2)