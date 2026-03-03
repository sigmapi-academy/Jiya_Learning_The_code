import pygame

pygame.init()

surface = pygame.display.set_mode((1000, 600))

color = (100, 25, 150)
surface.fill(color)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False