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


start_tile = None
current_tile = (0,0)
previous_tile = (0,0)

tile_pos = []
circle_pos = []
circle_color = [] # My work around to save color, Lol
circle_number = []
grid_movement = []

on_circle = False
is_dragging = False

# ======================
# STARTUP FUNCTIONS
# ======================

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)



# GRID SETUP # NOTE Maybe add a border later
def grid():
    screen.fill("black")
    for x in range(1, 7):
        pygame.draw.line(screen, 'white', (x * CELL_SIZE,0), (x * CELL_SIZE,600), width=2)
    for y in range(1, 7):
        pygame.draw.line(screen, 'white', (0, y * CELL_SIZE), (600, y * CELL_SIZE), width=2)
        


def draw_circle():

    total_circles = len(circle_pos)

    for i in range(total_circles):
        circle = circle_pos[i]
        color = circle_color[i]
        number = circle_number[i]

        pygame.draw.circle(screen, color, (circle.x + 35, circle.y + 35), radius=35)

        text = font.render(f"{number}", True, 'black')
        text_rect = text.get_rect(center=(circle.x + 35, circle.y + 35))
        screen.blit(text, text_rect)
        
        

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
        circle_color.append(color)
        circle_number.append(number)

        text = font.render(f"{number}", True, 'black')
        text_rect = text.get_rect(center=(50 + x * CELL_SIZE, 50 + y * CELL_SIZE))
        screen.blit(text, text_rect)



number_of_circle_pairs: int = 5
for circle in range(1, number_of_circle_pairs + 1):
    circleColor = random_color()

    place_circle(circleColor, circle)



# NOTE: grid movement
for x in range(6):
    for y in range(6):
        tile_pos.append(pygame.Rect(15 + x * CELL_SIZE, 15 + y * CELL_SIZE, 70, 70))



# ======================
# MAIN GAMEPLAY LOOP
# ======================

while running:
    
    grid()
    draw_circle()

    mouse_pos = pygame.mouse.get_pos()

    for circle in circle_pos:

        if circle.collidepoint(mouse_pos) and is_dragging == True:
            start_tile = None
            start_tile = (circle.x, circle.y)

  

    if start_tile != None:
        for tile in tile_pos:
            if tile.collidepoint(mouse_pos):
                pygame.draw.line(screen, 'white', (start_tile[0] + 35, start_tile[1] + 35), (tile.x + 35, tile.y + 35), width=35)


    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        # DRAGGING
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_dragging = True

            print("click")
        
        if event.type == pygame.MOUSEBUTTONUP:
            is_dragging = False
            start_tile = None

            print("let_go")
      
    pygame.display.flip()

    clock.tick(60)

pygame.quit()