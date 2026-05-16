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

start_tile = (0,0)
current_tile = (0,0)
previous_tile = (0,0)

tile_pos = []
circle_pos = []
grid_movement = []

is_dragging = False

# ======================
# STARTUP FUNCTIONS
# ======================

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# GRID SETUP
# NOTE Maybe add a boarder later
for x in range(1, 7):
    pygame.draw.line(screen, 'white', (x * CELL_SIZE,0), (x * CELL_SIZE,600), width=2)
for y in range(1, 7):
    pygame.draw.line(screen, 'white', (0, y * CELL_SIZE), (600, y * CELL_SIZE), width=2)
        

# DEBUG: Grid Points
# for x in range(6):
#     for y in range(6):
#         circleColor = random_color()
#         circle_pos.append(pygame.draw.circle(screen, circleColor, (50 + x * CELL_SIZE, 50 + y * CELL_SIZE), radius=35))
#         text = font.render(f"{random.randint(1, 101)}", True, 'black')
#         text_rect = text.get_rect(center=(50 + x * CELL_SIZE, 50 + y * CELL_SIZE))
#         screen.blit(text, text_rect)

taken = []
def place_circle(color, number):

    for i in range(2):
        
        while True:
            x = random.randint(0,5)
            y = random.randint(0,5)

            if (x, y) not in taken:
                taken.append((x, y))
                break

        circle = pygame.draw.circle(screen, color, (50 + x * CELL_SIZE, 50 + y * CELL_SIZE), radius=35)
        circle_pos.append(circle)

        text = font.render(f"{number}", True, 'black')
        text_rect = text.get_rect(center=(50 + x * CELL_SIZE, 50 + y * CELL_SIZE))
        screen.blit(text, text_rect)

        # print(circle)

number_of_circle_pairs: int = 2
for circle in range(1, number_of_circle_pairs + 1):
    circleColor = random_color()

    place_circle(circleColor, circle)


# print(circle_pos[0])



# DEBUG: Single Point
# x = 0
# y = 0

# circleColor = random_color()

# cic = pygame.draw.circle(screen, circleColor, (50 + x * CELL_SIZE, 50 + y * CELL_SIZE), radius=35)

# text = font.render(f"{random.randint(1, 101)}", True, 'black')
# text_rect = text.get_rect(center=(50 + x * CELL_SIZE, 50 + y * CELL_SIZE))
# screen.blit(text, text_rect)

# NOTE: grid movement
for x in range(6):
    for y in range(6):
        tile_pos.append(pygame.Rect(15 + x * CELL_SIZE, 15 + y * CELL_SIZE, 70, 70))

# print(tile_pos[0])

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

    mouse_pos = pygame.mouse.get_pos()

    # if cic.collidepoint(mouse_pos):
    #     print("Omori")
    #     print("Urotsuki")
    for circle in circle_pos:
        if circle.collidepoint(mouse_pos):
            print("BAZINGA")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(60)

pygame.quit()