import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Breakout')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Paddle settings
paddle_width, paddle_height = 100, 10
paddle_pos = [width // 2 - paddle_width // 2, height - 30]
paddle_speed = 6

# Ball settings
ball_size = 10
ball_pos = [width // 2, height // 2]
ball_speed = [3, -3]

# Brick settings
brick_rows = 5
brick_cols = 8
brick_width = (width - 60) // brick_cols
brick_height = 20
bricks = []
for i in range(brick_rows):
    for j in range(brick_cols):
        bricks.append(pygame.Rect(30 + j * brick_width, 30 + i * brick_height, brick_width - 2, brick_height - 2))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Move paddle
    if keys[pygame.K_LEFT] and paddle_pos[0] > 0:
        paddle_pos[0] -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_pos[0] < width - paddle_width:
        paddle_pos[0] += paddle_speed

    # Move ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Ball collision with walls
    if ball_pos[0] <= 0 or ball_pos[0] >= width - ball_size:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= 0:
        ball_speed[1] = -ball_speed[1]

    # Ball collision with paddle
    if paddle_pos[0] <= ball_pos[0] <= paddle_pos[0] + paddle_width and \
       paddle_pos[1] <= ball_pos[1] + ball_size <= paddle_pos[1] + paddle_height:
        ball_speed[1] = -ball_speed[1]

    # Ball collision with bricks
    for brick in bricks:
        if brick.colliderect(pygame.Rect(ball_pos[0], ball_pos[1], ball_size, ball_size)):
            ball_speed[1] = -ball_speed[1]
            bricks.remove(brick)
            break

    # Ball out of bounds
    if ball_pos[1] >= height:
        ball_pos = [width // 2, height // 2]
        ball_speed = [3, -3]

    # Clear screen
    screen.fill(BLACK)

    # Draw paddle
    pygame.draw.rect(screen, WHITE, (*paddle_pos, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.rect(screen, RED, (*ball_pos, ball_size, ball_size))

    # Draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, BLUE, brick)

    # Refresh display
    pygame.display.flip()

    # Control game speed
    pygame.time.Clock().tick(60)
