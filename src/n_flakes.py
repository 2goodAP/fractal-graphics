import math


def _draw_hexaflake(self, steps, rd, ct):
    if steps <= 0:
        pass
    elif steps == 1:
        poly = Polygon(self.num_vertices, rd, ct)
        poly.color = self.COLORS[steps - 1]

        if self.outlined:
            poly.fill = False

        poly.draw(self.screen_ref, 1)
    else:
        if self.colorful:
            poly = Polygon(self.num_vertices, rd, ct)
            poly.color = self.COLORS[steps - 1]

            if self.outlined:
                poly.fill = False

            poly.draw(self.screen_ref, 1)

        self.__draw_hexaflake(steps - 1, rd * self.scale_factor, ct)

        for i in range(0, self.num_vertices):
            cx = (
                ct[0] + rd *
                math.cos(math.radians((self.angle_base) * i + self.ROTATION)) -
                rd * self.scale_factor *
                math.cos(math.radians((self.angle_base) * i + self.ROTATION)))
            cy = (
                ct[1] + rd *
                math.sin(math.radians((self.angle_base) * i - self.ROTATION)) +
                rd * self.scale_factor *
                math.sin(math.radians((self.angle_base) * i + self.ROTATION)))
            self.__draw_hexaflake(steps - 1, rd * self.scale_factor, (cx, cy))


def _draw_pentaflake(self, steps, rd, ct, inv):
    if steps <= 0:
        pass
    elif steps == 1:
        poly = Polygon(self.num_vertices, rd, ct)
        poly.color = self.COLORS[steps - 1]

        if self.outlined:
            poly.fill = False

        poly.draw(self.screen_ref, inv)
    else:
        if self.colorful:
            poly = Polygon(self.num_vertices, rd, ct)
            poly.color = self.COLORS[steps - 1]

            if self.outlined:
                poly.fill = False

            poly.draw(self.screen_ref, inv)

        self.__draw_pentaflake(steps - 1, rd * self.scale_factor, ct, -inv)

        for i in range(0, self.num_vertices):
            cx = (
                ct[0] + rd *
                math.cos(math.radians((self.angle_base) * i + self.ROTATION)) -
                rd * self.scale_factor *
                math.cos(math.radians((self.angle_base) * i + self.ROTATION)))
            cy = (ct[1] + rd * math.sin(
                math.radians((self.angle_base) * i - inv * self.ROTATION)) +
                  inv * rd * self.scale_factor * math.sin(
                      math.radians((self.angle_base) * i + self.ROTATION)))
            self.__draw_pentaflake(steps - 1, rd * self.scale_factor, (cx, cy),
                                   inv)


def _draw_vicsek(self, steps, rd, ct):
    if steps <= 0:
        pass
    elif steps == 1:
        poly = Polygon(self.num_vertices, rd, ct)
        poly.color = self.COLORS[steps - 1]

        if self.outlined:
            poly.fill = False

        poly.draw(self.screen_ref, 1)
    else:
        if self.colorful:
            poly = Polygon(self.num_vertices, rd, ct)
            poly.color = self.COLORS[steps - 1]

            if self.outlined:
                poly.fill = False

            poly.draw(self.screen_ref, 1)

        self.__draw_vicsek(steps - 1, rd * self.scale_factor, ct)

        for i in range(0, self.num_vertices):
            cx = (
                ct[0] + rd *
                math.cos(math.radians((self.angle_base) * i + self.ROTATION)) -
                rd * self.scale_factor *
                math.cos(math.radians((self.angle_base) * i + self.ROTATION)))
            cy = (
                ct[1] + rd *
                math.sin(math.radians((self.angle_base) * i - self.ROTATION)) +
                rd * self.scale_factor *
                math.sin(math.radians((self.angle_base) * i + self.ROTATION)))
            self.__draw_vicsek(steps - 1, rd * self.scale_factor, (cx, cy))


def _draw_nflake(self, steps, rd, ct):
    if steps <= 0:
        pass
    elif steps == 1:
        poly = Polygon(self.num_vertices, rd, ct)
        poly.color = self.COLORS[steps - 1]

        if self.outlined:
            poly.fill = False

        poly.draw(self.screen_ref, 1)
    else:
        if self.colorful:
            poly = Polygon(self.num_vertices, rd, ct)
            poly.color = self.COLORS[steps - 1]

            if self.outlined:
                poly.fill = False

            poly.draw(self.screen_ref, 1)

        for i in range(0, self.num_vertices):
            cx = (
                ct[0] + rd *
                math.cos(math.radians((self.angle_base) * i + self.ROTATION)) -
                rd * self.scale_factor *
                math.cos(math.radians((self.angle_base) * i + self.ROTATION)))
            cy = (
                ct[1] + rd *
                math.sin(math.radians((self.angle_base) * i - self.ROTATION)) +
                rd * self.scale_factor *
                math.sin(math.radians((self.angle_base) * i + self.ROTATION)))

            self.__draw_nflake(steps - 1, rd * self.scale_factor, (cx, cy))


def _get_scale_factor(self):
    aux = 0

    for i in range(0, self.num_vertices // 4):
        aux += math.cos(2 * math.pi * (i + 1) / self.num_vertices)
    self.scale_factor = 1 / (2 * (1 + aux))
