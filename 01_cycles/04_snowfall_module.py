# -*- coding: utf-8 -*-

import simple_draw as sd
from paint.snowfall_engine import snowflake_gen, snowflake_color, snowflake_shift, check_snowflakes, \
    snowflake_background, snowflake_freeze

sd.resolution = (1200, 600)
# Сделать функции отрисовки снегопада

snowflake_gen(20)
while True:
    sd.start_drawing()
    snowflake_background(color=sd.background_color)
    snowflake_shift()
    snowflake_color()
    if check_snowflakes():
        snowflake_freeze(snowflakes_freeze=check_snowflakes())
    sd.finish_drawing()
    sd.sleep(0.09)
    if sd.user_want_exit():
        break

sd.pause()

