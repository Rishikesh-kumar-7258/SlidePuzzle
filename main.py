import pygame

from statemachine import StateMachine
from States.play import Play
from constants import *

pygame.init()


def main():

    global WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN, GAME_STATE

    STATES = {
    "play" : Play()
    }
    GAME_STATE.states = STATES
    GAME_STATE.change("play")

    GAME_OVER = False

    while not GAME_OVER:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

                
        SCREEN.fill(GRAY)
        GAME_STATE.update()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

pygame.quit()
quit()