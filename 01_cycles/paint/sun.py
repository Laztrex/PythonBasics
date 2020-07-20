import simple_draw as sd


class SunPainting:

    ANGLES = None

    def __init__(self, offset_ray):
        self.offset_ray = offset_ray
        self.point_centre = sd.get_point(480, 505)

    def body_sun(self):
        sd.circle(self.point_centre, 50, sd.COLOR_ORANGE, 0)

    def sun_core(self):
        sd.start_drawing()

        if self.ANGLES is None:
            self.ANGLES = [angle for angle in range(0, 361, 10)]
        for num_ray, angle in enumerate(self.ANGLES):
            sd.vector(self.point_centre, angle=self.ANGLES[num_ray], length=90, color=sd.background_color, width=3)
            angle += 3
            self.ANGLES[num_ray] = angle
            sd.vector(self.point_centre, angle=angle, length=90, width=3)
            self.body_sun()

        sd.finish_drawing()


sd.sleep(0.02)
