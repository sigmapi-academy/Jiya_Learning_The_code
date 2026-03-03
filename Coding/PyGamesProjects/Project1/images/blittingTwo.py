import pygame

pygame.init()

display_surface = pygame.display.set_mode((720, 700), pygame.RESIZABLE)

# image1 = pygame.image.load("PyGamesProjects/Project1/images/spa.png")

# image2 = pygame.image.load("PyGamesProjects/Project1/images/spa.png")

# display_surface.blit(image1, (0,0))

# display_surface.blit(image2, (300,300))

# pygame.Surface.convert_alpha(display_surface)

# copy_surface = pygame.Surface.copy(display_surface)
image1 = pygame.image.load("PyGamesProjects/Project1/images/MickeyMouse.png")
# pygame.Surface.set_colorkey(image1, [255,255,255])
# pygame.Surface.set_alpha(image1, 255)
print(pygame.Surface.get_alpha(image1))
display_surface.blit(image1, (50, 50))
pygame.display.flip()
running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
