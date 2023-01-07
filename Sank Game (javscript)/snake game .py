import pygame
import random

# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Snake properties
SNAKE_SIZE = 20
SNAKE_SPEED = 15

# Snake colors
SNAKE_GREEN = (0, 255, 0)

# Apple properties
APPLE_SIZE = 20
APPLE_SPAWN_BUFFER = 50

# Apple colors
APPLE_RED = (255, 0, 0)

class Snake:
    def __init__(self):
        self.size = SNAKE_SIZE
        self.speed = SNAKE_SPEED
        self.color = SNAKE_GREEN
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.body = []
        self.turns = {}

    def update_position(self):
        # Add the new position to the front of the snake
        self.body.insert(0, (self.x, self.y))

        # Remove the last element of the snake if the snake has not eaten an apple
        if (self.x, self.y) != self.turns.get(self.x, self.y):
            self.body.pop()
        else:
            self.turns.pop((self.x, self.y))

        # Update the position based on the current direction
        if self.direction == "North":
            self.y -= self.speed
        elif self.direction == "South":
            self.y += self.speed
        elif self.direction == "East":
            self.x += self.speed
        elif self.direction == "West":
            self.x -= self.speed

    def draw(self, window):
        for x, y in self.body:
            pygame.draw.rect(window, self.color, (x, y, self.size, self.size))

    def change_direction(self, direction):
        self.direction = direction

        # Save the current position of the snake in the turns dictionary
        self.turns[self.x] = self.y

    def check_collision(self):
        # Check collision with walls
        if self.x > WINDOW_WIDTH or self.x < 0 or self.y > WINDOW_HEIGHT or self.y < 0:
            return True

        # Check collision with itself
        for block in self.body[1:]:
            if (self.x, self.y) == block:
                return True

        return False

class Apple:
    def __init__(self):
        self.size = APPLE_SIZE
        self.color = APPLE_RED
        self.spawn()

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))

    def spawn(self):
        self.x = random.randint(APPLE_SPAWN_BUFFER, WINDOW_WIDTH - APPLE_SPAWN_BUFFER)
        self.y = random.randint(APPLE_SP
