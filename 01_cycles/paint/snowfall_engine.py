import simple_draw as sd

x_coordinates_list = []
y_coordinates_list = []
length_list = []


def snowflake_gen(N):
    for _ in range(N):
        x_coordinates_list.append(sd.random_number(-20, 1200))
        y_coordinates_list.append(sd.random_number(500, 900))
        length_list.append(sd.random_number(10, 100))


def snowflake_background(color):
    for snowflake in range(len(x_coordinates_list)):
        point = sd.get_point(x_coordinates_list[snowflake], y_coordinates_list[snowflake])
        sd.snowflake(center=point, length=length_list[snowflake], color=color)


def snowflake_color():
    for snowflake in range(len(x_coordinates_list)):
        point_new = sd.get_point(x_coordinates_list[snowflake], y_coordinates_list[snowflake])
        sd.snowflake(center=point_new, length=length_list[snowflake])


def snowflake_shift():
    for snowflake in range(len(x_coordinates_list)):
        y_coordinates_list[snowflake] -= 10
        random_vector = sd.random_number(-3, 3)
        if length_list[snowflake] < 35:
            x_coordinates_list[snowflake] = x_coordinates_list[snowflake] + abs(random_vector) * 1.3
        else:
            x_coordinates_list[snowflake] = x_coordinates_list[snowflake] + random_vector


def snowflake_freeze(snowflakes_freeze):
    for it_snowflake_stop in snowflakes_freeze:
        point = sd.get_point(x_coordinates_list.pop(it_snowflake_stop), y_coordinates_list.pop(it_snowflake_stop))
        sd.snowflake(center=point, length=length_list.pop(it_snowflake_stop))
        x_coordinates_list.insert(it_snowflake_stop, sd.random_number(-20, 1200))
        y_coordinates_list.insert(it_snowflake_stop, sd.random_number(500, 900))
        length_list.insert(it_snowflake_stop, sd.random_number(10, 100))


def check_snowflakes():
    freeze_list = []
    for snowflake in range(len(x_coordinates_list)):
        if y_coordinates_list[snowflake] < 50:
            freeze_list.append(snowflake)
    return freeze_list
