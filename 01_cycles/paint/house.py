import simple_draw as sd


def house():
    left_bottom_perimeter = sd.get_point(300, 35)
    right_top_perimeter = sd.get_point(510, 215)
    sd.rectangle(left_bottom_perimeter, right_top_perimeter, sd.COLOR_DARK_RED, 0)

    left_bottom_foundation = sd.get_point(285, 0)
    right_top_foundation = sd.get_point(525, 35)
    sd.rectangle(left_bottom_foundation, right_top_foundation, sd.COLOR_ORANGE, 0)

    point_list = (sd.get_point(285, 215), sd.get_point(525, 215), sd.get_point(410, 430))
    sd.polygon(point_list, sd.COLOR_DARK_RED, width=0)