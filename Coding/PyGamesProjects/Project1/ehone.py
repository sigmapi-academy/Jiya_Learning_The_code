import pygame
import sys

pygame.init()

display = pygame.display.set_mode((300,300))

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Checking if keydown event happened or not.
        if event.type == pygame.KEYDOWN:
            # If key round event happened then printing a string to output.
            print(' A key has been pressed')
    