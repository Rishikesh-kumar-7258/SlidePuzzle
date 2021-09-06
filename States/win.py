import pygame

from States.baseclass import Base
from constants import *

class Win(Base):

    def __init__(self):
        super().__init__()

    
    def render(self):
        font = pygame.font.SysFont("Comic sans MS", 72)
        font1 = pygame.font.SysFont("Comic sans MS", 36)
        text = font.render("Congruatulations!", True, GREEN, GRAY)
        text1 = font1.render("You Won", True, GREEN, GRAY)
        textRect = text.get_rect()
        textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 30)
        textRect1 = text1.get_rect()
        textRect1.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 30)
        SCREEN.blit(text, textRect)
        SCREEN.blit(text1, textRect1)

    def update(self):

        self.render()