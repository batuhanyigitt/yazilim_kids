import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball settings
ball_size = 20
ball_pos = [width // 2, height // 2]
ball_speed = [3, 3]

# Paddle settings
paddle_width, paddle_height = 10, 100
left_paddle_pos = [50, height // 2 - paddle_height // 2]
right_paddle_pos = [width - 50 - paddle_width, height // 2 - paddle_height // 2]
paddle_speed = 5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Move left paddle
    if keys[pygame.K_w] and left_paddle_pos[1] > 0:
        left_paddle_pos[1] -= paddle_speed
    if keys[pygame.K_s] and left_paddle_pos[1] < height - paddle_height:
        left_paddle_pos[1] += paddle_speed

    # Move right paddle
    if keys[pygame.K_UP] and right_paddle_pos[1] > 0:
        right_paddle_pos[1] -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_pos[1] < height - paddle_height:
        right_paddle_pos[1] += paddle_speed

    # Move ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Ball collision with top or bottom
    if ball_pos[1] <= 0 or ball_pos[1] >= height - ball_size:
        ball_speed[1] = -ball_speed[1]

    # Ball collision with paddles
    if (ball_pos[0] <= left_paddle_pos[0] + paddle_width and left_paddle_pos[1] <= ball_pos[1] <= left_paddle_pos[1] + paddle_height) or \
       (ball_pos[0] >= right_paddle_pos[0] - ball_size and right_paddle_pos[1] <= ball_pos[1] <= right_paddle_pos[1] + paddle_height):
        ball_speed[0] = -ball_speed[0]

    # Ball out of bounds
    if ball_pos[0] <= 0 or ball_pos[0] >= width - ball_size:
        ball_pos = [width // 2, height // 2]

    # Clear screen
    screen.fill(BLACK)

    # Draw paddles
    pygame.draw.rect(screen, WHITE, (*left_paddle_pos, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (*right_paddle_pos, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.rect(screen, WHITE, (*ball_pos, ball_size, ball_size))

    # Refresh display
    pygame.display.flip()

    # Control game speed
    pygame.time.Clock().tick(60)
