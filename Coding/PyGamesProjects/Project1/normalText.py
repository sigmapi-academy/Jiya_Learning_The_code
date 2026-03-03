import pygame
import sys

# Initialize the game.
pygame.init()

# Create the screen.
screen = pygame.display.set_mode((320, 240))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the font object.
font = pygame.font.Font(None, 32)

while True:
    screen.fill(WHITE) # Fill the background.
    
    # Check for quit event.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # Create the text surface.
    text = font.render('Hello World', True, BLACK)
    
    # blit the text surface to the center of the screen.
    # Which is calculated by subtracting half of the width and 
    # height of the text surface from the width and height of the screen.
    screen.blit(text, ((screen.get_width()-text.get_width())/2,
                       (screen.get_height() - text.get_height())/2))
    #update the screen
    pygame.display.flip()
    