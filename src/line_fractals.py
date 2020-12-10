"""
Module to draw line fractals
"""
import math

import pygame

# some constants
MIN_LINE_LENGTH = 1  # when to terminate recursion


def draw_koch_snowflake(surface, clock, fps):
    surface.fill([255, 255, 255])
    # calculate the three corners of the snowflake,
    # an equilateral triangle centered on the screen
    screen_center = pygame.Vector2(surface.get_width() / 2,
                                   surface.get_height() / 2)
    # Distance from center to edge
    radius = surface.get_width() / 2
    snowflake_top = screen_center + _vector_from_polar(radius, 90)
    snowflake_left = (screen_center + _vector_from_polar(radius, 90 + 120))
    snowflake_right = (screen_center + _vector_from_polar(radius, 90 + 240))

    _generate_koch_line(surface, clock, fps, snowflake_top, snowflake_left)
    _generate_koch_line(surface, clock, fps, snowflake_left, snowflake_right)
    _generate_koch_line(surface, clock, fps, snowflake_right, snowflake_top)


def draw_fractal_tree(surface, clock, fps):
    start = pygame.Vector2(surface.get_width() / 2,
                           3 * surface.get_height() / 4)

    _generate_tree_line(surface, clock, fps, start, -90, 9)


def _generate_koch_line(surf, clock, fps, start, end):
    if (end - start).magnitude() / 3 < MIN_LINE_LENGTH:
        # last iteration: draw the line
        pygame.draw.line(surf, (0, 0, 0), start, end)
        clock.tick(fps)
        pygame.display.update()
    else:
        normal = pygame.Vector2(end.y - start.y, start.x - end.x)
        # find three points for the line segments
        left = 2 / 3 * start + 1 / 3 * end
        right = 1 / 3 * start + 2 / 3 * end
        top = (1 / 2 * start + 1 / 2 * end + math.sqrt(3) / 2 / 3 * normal)

        _generate_koch_line(surf, clock, fps, start, left)
        _generate_koch_line(surf, clock, fps, left, top)
        _generate_koch_line(surf, clock, fps, top, right)
        _generate_koch_line(surf, clock, fps, right, end)


def _generate_tree_line(surf, clk, fps, start, angle, depth):
    if depth > 0:
        end = pygame.Vector2(
            start.x + int(math.cos(math.radians(angle)) * depth * 10),
            start.y + int(math.sin(math.radians(angle)) * depth * 10))

        pygame.draw.line(surf, (0, 0, 0), start, end)
        clk.tick(fps)
        pygame.display.update()

        _generate_tree_line(surf, clk, fps, end, angle - 30, depth - 1)
        _generate_tree_line(surf, clk, fps, end, angle + 30, depth - 1)


# Constructs a vector from its angle and mangitude
def _vector_from_polar(magnitude, angle_deg):
    return (magnitude * pygame.Vector2(math.cos(math.radians(angle_deg)),
                                       math.sin(math.radians(angle_deg))))
