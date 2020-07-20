import simple_draw as sd

N = 15

x_coordinates_list = []
y_coordinates_list = []
length_list = []
for _ in range(N):
    x_coordinates_list.append(sd.random_number(30, 200))
    y_coordinates_list.append(sd.random_number(500, 900))
    length_list.append(sd.random_number(1, 10))

drift = 5


def snow(y_drop):
    drift = 5

    sd.start_drawing()

    for snowflake in range(N):
        point = sd.get_point(x_coordinates_list[snowflake], y_coordinates_list[snowflake])
        sd.snowflake(center=point, length=length_list[snowflake], color=sd.background_color)
        if y_coordinates_list[snowflake] > drift and x_coordinates_list[snowflake] < 300:
            y_coordinates_list[snowflake] -= y_drop
            random_vector = sd.random_number(-8, 8)
            if length_list[snowflake] < 35:
                x_coordinates_list[snowflake] = x_coordinates_list[snowflake] + random_vector * 1.4
            else:
                x_coordinates_list[snowflake] = x_coordinates_list[snowflake] + random_vector
            point_new = sd.get_point(x_coordinates_list[snowflake], y_coordinates_list[snowflake])
            sd.snowflake(center=point_new, length=length_list[snowflake])
        else:
            sd.snowflake(center=point, length=length_list[snowflake])
            x_coordinates_list[snowflake] = sd.random_number(30, 200)
            y_coordinates_list[snowflake] = sd.random_number(500, 900)
            length_list[snowflake] = sd.random_number(1, 10)
            drift += 0.1

    sd.finish_drawing()

    sd.sleep(0.02)
