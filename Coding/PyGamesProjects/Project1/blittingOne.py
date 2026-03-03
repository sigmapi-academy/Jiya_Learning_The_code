import pygame

pygame.init()

display_surface = pygame.display.set_mode((800, 600))

image1 = pygame.image.load("PyGamesProjects/Project1/images/spa.png")

image2 = pygame.image.load("PyGamesProjects/Project1/images/spa.png")

display_surface.blit(image1, (0,0))

display_surface.blit(image2, (300,300))

pygame.display.flip()
running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
