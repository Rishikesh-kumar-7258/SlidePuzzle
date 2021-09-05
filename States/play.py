import pygame
import random

from States.baseclass import Base
from constants import *
from Classes.blocks import Block

class Play(Base):

    def __init__(self):
        super().__init__()

        self.block_array = []
        for i in range(4):
            for j in range(4):
                block = Block(120+j*100, 40+i*100)
                self.block_array.append(block)
        
        self.block_array.pop()

        self.num_array = []
        for i in range(15):
            self.num_array.append(i+1)

        random.shuffle(self.num_array)

        for i in range(15):
            self.block_array[i].text = self.num_array[i]


    def render(self):
        global SCREEN, BLACK
        pygame.draw.rect(SCREEN, BLACK, [120, 40, 400, 400])

        for i in range(15):
            self.block_array[i].render()

    def update(self):

        self.render()   