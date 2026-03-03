import pygame
# Initialize Pygame
pygame.init()

# Initialize the mixer to play sound.
pygame.mixer.init()
pygame.mixer.music.load("PyGamesProjects/Project1/music/sacredmusic.mp3")
# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Image Display")
# Load images
smiley = pygame.image.load('PyGamesProjects/Project1/images/image.png')

# Main game loop
running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
   # Draw the background and character
   screen.blit(smiley, (300, 200)) # Draw character at (300, 200)
   
   # play the music
   pygame.time.delay(10000)
   pygame.mixer.music.play()
   
   # Update the display
   pygame.display.flip()
# Quit Pygame
pygame.quit()