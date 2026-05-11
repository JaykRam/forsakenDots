import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

CELL_SIZE: int = 50
moveX: int = 0 # NOTE This will be used to keep track of where the line is going
moveY: int = 0
score: int = 0
highscore: int = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(60)

pygame.quit()