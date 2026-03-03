import pygame

pygame.init()

surface = pygame.display.set_mode((800, 500))

pygame.display.set_caption("Sigmapi-Academy")

logo = pygame.image.load("./PyGamesProjects/Project1/images/spa.png")

pygame.display.set_icon(logo) 

surface.fill((0,0,0)) # background color.
pygame.draw.rect(surface, (140,20,150), pygame.Rect(30,30,60,80))

image = pygame.image.load("./PyGamesProjects/Project1/images/image.png")
surface.blit(image, (300,300))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            