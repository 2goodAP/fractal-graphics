import math

import pygame


def draw_sierpinski_triangle(surface, clock, fps):
    _generate_sierpinski_triangle(
        surface, clock, fps, 8,
        surface.get_width() / 2,
        pygame.Vector2(surface.get_width() / 2,
                       surface.get_height() / 2))


def draw_vicsek_fractal(surface, clock, fps):
    _generate_vicsek_fractal(
        surface, clock, fps, 8,
        surface.get_width() / 2,
        pygame.Vector2(surface.get_width() / 2,
                       surface.get_height() / 2))


class _Polygon:
    def __init__(self, n_verts, rad, center):
        self.n_vertices = n_verts
        self.radius = rad
        self.center = center
        self.angle_base = 360 / self.n_vertices
        self.color = (0, 0, 0)

    def draw(self, surf, clk, fps, inv=1):
        coords = []

        for i in range(self.n_vertices):
            cx = round(self.center[0] + self.radius *
                       math.cos(math.radians(self.angle_base * i + 90)))
            cy = round(self.center[1] - inv * self.radius *
                       math.sin(math.radians(self.angle_base * i + 90)))
            coords.append(pygame.Vector2(cx, cy))

        pygame.draw.polygon(surf, self.color, coords)
        pygame.display.update()


def _generate_sierpinski_triangle(surf, clk, fps, steps, radius, center):
    if steps <= 0:
        return

    scale_factor = _get_scale_factor(3)
    poly = _Polygon(3, radius, center)

    if steps == 1:
        poly.draw(surf, clk, fps)
        poly.color = (255, 255, 255)
        clk.tick(fps)
    else:
        for i in range(3):
            cx = (center[0] + radius * math.cos(math.radians(120 * i + 90)) -
                  radius * scale_factor * math.cos(math.radians(120 * i + 90)))
            cy = (center[1] + radius * math.sin(math.radians(120 * i - 90)) +
                  radius * scale_factor * math.sin(math.radians(120 * i + 90)))

            _generate_sierpinski_triangle(surf, clk, fps, steps - 1,
                                          radius * scale_factor,
                                          pygame.Vector2(cx, cy))


def _generate_vicsek_fractal(surf, clk, fps, steps, radius, center):
    if steps <= 0:
        return

    scale_factor = 1 / 3
    poly = _Polygon(4, radius, center)

    if steps == 1:
        poly.draw(surf, clk, fps)
    else:
        _generate_vicsek_fractal(surf, clk, fps, steps - 1,
                                 radius * scale_factor, center)

        for i in range(4):
            cx = (center[0] + radius * math.cos(math.radians(90 * i + 90)) -
                  radius * scale_factor * math.cos(math.radians(90 * i + 90)))
            cy = (center[1] + radius * math.sin(math.radians(90 * i - 90)) +
                  radius * scale_factor * math.sin(math.radians(90 * i + 90)))

            _generate_vicsek_fractal(surf, clk, fps, steps - 1,
                                     radius * scale_factor,
                                     pygame.Vector2(cx, cy))


def _get_scale_factor(n_verts):
    aux = 0

    for i in range(0, n_verts // 4):
        aux += math.cos(2 * math.pi * (i + 1) / n_verts)

    return 1 / (2 * (1 + aux))
