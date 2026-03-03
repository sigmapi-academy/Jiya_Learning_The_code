import pygame
import random

# Global variables.

COLOR = (255, 100, 98)
SURFACE_COLOR = (167,255,100)
WIDTH = 500
HEIGHT = 500

# Object class.
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)
        
        # pygame.draw.rect(self.image, color, pygame.Rect(0,0,width, height))
        # Define triangle points (pointing upwards)
        points = [
            (width // 2, 0),        # Top middle
            (0, height),            # Bottom left
            (width, height)         # Bottom right
        ]

        pygame.draw.polygon(self.image, color, points)
        
        self.rect = self.image.get_rect()
        
    def moveRight(self, pixels):
        self.rect.x += pixels
        
    def moveLeft(self, pixels):
        self.rect.x -= pixels
        
    def moveForward(self, speed):
        self.rect.y += speed * speed/10
        
    def moveBack(slef, speed):
        slef. rect.y -= speed * speed/10
        
pygame.init()

RED=(255,0,0)
size=(WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")

all_sprite_list = pygame.sprite.Group()

playerCar = Sprite(RED, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300

all_sprite_list.add(playerCar)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(10)
    
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(10)
    
    if keys[pygame.K_DOWN]:
        playerCar.moveForward(10)
    
    if keys[pygame.K_UP]:
        playerCar.moveBack(10)
    
    
    all_sprite_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    