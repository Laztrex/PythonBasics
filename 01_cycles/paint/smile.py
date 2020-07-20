import simple_draw as sd


def smile(add_wink):
    i = 0
    while i < 2:
        x = 425
        y = 130
        point_smile = sd.get_point(x, y)
        point_eyes_1 = sd.get_point(x - 6, y + 5)
        point_eyes_2 = sd.get_point(x + 6, y + 5)
        color_smile = sd.COLOR_BLACK
        color_eyes_lips = sd.COLOR_WHITE
        radius = 20
        sd.circle(point_smile, radius, color_smile, width=0)
        sd.circle(point_eyes_1, 2, color_eyes_lips, width=1)
        if add_wink < 3:
            sd.line(sd.get_point(x, y + 5), sd.get_point(x + 10, y + 5), color_eyes_lips, width=1)
        else:
            sd.circle(point_eyes_2, 2, color_eyes_lips, width=1)
        start_point1 = sd.get_point(x - 4, y - 6)
        end_point1 = sd.get_point(x - 3, y - 5)
        start_point2 = sd.get_point(x - 3, y - 5)
        end_point2 = sd.get_point(x + 3, y - 5)
        start_point3 = sd.get_point(x + 3, y - 5)
        end_point3 = sd.get_point(x + 4, y - 6)
        sd.line(start_point1, end_point1, color_eyes_lips, 1)
        sd.line(start_point2, end_point2, color_eyes_lips, 1)
        sd.line(start_point3, end_point3, color_eyes_lips, 1)

        point_list1 = (sd.get_point(x - 17, y + 12), sd.get_point(x - 9, y + 18), sd.get_point(x - 17, y + 35))
        sd.polygon(point_list1, sd.COLOR_BLACK, width=0)
        point_list2 = (sd.get_point(x + 17, y + 2), sd.get_point(x + 9, y + 18), sd.get_point(x + 17, y + 35))
        sd.polygon(point_list2, sd.COLOR_BLACK, width=0)

        sd.rectangle(sd.get_point(402, 78), sd.get_point(448, 115), sd.COLOR_BLACK)
        i += 1


sd.sleep(0.02)

