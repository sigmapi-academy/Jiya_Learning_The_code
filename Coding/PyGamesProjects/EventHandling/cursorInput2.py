import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Unicode Input Example")
user_text = ""
font = pygame.font.Font(None, 36)
while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
       # Handle key presses
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_BACKSPACE:
               user_text = user_text[:-1]
           else:
               # Append the typed character
               user_text += event.unicode
   screen.fill((30, 30, 30))
   text_surface = font.render(user_text, True, (255, 255, 255))
   screen.blit(text_surface, (20, 80))
   pygame.display.flip()