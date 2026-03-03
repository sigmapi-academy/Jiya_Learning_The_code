import pygame

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Moving rectangle")

# object current co-ordinates
x = 200
y = 200

# dimension of the object
width = 20
height = 20

# velocity/speed of movement
vel = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        # stores keys pressed
        keys = pygame.key.get_pressed() 
        
        # if left arrow key is pressed
        if keys[pygame.K_LEFT] and x > 0:
            x -= vel   #decrement the x co-ordinate
            
        # if right arrow key is pressed
        if keys[pygame.K_RIGHT] and x < 500 - width:
            x += vel # increment in x co-ordinate
        
        #if up arrow key is pressed
        if keys[pygame.K_UP] and y > 0:
            y -= vel # deccrement the value of y co-ordinate
        
        # if down arrow key is pressed
        if keys[pygame.K_DOWN] and y < 500 - height:
            y += vel    #increment the value of y co-ordinate
            
        # Completely fill the surface object with black color.
        win.fill((0,0,0))
        
        # Drawing object on screen which is a rectangle here.
        pygame.draw.rect(win,(255,0,0),(x,y,width, height))
        
        # It refreshes the window.
        pygame.display.update()