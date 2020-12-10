import math

import pygame


def draw_rhodonea_rose(surface, clock, fps):
    _generate_rose_curve(surface, clock, fps, 71, 6, 200, surface.get_width(),
                         surface.get_height(), (0, 0, 0), False)


def draw_maurer_rose(surface, clock, fps):
    _generate_rose_curve(surface, clock, fps, 71, 6, 200, surface.get_width(),
                         surface.get_height(), (0, 0, 0), True)


def _generate_rose_curve(surf, clk, fps, d, num, size, width, height, color,
                         is_maurer):
    points = []

    for i in range(361):

        if is_maurer:
            k = i * d
        else:
            k = i

        r = size * math.sin(math.radians(num * k))

        x = r * math.cos(math.radians(k))
        y = r * math.sin(math.radians(k))

        points.append((width / 2 + x, height / 2 + y))

    for i in range(1, len(points)):
        pygame.draw.line(surf, color, points[i - 1], points[i])
        clk.tick(fps / 2)
        pygame.display.update()
