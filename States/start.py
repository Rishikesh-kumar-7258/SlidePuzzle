import pygame

from States.baseclass import Base
from constants import *
from Functions import *
from Classes.button import Button

class Start(Base):

    def __init__(self):
        super().__init__()

        self.startBtn = Button(y=WINDOW_HEIGHT // 2 + 100, text="Start", color=RED, background=GREEN, width=100, height=40)
        self.startBtn.x = WINDOW_WIDTH // 2 - self.startBtn.width // 2
    
    def render(self):
        
        text, textRect = print_text(size=72, text="SlidePuzzle", color=BLUE, background=GRAY)
        textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        SCREEN.blit(text, textRect)

        self.startBtn.render()

    def update(self):

        if self.startBtn.clicked() : GAME_STATE.change("countdown")

        self.render()