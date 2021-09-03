import pygame

pygame.init()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Slide Blocks")


def main():

    GAME_OVER = False

    while not GAME_OVER:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

if __name__ == "__main__":
    main()

pygame.quit()
quit()