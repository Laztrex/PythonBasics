import simple_draw as sd


def bat_signal():
    x = 700
    y = 470
    bat_rays = (sd.get_point(x + 250, y - 330), sd.get_point(x, y - 50), sd.get_point(x + 40, y + 32))
    sd.polygon(bat_rays, sd.COLOR_DARK_YELLOW, width=0)

    radius_sun = 50
    color_sun = sd.COLOR_WHITE
    point_sun = sd.get_point(x, y)
    sd.circle(point_sun, radius_sun, color_sun, 0)

    point_list = (sd.get_point(x - 6, y + 11), sd.get_point(x - 15, y + 16), sd.get_point(x - 17, y + 22), sd.get_point(x - 34, y + 15), sd.get_point(x - 30, y + 15), sd.get_point(x - 21, y + 6), sd.get_point(x - 18, y + 1),
                  sd.get_point(x - 14, y), sd.get_point(x - 7, y - 3), sd.get_point(x - 6, y - 5), sd.get_point(x - 1, y - 9),
                  sd.get_point(x, y - 12), sd.get_point(x, y - 15), sd.get_point(x, y - 17),
                  sd.get_point(x, y - 12), sd.get_point(x + 1, y - 9), sd.get_point(x + 6, y - 5), sd.get_point(x + 7, y - 3),
                  sd.get_point(x + 14, y), sd.get_point(x + 18, y + 1), sd.get_point(x + 21, y + 6), sd.get_point(x + 30, y + 15),
                  sd.get_point(x + 34, y + 15), sd.get_point(x + 17, y + 22), sd.get_point(x + 15, y + 16), sd.get_point(x + 6, y + 11))
    sd.polygon(point_list, sd.COLOR_BLACK, width=0)
    x = 700
    y = 480
    radius = 7
    point_smile = sd.get_point(x, y)
    color_smile = sd.COLOR_BLACK
    sd.circle(point_smile, radius, color_smile, width=0)
    point_list1 = (sd.get_point(x - 8, y), sd.get_point(x - 3, y + 6), sd.get_point(x - 7, y + 11))
    sd.polygon(point_list1, sd.COLOR_BLACK, width=0)
    point_list2 = (sd.get_point(x + 8, y), sd.get_point(x + 3, y + 6), sd.get_point(x + 7, y + 11))
    sd.polygon(point_list2, sd.COLOR_BLACK, width=0)

