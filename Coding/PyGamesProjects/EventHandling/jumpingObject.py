import pygame

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Jump Game")

x = 200
y = 200

width = 30
height = 40

isjump = False

v = 5
m = 1

while True:
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0),(x,y,width,height))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        #stores key pressed
        keys = pygame.key.get_pressed()
        
        if isjump == False:
            # if space bar is pressed
            if keys[pygame.K_SPACE]:
                # make isjump equal to True
                isjump = True
            
        if isjump:
            # calculate force(F) = 1/2*mass*velocity^2
            F = (1/2)*m*(v**2)
            
            # change in the y co-ordinate
            y -= F
            
            # Decreasing velocity while going up and become negative while coming down.
            v -= 1
            
            # object reached its maximum height
            if v < 0:
                # Negative sign is added to counter negative velocity.
                m = -1
            # Object reaches its original state
            if v == -6:
                isjump = False
                
                # Setting original values to v and m.
                v = 5 
                m = 1
            
        pygame.time.delay(50)
        pygame.display.update()