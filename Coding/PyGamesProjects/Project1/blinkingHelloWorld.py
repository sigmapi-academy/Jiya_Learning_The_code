import pygame
import sys
import random 
# Initialize the game.
pygame.init()

# Initialize the mixer to play sound.
pygame.mixer.init()
pygame.mixer.music.load("PyGamesProjects/Project1/music/sacredmusic.mp3")

# Create the screen.
screen = pygame.display.set_mode((640, 520))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)
HelloWorldColors = [BLACK, RED, GREEN, BLUE]

# Create the font object.
font = pygame.font.Font(None, 32)

# count = 0
while True:
    # count += 1
    screen.fill(WHITE) # Fill the background.
    
    # Check for quit event.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # Create the text surface.
    text = font.render('Hello World', True, HelloWorldColors[random.randint(0,3)])
    
    # Wait one second (or 1000 milliseconds)
    pygame.time.delay(1000)
    
    # # Surround text with black rectangular border.
    # In this case, the top left corner of the rectangle is calculated by subtracting 10 
    # from the coordinates of the center of the screen, and the width and height of the 
    # rectangle is calculated by adding 20 to the width and height of the text surface. 
    # The one argument specifies that the line should be one pixel thick.

    pygame.draw.rect(screen, BLACK, ((screen.get_width() - text.get_width())/2 -10,
                     (screen.get_height() - text.get_height())/2 - 10, text.get_width() + 20,
                     text.get_height() + 20), 1)
    
    # blit the text surface to the center of the screen.
    # Which is calculated by subtracting half of the width and 
    # height of the text surface from the width and height of the screen.
    screen.blit(text, ((screen.get_width()-text.get_width())/2,
                       (screen.get_height() - text.get_height())/2))
    
    # play the music
    pygame.mixer.music.play()
   
    #update the screen
    pygame.display.flip()
    