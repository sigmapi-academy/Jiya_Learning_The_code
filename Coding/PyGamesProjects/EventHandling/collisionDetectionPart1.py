import pygame
import random

pygame.init()

# Dimension of the screen.
width = 650
height = 700

# colours
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

#size of block
pixel = 64
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Corona Scarper")

gameIcon = pygame.image.load("./images/pygame.jpg")

pygame.display.set_icon(gameIcon)

backgroundImg = pygame.image.load("./images/wallBackground.jpg")

playerImage = pygame.image.load("./images/player.jpg")

playerXPosition = (width/2) - (pixel/2)
playerYPosition = height - pixel - 10

playerXPositionChange = 0

# Define a function for setting the image at particular coordinates.
def player(x, y):
    screen.blit(playerImage,(x, y))
    
blockImage = pygame.image.load("./images/pygame.jpg")

blockXPosition = random.randint(0, (width - pixel))

blockYPosition = 0 - pixel

# Set the speed of the block.
blockXPositionChange = 0
blockYPositionChange = 2

# Define a function for setting the image at particular coordinates.
def block(x, y):
    screen.blit(blockImage, (x,y))
    
# Define a function for collision detection.
def crash():
    #take a global variable
    global blockYPosition
    
    #check conditions
    if playerYPosition < (blockYPosition + pixel):
        if ((playerXPosition > blockXPosition) 
            and playerXPosition < (blockXPosition + pixel)) or ((playerXPosition + pixel) > blockXPosition and (playerXPosition + pixel) < (blockXPosition + pixel)):
            blockYPosition = height + 1000


while True:
    screen.blit(backgroundImg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerXPositionChange = 3
            if event.key == pygame.K_LEFT:
                playerXPositionChange = -3
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                playerXPositionChange = 0
                
    # Boundaries to the player
    #if it comes at right end,
    #stay at right end does noy exceed
    
    if playerXPosition >= (width - pixel):
        playerXPosition = width - pixel
        
    # If it comes at left end, stay at left end and does not exceed.
    if playerXPosition <= 0:
        playerXPosition = 0
    
    # Multiple blocks movement after each other and 
    # condition used because of game over function.
    if (blockYPosition >= height and blockYPosition <= (height + 200)):
        blockYPosition = 0 - pixel
    
    # Randomly assign value in range.
    blockXPosition = random.randint(0, (width - pixel))
    
    # Movement of player
    playerXPosition += playerXPositionChange
    
    #Movement of the block
    blockYPosition += blockYPositionChange
    
    #player Function call
    player(playerXPosition, playerYPosition)
    
    #block function call
    block(blockXPosition, blockYPosition)
    
    #crash function call
    crash()
    
    pygame.display.update()