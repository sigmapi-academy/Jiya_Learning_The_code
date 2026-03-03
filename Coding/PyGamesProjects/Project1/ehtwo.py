import pygame
import sys

pygame.init()

display = pygame.display.set_mode((300, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print('Key A has been pressed')
                
            if event.key == pygame.K_j:
                print('Key J has been pressed')
            
            if event.key == pygame.K_p:
                print('Key P has been pressed')
                
            if event.key == pygame.K_m:
                print('Key M has been pressed')