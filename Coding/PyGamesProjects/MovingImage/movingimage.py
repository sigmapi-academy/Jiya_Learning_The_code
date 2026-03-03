# Approach:
# 	1. Import the library pygame
# 	2. Take the colors as input that we want to use in the game.
# 	3. Then, construct a GUI game.
# 	4. Further, set dimensions of your GUI game.
# 	5. Take the image as input which you want to move with the mouse
# 	6. Moreover, you can make your image look attractive by adding rectangle borders around it.
# 	7. Set the value for running the game and moving value for moving the image.
# 	8. Set the things which you want your app to do when in running state.
# 		a. Once the app is in running state, make it quit if the user wants to quit.
# 		b. In case, the user doesn't want to quit, move your image around the dimensions of the GUI app
# 		c. Next set the moving value as false if you want to move the image only with the mouse click. Else set moving as true if you want to move the image without the mouse click.
# 		d. Further set your image in a moving state if it has been once moved.
# 	9. Next you need to set the screen color and image on the screen.
# 	10. Further, make your image look attractive by constructing the border to the image.
# 	11. Furthermore, update the changes done in the GUI game.
# Finally, quit the GUI game.


import pygame

from pygame.locals import *

YELLOW = (255,255, 0)
BLUE = (0, 0, 255)

pygame.init()

w, h = 840, 600

screen = pygame.display.set_mode((w,h))

img = pygame.image.load('./PyGamesProjects/images/pygame.jpg')
img.convert()

rect = img.get_rect()

rect.center = w//2, h//2

running = True
moving = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
        elif event.type == pygame.MOUSEBUTTONUP:
            moving = False
        elif event.type == pygame.MOUSEMOTION and moving:
            rect.move_ip(event.rel)
    
    screen.fill(YELLOW)
    screen.blit(img, rect)
    pygame.draw.rect(screen, BLUE, rect, 2)
    pygame.display.update()

pygame.quit() 
            