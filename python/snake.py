import pygame
import sys
import random

pygame.init()

cell_size = 20
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption('Snake Game')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

colors = {
    'GREEN': GREEN,
    'RED': RED,
    'BLUE': BLUE,
    'YELLOW': YELLOW
}

snake_color = GREEN  

def choose_character():
    global snake_color
    while True:
        screen.fill(BLACK)
        font = pygame.font.Font(None, 36)
        text = font.render('Choose your snake color:', True, WHITE)
        screen.blit(text, (10, 10))
        
        y_pos = 60
        for color_name, color in colors.items():
            pygame.draw.rect(screen, color, pygame.Rect(10, y_pos, 100, 50))
            text = font.render(color_name, True, WHITE)
            screen.blit(text, (120, y_pos + 10))
            y_pos += 60

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                y_pos = 60
                for color_name, color in colors.items():
                    if 10 <= mouse_pos[0] <= 110 and y_pos <= mouse_pos[1] <= y_pos + 50:
                        snake_color = color
                        return
                    y_pos += 60

def move_food():
    return [random.randint(0, cell_number - 1) * cell_size, random.randint(0, cell_number - 1) * cell_size]

def check_collision(position, body):
    return position in body

choose_character()

snake_position = [cell_number // 2 * cell_size, cell_number // 2 * cell_size]
snake_body = [list(snake_position)]
snake_speed = [0, 0]
snake_direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])

food_position = [random.randint(0, cell_number - 1) * cell_size, random.randint(0, cell_number - 1) * cell_size]

score = 0
speed = 5  

obstacles = []
for _ in range(5):
    obstacle_position = [random.randint(0, cell_number - 1) * cell_size, random.randint(0, cell_number - 1) * cell_size]
    while obstacle_position in snake_body or obstacle_position == food_position:
        obstacle_position = [random.randint(0, cell_number - 1) * cell_size, random.randint(0, cell_number - 1) * cell_size]
    obstacles.append(obstacle_position)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_speed = [0, -cell_size]
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_speed = [0, cell_size]
                snake_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_speed = [-cell_size, 0]
                snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_speed = [cell_size, 0]
                snake_direction = 'RIGHT'

    snake_position[0] += snake_speed[0]
    snake_position[1] += snake_speed[1]


    if snake_position[0] < 0:
        snake_position[0] = (cell_number - 1) * cell_size
    elif snake_position[0] >= cell_number * cell_size:
        snake_position[0] = 0
    if snake_position[1] < 0:
        snake_position[1] = (cell_number - 1) * cell_size
    elif snake_position[1] >= cell_number * cell_size:
        snake_position[1] = 0

    if snake_position == food_position:
        score += 1
        snake_body.append(list(snake_position))  
        food_position = move_food()
        while check_collision(food_position, snake_body) or food_position in obstacles:
            food_position = move_food()
        speed += 1  


    snake_body.insert(0, list(snake_position))
    if snake_position != food_position:
        snake_body.pop()

    if snake_position in obstacles:
        pygame.quit()
        sys.exit()

    screen.fill(BLACK)

    for pos in snake_body:
        pygame.draw.rect(screen, snake_color, pygame.Rect(pos[0], pos[1], cell_size, cell_size))

    pygame.draw.rect(screen, RED, pygame.Rect(food_position[0], food_position[1], cell_size, cell_size))

    for pos in obstacles:
        pygame.draw.rect(screen, BLUE, pygame.Rect(pos[0], pos[1], cell_size, cell_size))

    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()

    pygame.time.Clock().tick(speed) 






import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('02102.jpg')

if image is None:
    print("Error: Could not load image.")
    exit()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

edges = cv2.Canny(blurred_image, 100, 200)

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Grayscale Image')
plt.imshow(gray_image, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Blurred Image')
plt.imshow(blurred_image, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Edge Detection')
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
