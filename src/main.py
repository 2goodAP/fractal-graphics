#!/usr/bin/env python

import sys

import pygame
from pygame.locals import QUIT

import curve_fractals
import line_fractals
import n_flakes


def main():
    pygame.init()
    clock = pygame.time.Clock()
    running = True

    while running:
        print("Choose fractal type:")
        print("1. Koch Snowflake\n2. Fractal Tree\n3. Triflake" +
              "\n4. Vicsek\n5. Rhodonea\n6. Maurer Rose")

        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            choice = KOCH_SNOWFLAKE

        if (choice != KOCH_SNOWFLAKE and choice != FRACTAL_TREE
                and choice != TRIFLAKE and choice != VICSEK
                and choice != MAURER_ROSE and choice != RHODONEA):
            print('error: Invalid choice. Exiting...', file=sys.stderr)
            sys.exit(1)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        if choice == KOCH_SNOWFLAKE:
            window = _window_open("Koch Snowflake")

            line_fractals.draw_koch_snowflake(window, clock, FPS)

            _window_close()
        elif choice == FRACTAL_TREE:
            window = _window_open("Fractal Tree")

            line_fractals.draw_fractal_tree(window, clock, FPS)

            _window_close()
        elif choice == TRIFLAKE:
            window = _window_open("Sierpinski Triangle")

            n_flakes.draw_sierpinski_triangle(window, clock, FPS)

            _window_close()
        elif choice == VICSEK:
            window = _window_open("Vicsek Fractal")

            n_flakes.draw_vicsek_fractal(window, clock, FPS)

            _window_close()
        elif choice == RHODONEA:
            window = _window_open("Rhodonea Rose")

            curve_fractals.draw_rhodonea_rose(window, clock, FPS)

            _window_close()
        else:
            window = _window_open("Maurer Rose")

            curve_fractals.draw_maurer_rose(window, clock, FPS)

            _window_close()


def _window_open(win_name, color=(255, 255, 255)):
    window = pygame.display.set_mode([WINDOW_SIZE, WINDOW_SIZE])
    window.fill((255, 255, 255))
    pygame.display.set_caption(win_name)
    pygame.display.flip()

    return window


def _window_close():
    while True:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

                return


if __name__ == "__main__":
    # Window resolution
    WINDOW_SIZE = 600
    FPS = 120

    KOCH_SNOWFLAKE = 1
    FRACTAL_TREE = 2
    TRIFLAKE = 3
    VICSEK = 4
    RHODONEA = 5
    MAURER_ROSE = 6

    main()
