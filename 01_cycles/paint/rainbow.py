import simple_draw as sd


def rainbow(color_index):
    rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]

    radius = 880
    rainbow_colors = rainbow_colors[color_index:] + rainbow_colors[:color_index]
    for color in rainbow_colors:
        radius += 15
        point = sd.get_point(370, -200)
        sd.circle(point, radius, color, 15)

    sd.sleep(0.05)
