import game.wrapped_flappy_bird as game
import pygame
from pygame.locals import *
import sys


def main():
    action_terminal = game.GameState()

    while True:
        # input_actions[0] == 1: do nothing
        # input_actions[1] == 1: flap the bird
        input_actions = [1, 0]
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                input_actions = [0, 1]
            else:
                input_actions = [1, 0]

        action_terminal.frame_step(input_actions)


if __name__ == '__main__':
    # ручная игра
    main()
