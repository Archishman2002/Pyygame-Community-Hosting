import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
DOT_RADIUS = 5
LINE_HEIGHT = 100
NUM_DOTS = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Dots Video")

# Create a list of dots with random positions and velocities
dots = [{'x': random.randint(0, WIDTH), 'y': random.randint(0, HEIGHT), 'vx': random.uniform(1, 3), 'vy': 0} for _ in range(NUM_DOTS)]

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update dot positions
    for dot in dots:
        dot['x'] += dot['vx']
        dot['y'] += dot['vy']

        # Check if the dot is outside the screen
        if dot['x'] < 0 or dot['x'] > WIDTH:
            dot['vx'] *= -1

    # Draw background
    screen.fill(BLACK)

    # Draw lines
    pygame.draw.line(screen, WHITE, (0, HEIGHT // 2 - LINE_HEIGHT // 2), (WIDTH, HEIGHT // 2 - LINE_HEIGHT // 2), 2)
    pygame.draw.line(screen, WHITE, (0, HEIGHT // 2 + LINE_HEIGHT // 2), (WIDTH, HEIGHT // 2 + LINE_HEIGHT // 2), 2)

    # Draw dots
    for dot in dots:
        pygame.draw.circle(screen, WHITE, (int(dot['x']), int(dot['y'])), DOT_RADIUS)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
