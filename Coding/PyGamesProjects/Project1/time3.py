import pygame
import mymodule
pygame.init()

display = pygame.display.set_mode((700,700))
image = pygame.image.load("Project1/images/MickeyMouse.png")

display.blit(image, (10,10))

pygame.time.delay(5000)

while True:
    mymodule.quitFromApp()
    
    pygame.display.flip()