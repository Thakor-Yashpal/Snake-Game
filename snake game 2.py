import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set the dimensions of the screen (width, height).
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Define snake block size
block_size = 10

# Set initial position and movement speed of snake
x_pos = 300
y_pos = 300
x_speed = 0
y_speed = 0

# Create a list to store the snake's blocks
snake_list = [(x_pos, y_pos)]

# Generate initial position for food
foodx = round(random.randrange(0, size[0] - block_size) / 10.0) * 10.0
foody = round(random.randrange(0, size[1] - block_size) / 10.0) * 10.0

# Set initial score
score = 0

# Initialize font for displaying score
font_style = pygame.font.SysFont(None, 50)

# Function to display score
def display_score(score):
    score_text = font_style.render("Score: " + str(score), True, white)
    screen.blit(score_text, [0,0])

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Main game loop
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_speed != 10:
                x_speed = -10
                y_speed = 0
            elif event.key == pygame.K_RIGHT and x_speed != -10:
                x_speed = 10
                y_speed = 0
            elif event.key == pygame.K_UP and y_speed != 10:
                y_speed = -10
                x_speed = 0
            elif event.key == pygame.K_DOWN and y_speed != -10:
                y_speed = 10
                x_speed = 0
                
    # --- Game logic
    # Update snake's position
    x_pos += x_speed
    y_pos += y_speed
    
    # Check for collision with food
    if x_pos == foodx and y_pos == foody:
        # Generate new food position
        foodx = round(random.randrange(0, size[0] - block_size) / 10.0) * 10.0
        foody = round(random.randrange(0, size[1] - block_size) / 10.0) * 10.0
        score += 1
    else:
        # Remove the last block of the snake
