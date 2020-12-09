#!/usr/bin/env python

import sys

import pygame
from pygame.locals import QUIT

import line_fractals


def main():
    pygame.init()
    window = pygame.display.set_mode([WINDOW_SIZE, WINDOW_SIZE])
    window.fill((255, 255, 255))
    pygame.display.flip()

    clock = pygame.time.Clock()
    running = True

    while running:
        print('Choose fractal type:')
        print('1. Koch Snowflake\n2. Fractal Tree')

        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            choice = KOCH_SNOWFLAKE

        if choice != KOCH_SNOWFLAKE and choice != FRACTAL_TREE:
            print('error: Invalid choice. Exiting...', file=sys.stderr)
            sys.exit(1)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        clock.tick(FPS)

        window.fill((255, 255, 255))

        if choice == KOCH_SNOWFLAKE:
            line_fractals.draw_koch_snowflake(window, clock, FPS)
        elif choice == FRACTAL_TREE:
            line_fractals.draw_fractal_tree(window, clock, FPS)

        pygame.display.flip()


if __name__ == "__main__":
    # Window resolution
    WINDOW_SIZE = 600
    FPS = 120

    KOCH_SNOWFLAKE = 1
    FRACTAL_TREE = 2

    main()
