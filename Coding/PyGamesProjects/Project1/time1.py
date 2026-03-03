import pygame

import mymodule

pygame.init()

display = pygame.display.set_mode((500,500))

image = pygame.image.load('Project1/images/image.png')

display.blit(image, (100, 100))

pygame.time.wait(5000)

while True:
    mymodule.quitFromApp()

    pygame.display.flip()

    