import pygame
import random

from States.baseclass import Base
from constants import *
from Classes.blocks import Block
from Functions import *

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

        self.blank = (420, 340)
        self.width = 100
        self.height = 100

        self.moves_count = 0


    def render(self):
        global SCREEN, BLACK
        pygame.draw.rect(SCREEN, BLACK, [120, 40, 400, 400])

        for i in range(15):
            self.block_array[i].render()
        
        text, textRect = print_text(24, f"Moves : {str(self.moves_count)}", BLUE, GRAY)
        textRect.x = 5
        textRect.y = 5
        SCREEN.blit(text, textRect)

    def update(self):

        for block in self.block_array:
            if block.clicked():
                can_move = self.get_can_move()
                if (block.x, block.y) in can_move:
                    temp = self.blank
                    self.blank = (block.x, block.y)
                    block.x = temp[0]
                    block.y = temp[1]
                    self.moves_count += 1

        if (self.won() and self.blank == (420, 340)) : GAME_STATE.change("win")
        self.render()
    
    def get_can_move(self):
        l = []
        l.append((self.blank[0] + self.width, self.blank[1]))
        l.append((self.blank[0] - self.width, self.blank[1]))
        l.append((self.blank[0], self.blank[1] + self.height))
        l.append((self.blank[0], self.blank[1] - self.height))

        return l
    
    def won(self):
        
        l = Pivot_sort(self.block_array)
        
        for i in range(len(l)-1):
            if (int(l[i].text) > int(l[i+1].text)) : return False
        
        return True
    
    def enter(self):
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

        self.blank = (420, 340)
        self.width = 100
        self.height = 100

        self.moves_count = 0