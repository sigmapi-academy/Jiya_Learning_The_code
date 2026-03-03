import pygame


pygame.init()

i = 0

while i < 5:
    ticks = pygame.time.get_ticks()
    print(ticks)
    i += 1
    pygame.time.wait(1000)