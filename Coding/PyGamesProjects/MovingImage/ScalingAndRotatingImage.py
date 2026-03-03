# 1. Frist import the libraries Pygame and math

import pygame
import math
from pygame.locals import *

# 2 Now take the colors as input that we want to use in the game.

RED = (255, 0, 0)
BLACK = (0,0,0)
YELLOW = (255,255, 0)

# 3: Then initialize the constructor
pygame.init()

# 4: Set the dimensions of your GUI game.
w, h = 600, 400 # WIdth dimension, height dimension

screen = pygame.display.set_mode((w,h))

#5: Set the running value for running the game,
# The angle by which it can be moved.

running = True
angle = 0
scale = 1

# 6: Next take the image as input which we want to move with the mouse.
img_logo = pygame.image.load('./PyGamesProjects/images/pygame.jpg')
img_logo = img_logo.convert()

#7: Draw a border around an image.
rect_logo = img_logo.get_rect()
pygame.draw.rect(img_logo, RED, rect_logo, 1)

# 8: Locate the center of the GUI game and get the position of the mouse.
center = w//2, h//2
mouse = pygame.mouse.get_pos()

# 9: Store the image in a new variable and construct a rectangle around the image.
img = img_logo
rect = img.get_rect()
rect.center = center

#10: Set the things which you want your app to do when in a running state.
while running:
    for event in pygame.event.get():
        # 10.1: Once the app is in running state, make it quit if the user wants to quit.
        if event.type == pygame.QUIT:
            running = False
        # 10.2: In case the user doesn't want to quit. 
        # Set at what angle the image should rotate.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                if event.mod & pygame.KMOD_SHIFT:
                    angle -= 5 #moving left
                else:
                    angle += 5 #moving right
            # 10.3: Also set at what ratio the image size should increase or decrease.
            elif event.key == pygame.K_s:
                if event.mod & pygame.KMOD_SHIFT:
                    scale /= 1.5 # Scale at which the image size should decrease.
                else:
                    scale *= 1.5 # Scale at which the image size should increase.
        # 10.4: Set at what coordinates, angle and scale the image will rotate or resize.
        elif event.type == pygame.MOUSEMOTION:
            # 10.4.1: Store the current position of the event in the new variable.
            mouse = event.pos
            
            #10.4.2: Locate the cartesian coordinates with the help of a 
            # mouse variable and center of the image for rotating the image.
            x = mouse[0] - center[0]
            y = mouse[1] - center[1]
            
            # 10.4.3: Further calculate the distance between the two points(0,0) and
            # (x,y) with the help of formula sqrt(x**2 + y**2)
            d = math.sqrt(x**2 + y**2)
            
            # 10.4.5: Calculate which scale the image size should decrease or 
            # increase using the function ABS. Which returns the magnitude 
            # of the number.
            scale = abs(5*d/w)
            
            # 10.4.6: Calculate the updated position of the image in the running 
            # state using the rotozoom function, which is a combined scale and
            # rotation transform.
            img = pygame.transform.rotozoom(img_logo, angle, scale)
            
            # 10.4.7: Construct the rectangle around the updated image.
            rect = img.get_rect()
            rect.center = center
        
    # 11: Next you need to set the screen color and the image on the screen.
    screen.fill(YELLOW)
    screen.blit(img, rect)
    
    # 12: Later on draw the rectangle, line and circle. Which will help 
    # in moving the image.
    pygame.draw.rect(screen, BLACK, rect, 3)
    pygame.draw.line(screen, RED, center, mouse, 2)
    pygame.draw.circle(screen, YELLOW, mouse, 6, 2)
    pygame.draw.circle(screen, BLACK, mouse, 6, 2)
    # 13: Furthermore, update the changes done in the GUI game.
    pygame.display.update()

pygame.quit()