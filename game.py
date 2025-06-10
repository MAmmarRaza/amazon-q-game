
# Simple Snake Game using Pygame
import pygame
import random
import time

# Initialize pygame
pygame.init()

# Set up display
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake and food
snake_block = 20
snake_speed = 15

# Initialize snake
x1 = width / 2
y1 = height / 2
x1_change = 0
y1_change = 0
snake_list = []
snake_length = 1

# Initialize food
foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

# Game clock
clock = pygame.time.Clock()

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], snake_block, snake_block])

# Main game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    # Check boundaries
    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    window.fill(BLACK)
    
    pygame.draw.rect(window, RED, [foodx, foody, snake_block, snake_block])
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check if snake hits itself
    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True

    draw_snake(snake_block, snake_list)

    # Check if food eaten
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
        foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
        snake_length += 1

    pygame.display.update()
    clock.tick(snake_speed)

pygame.quit()