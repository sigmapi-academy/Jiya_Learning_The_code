import pygame
import sys
# Initialize the game.
pygame.init()

# Create the screen.
gameWindow = pygame.display.set_mode((320,240))

WHITE = (255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    gameWindow.fill(WHITE)
    # pygame.display.flip()
