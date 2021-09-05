import pygame 

from statemachine import StateMachine

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Slide Blocks")

GAME_STATE = StateMachine()

# Colors
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()