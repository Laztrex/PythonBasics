# -*- coding: utf-8 -*-

import simple_draw as sd


def tree():
    def next_random_branches(angle, length, next_point1, next_point2, random_sign, color):
        random_angle = sd.random_number(1, 12)
        random_length = sd.random_number(1, 15)
        if random_sign == 0:
            next_angle1 = angle + (30 - random_angle)
            next_angle2 = angle - (30 + random_angle)
            next_length = length * (.75 - random_length / 100)
            draw_branches(start_point=next_point1, angle=next_angle1, length=next_length, color=color)
            draw_branches(start_point=next_point2, angle=next_angle2, length=next_length, color=color)
        else:
            next_angle1 = angle + (30 + random_angle)
            next_angle2 = angle - (30 - random_angle)
            next_length = length * (.75 + random_length / 100)
            draw_branches(start_point=next_point1, angle=next_angle1, length=next_length, color=color)
            draw_branches(start_point=next_point2, angle=next_angle2, length=next_length, color=color)

    def draw_branches(start_point, angle, length, color):
        sd.start_drawing()
        if length < 3:
            return
        v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=1)
        v1.draw(color=color)
        v2 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=1)
        v2.draw(color=color)
        random_sign = sd.random_number(0, 1)
        if 3 < length < 9:
            if random_sign == 0:
                next_random_branches(angle=angle, length=length, next_point1=v1.end_point, next_point2=v2.end_point,
                                     color=sd.COLOR_DARK_GREEN, random_sign=random_sign)
            else:
                next_random_branches(angle=angle, length=length, next_point1=v1.end_point, next_point2=v2.end_point,
                                     color=sd.COLOR_GREEN, random_sign=random_sign)
        else:
            if random_sign == 0:
                next_random_branches(angle=angle, length=length, next_point1=v1.end_point, next_point2=v2.end_point,
                                     color=sd.COLOR_DARK_ORANGE, random_sign=random_sign)
            else:
                next_random_branches(angle=angle, length=length, next_point1=v1.end_point, next_point2=v2.end_point,
                                     color=sd.COLOR_DARK_ORANGE, random_sign=random_sign)

    root_point = sd.get_point(760, 30)
    draw_branches(start_point=root_point, angle=90, length=100, color=sd.COLOR_DARK_ORANGE)
    sd.finish_drawing()
