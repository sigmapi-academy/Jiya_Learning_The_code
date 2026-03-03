def quitFromApp():
    import pygame
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # to quit pygame library
            quit() #to quit python execution environment.

