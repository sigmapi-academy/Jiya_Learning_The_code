import pygame

pygame.init()

win = pygame.display.set_mode((720, 500))

pygame.display.set_caption("Moving rectangle")

# Marker current coordinates.

x = 200
y = 200

# Dimension of the marker.
width = 10
height = 10

# Velocity or speed of movement?
vel = 10

while True:
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quiting the game
        
        keys = pygame.key.get_pressed()
        # If left arrow key is pressed.
        if keys[pygame.K_LEFT] and x > 0:
            x -= vel # Decrement in X coordinate.
        # If right arrow key is pressed.
        if keys[pygame.K_RIGHT] and x < 720 - width:
            x += vel #increment in x-coordinate
        # If up arrow key is pressed.
        if keys[pygame.K_UP] and y > 0:
            y -= vel # Decrement in Y coordinate.
        # If down arrow key is pressed.
        if keys[pygame.K_DOWN] and y < 500 - height:
            y += vel # Increment in Y coordinate.
        
        # Drawing spot on screen which is rectangle here.
        pygame.draw.rect(win, (255,0,0),(x,y,width, height))
        
        pygame.display.update() # It refreshes the window.