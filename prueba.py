import pygame
import sys

pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dynamic Camera Example")

# Set the dimensions of your game world
WORLD_WIDTH = 1600
WORLD_HEIGHT = 1200

# Set up a clock to control the frame rate
clock = pygame.time.Clock()

# Create a camera class
class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(WINDOW_WIDTH / 2)
        y = -target.rect.centery + int(WINDOW_HEIGHT / 2)

        # Limit scrolling to the bounds of the world
        x = min(0, x)  # Prevent scrolling left
        y = min(0, y)  # Prevent scrolling up
        x = max(-(self.width - WINDOW_WIDTH), x)  # Prevent scrolling right
        y = max(-(self.height - WINDOW_HEIGHT), y)  # Prevent scrolling down

        self.camera = pygame.Rect(x, y, self.width, self.height)

# Define a simple entity class
class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Create some entities
player = Entity(100, 100, 50, 50, pygame.Color("blue"))
entities = pygame.sprite.Group()
entities.add(player)

# Create a camera object
camera = Camera(WORLD_WIDTH, WORLD_HEIGHT)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the camera's position based on the player's position
    camera.update(player)

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw entities relative to the camera's position
    for entity in entities:
        window.blit(entity.image, camera.apply(entity))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
