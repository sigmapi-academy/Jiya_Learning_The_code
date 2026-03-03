import pygame
import sys

pygame.font.init()

print(pygame.font.get_init())

display_surface = pygame.display.set_mode((500,500))

pygame.display.set_caption('Our Text')

font1 = pygame.font.SysFont('Arial.ttf', 50)
font2 = pygame.font.SysFont('LiberationSans-Regular.ttf', 40)

text1 = font1.render('Sigmapi-Academy',True, (0,255, 0))
text2 = font2.render('Sigmapi-Academy',True, (0,255, 0))

textRect1 = text1.get_rect()
textRect2 = text2.get_rect()

textRect1.center = (250, 250)
textRect2.center = (250, 300)

while True:
    
    display_surface.fill((200,150,20))
    
    display_surface.blit(text1, textRect1)
    display_surface.blit(text2, textRect2)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()