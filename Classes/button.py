import pygame

from constants import *
from Functions import *

class Button:

    def __init__(self, x=0, y=0, color=WHITE, background=BLACK, width=60, height=20, text="Button"):
        
        self.x = x
        self.y = y
        self.color = color
        self.background = background
        self.width = width
        self.height = height
        self.text = text

    def render(self): 
        pygame.draw.rect(SCREEN, self.background, [self.x, self.y, self.width, self.height])
        text, textRect = print_text(self.height // 2, self.text, self.color, self.background)
        textRect.center = (self.x + self.width // 2, self.y + self.height // 2)

        SCREEN.blit(text, textRect)

    def update(self) :
        self.render()
    
    def hover(self):

        x,y = pygame.mouse.get_pos()

        return (x >= self.x and y >= self.y and x <= self.x + self.width and y <= self.y + self.height)
    
    def clicked(self):

        a, b, c = pygame.mouse.get_pressed()

        return (self.hover() and a)