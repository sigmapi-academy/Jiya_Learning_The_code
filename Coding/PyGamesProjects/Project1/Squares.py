import pygame

from pygame.locals import *

# Define our Square object and call super two. Give it all the properties and methods of 
# pygame.sprite.Sprite.
# Define the class for our square objects.
class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
        
        # Define the dimension of the surface.
        # Here we are making squares of side 25PX.
        self.surf = pygame.Surface((25,25))
        
        # Define the color of the surface using RGB color coding.
        self.surf.fill((0,200,255))
        
        self.rect = self.surf.get_rect()
        

#initialize pygame

pygame.init()

# Define the dimension of screen object.

screen = pygame.display.set_mode((800,600))

sq1 = Square()
sq2 = Square()
sq3 = Square()
sq4 = Square()

# Variable to keep our game loop running.
gameOn = True     
# Our game loop.
while gameOn:
    # For loop through the event queue.
    for event in pygame.event.get():
        # Check the key down event.
        if event.type == KEYDOWN:
            # If the backspace key has been pressed, set. 
            # Running two false to exit the main loop.
            if event.key == K_BACKSPACE:
                gameOn = False
            elif event.type == pygame.QUIT:
                gameOn = False
        
        # Define where the squares will appear on the screen.
        # Use blitz to draw them on the screen surface.
        screen.blit(sq1.surf,(40,40))
        screen.blit(sq1.surf,(40, 530))
        screen.blit(sq1.surf,(730,40))
        screen.blit(sq1.surf,(730, 530))
        
        #Update the display using flip
        pygame.display.flip()
        