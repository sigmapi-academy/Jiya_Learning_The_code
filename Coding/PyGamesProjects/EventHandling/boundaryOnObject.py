import pygame
import random

pygame.init()

# Dimension of the screen.
width = 700
height = 550

# colours
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Bouncy Ball")

# Declare variables for the ball.
ball_X = width/2 - 12
ball_Y = height/2 - 12
ball_XChange = 3 * random.choice((1,-1))
ball_YChange = 3
ballPixel = 24

while True:
    # Background color.
    screen.fill(red)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        # Bouncing the ball.
        if ball_X + ballPixel >= width or ball_X <= 0:
            ball_XChange *= -1
        
        if ball_Y + ballPixel >= height or ball_Y <= 0:
            ball_YChange *= -1
            
        # Moving the ball.
        ball_X += ball_XChange
        ball_Y += ball_YChange
        
        # Drawing the ball.
        ballImg = pygame.draw.circle(screen, green, (int(ball_X), int(ball_Y)), 15)
        
        pygame.display.update()
