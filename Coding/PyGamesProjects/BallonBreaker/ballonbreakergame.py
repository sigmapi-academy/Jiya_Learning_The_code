import pygame
import random
import sys

# Initialize pygame.
pygame.init()

# Screen dimensions.
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ballon Breaker")

#Colors
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)

#Clock
clock = pygame.time.Clock()

#fonts
font = pygame.font.SysFont('Arial', 30)
big_font = pygame.font.SysFont("Arial", 60)

# Sounds
try:
    pop_sound = pygame.mixer.Sound("ballon_pop.wav")
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.play(-1) # loop background music
except:
    pop_sound = None

# Ballon Class
class Balloon:
    def __init__(self):
        self.x = random.randint(50, WIDTH-50)
        self.y = HEIGHT
        self.radius = random.randint(20, 40)
        self.speed = random.randint(2, 5)
        self.color = random.choice([
            (255,0,0), #red
            (0,255,0), #Green
            (0,0,255), #Blue
            (255,255,0) #Yellow
        ])
        
    def move(self):
        self.y -= self.speed
        
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        
#Power-up balloon class
class PowerUp(Balloon):
    def __init__(self):
        super().__init__()
        self.color = (255,0,255) #purple
        
    def activate(self, game):
        # Example: grant extra life
        game.lives += 1
        
# Game class
class Game:
    def __init__(self):
        self.balloons = []
        self.score = 0
        self.lives = 50
        self.game_time = 60 #seconds
        self.start_ticks = pygame.time.get_ticks()
        self.running = True
    
    def spwan_balloon(self):
        if random.randint(1, 30) == 1:
            self.balloons.append(Balloon())
        
        if random.randint(1,100) == 1: #Rare power-up
            self.balloons.append(PowerUp())
            
    def update_ballons(self):
        for balloon in self.balloons[:]:
            balloon.move()
            balloon.draw()
            if balloon.y + balloon.radius < 0: #Escaped
                self.balloons.remove(balloon)
                self.lives -= 1
                if self.lives <= 0:
                    self.running = False
                    
    def check_click(self, pos):
        for balloon in self.balloons[:]:
            dist = ((balloon.x -pos[0])**2 + (balloon.y - pos[1])**2) ** 0.5
            if dist < balloon.radius:
                if isinstance(balloon, PowerUp):
                    balloon.activate(self)
                else:
                    self.score += 1
                if pop_sound:
                    pop_sound.play()
                self.balloons.remove(balloon)
                
    def check_timer(self):
        seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000
        if seconds >= self.game_time:
            self.running = False
            
    def draw_ui(self):
        score_text = font.render(f"Score: {self.score}", True, BLACK)
        lives_text = font.render(f"Lives: {self.lives}", True, BLACK)
        screen.blit(score_text, (10,10))
        screen.blit(lives_text, (10, 50))
        
    def game_over(self):
        screen.fill(WHITE)
        over_text = big_font.render("GAME OVER", True, BLACK)
        score_text = font.render(f"Final score: {self.score}", True, BLACK)
        screen.blit(over_text, (WIDTH//2 - 150, HEIGHT//2 -50))
        screen.blit(score_text, (WIDTH//2 - 100, HEIGHT//2 + 20))
        pygame.display.flip()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False


# Main loop
game = Game()

while game.running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.check_click(pygame.mouse.get_pos())
    
    game.spwan_balloon()
    game.update_ballons()
    game.check_timer()
    game.draw_ui()
    
    pygame.display.flip()
    clock.tick(60)
    
game.game_over()
pygame.quit()
sys.exit()