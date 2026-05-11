import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

font = pygame.font.Font(None, 25)

# ======================
# GAME VARIABLES
# ======================

CELL_SIZE: int = 100
OFFSET: int = 0 # NOTE For later
moveX: int = 0 # NOTE This will be used to keep track of where the line is going
moveY: int = 0
score: int = 0
highscore: int = 0

# ======================
# STARTUP FUNCTIONS
# ======================

# GRID SETUP
# NOTE Maybe add a boarder later
for x in range(1, 7):
    pygame.draw.line(screen, 'white', (x*CELL_SIZE,0), (x*CELL_SIZE,600), width=2)
for y in range(1, 7):
    pygame.draw.line(screen, 'white', (0,y*CELL_SIZE), (600,y*CELL_SIZE), width=2)
        
# DEBUG: Grid Points
for x in range(6):
    for y in range(6):
        pygame.draw.circle(screen, 'white', (50+x*CELL_SIZE,50+y*CELL_SIZE), radius=40)
        text = font.render(f"{random.randint(1, 101)}", True, 'black')
        text_rect = text.get_rect(center=(50+x*CELL_SIZE,50+y*CELL_SIZE))
        screen.blit(text, text_rect)

# ======================
# GAME FUNCTIONS
# ======================



# ======================
# STARTUP GAME
# ======================



# ======================
# MAIN GAMEPLAY LOOP
# ======================

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(60)

pygame.quit()