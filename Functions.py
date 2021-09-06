import pygame
def Pivot_sort(arr):

    if (len(arr) < 2) : return arr

    pivot = arr[0]

    left = []
    right = []

    for a in arr:
        if a.y > pivot.y : right.append(a)
        elif a.y < pivot.y : left.append(a)
        else : 
            if a.x > pivot.x : right.append(a)
            elif a.x < pivot.x : left.append(a)
    
    left = Pivot_sort(left)
    right = Pivot_sort(right)

    left.append(pivot)
    left.extend(right)
    
    return left


def print_text(size=24, text="", color=(255, 255, 255), background=(0, 0, 0)):

    font = pygame.font.SysFont("Comic sans MS", size)
    text = font.render(text, True, color, background)
    textRect = text.get_rect()

    return (text, textRect)