import pygame
import sys

pygame.init()

res = (720,720)

screen = pygame.display.set_mode(res)

color = (255,255,255) #white

color_light = (170,170,170) #light shade of the button

color_dark = (100,100,100) #dark shade of the button

width = screen.get_width() # Stores the width of the screen into a variable.
height = screen.get_height() # Stores the height of the screen into a variable.

smallfont = pygame.font.SysFont('Arial', 35) # Defining a font.

text = smallfont.render('Hover', True, color)

while True:
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            pygame.quit()
            
        # Check if a mouse is clicked.
        mouse = pygame.mouse.get_pos()
        # Super imposing the text onto our button
        screen.blit(text,(width/2+50, height/2))
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the mouse is clicked the hovering effect we get
            if width/2 <= mouse[0] <= width/2 + 140 and height/2 <= mouse[1] <= height/2 + 40:
                pygame.draw.rect(screen, color_light,[width/2, height/2,140, 40])
            else:
                pygame.draw.rect(screen, color_dark,[width/2, height/2,140,40])
            
        #update the frames of the game
        pygame.display.update()