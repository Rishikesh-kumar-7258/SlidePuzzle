import pygame

from constants import *
from Functions import *

class Block:

    def __init__(self, x=0, y=0, color=GREEN, color2=RED, width=100, height=100, text=0):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.color2 = color2
        self.text = text

    def render(self):
        global SCREEN
        pygame.draw.rect(SCREEN, self.color, [self.x, self.y, self.width, self.height])
        pygame.draw.line(SCREEN, self.color2, (self.x, self.y), (self.x + self.width, self.y))
        pygame.draw.line(SCREEN, self.color2, (self.x, self.y), (self.x, self.y+self.height))
        pygame.draw.line(SCREEN, self.color2, (self.x+self.width, self.y), (self.x + self.width, self.y+self.height))
        pygame.draw.line(SCREEN, self.color2, (self.x, self.y+self.height), (self.x + self.width, self.y+self.height))

        text, textRect = print_text(54, str(self.text), self.color2, self.color)
        textRect.center = (self.x + self.width // 2, self.y + self.height // 2)
        SCREEN.blit(text, textRect)

    def update(self):

        self.render()

    def hover(self):
        x,y = pygame.mouse.get_pos()

        return (x >= self.x and y >= self.y and x <= self.x + self.width and y <= self.y + self.height)
    
    def clicked(self):

        a, b, c = pygame.mouse.get_pressed()

        return self.hover() and a
