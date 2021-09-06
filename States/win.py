import pygame

from States.baseclass import Base
from constants import *
from Functions import *
from Classes.button import Button

class Win(Base):

    def __init__(self):
        super().__init__()

        self.playagain = Button(y=WINDOW_HEIGHT // 2+ 100, color=GREEN, background=BLUE, text="Play Again")
        self.playagain.width = 150
        self.playagain.height = 50
        self.playagain.x = WINDOW_WIDTH // 2 - self.playagain.width // 2
    
    def render(self):
        text, textRect = print_text(size=72, text="Congratulations!", color=GREEN, background=GRAY)
        textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 30)
        SCREEN.blit(text, textRect)

        text, textRect = print_text(36, "You Won", GREEN, GRAY)
        textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 30)
        SCREEN.blit(text, textRect)

        self.playagain.render()

    def update(self):

        if self.playagain.clicked() : GAME_STATE.change("countdown")

        self.render()