import pygame


pygame.init()

i = 0

clock = pygame.time.Clock() # Creating a Clock object.

while i < 5:
    # Setting FPS of a program to Max 1 per second.
    clock.tick(1)
    print(clock.get_time()) # Printing time used in the previous tick
    print(clock.get_fps()) # Printing compute the clock frame rate.
    i+=1