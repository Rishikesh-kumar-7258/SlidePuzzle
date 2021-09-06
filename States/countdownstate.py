import pygame
import time

from Functions import *
from States.baseclass import Base
from constants import *

class CountDown(Base):

    def __init__(self):
        super().__init__()

        self.count = 4

    
    def render(self):
        text, textRect = print_text(100, str(self.count), RED, GRAY)
        textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        SCREEN.blit(text, textRect)

    def update(self):

        self.count -= 1
        pygame.time.wait(1000)

        if self.count <= 0 : GAME_STATE.change("play")

        self.render()

    def enter(self):
        self.count = 4