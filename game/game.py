import pygame
import os
from map_loader import TileMap

# Constants
TILE_SIZE = 16
VISIBLE_TILES_X = 16  # 16 tiles horizontally
VISIBLE_TILES_Y = 15  # 15 tiles vertically
BASE_WIDTH = VISIBLE_TILES_X * TILE_SIZE  # 256 pixels wide
BASE_HEIGHT = VISIBLE_TILES_Y * TILE_SIZE  # 240 pixels tall

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((BASE_WIDTH * 3, BASE_HEIGHT * 3), pygame.RESIZABLE)
pygame.display.set_caption("Legend of Zack")

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
WORLD_PATH = os.path.join(BASE_DIR, "worlds", "Sample", "world.json")

# Load map (no player for now)
tile_map = TileMap(WORLD_PATH, BASE_DIR)

# Game loop
running = True
while running:
    screen_width, screen_height = screen.get_size()

    # Create a surface to render the game at its base resolution (256x240)
    game_surface = pygame.Surface((BASE_WIDTH, BASE_HEIGHT))
    game_surface.fill((0, 0, 0))  # Clear screen

    # Draw the map at base resolution (only 15x16 tiles visible)
    tile_map.draw_map(game_surface, 1)  # No scaling for now

    # Scale the game surface to fit the window size while maintaining aspect ratio
    scaled_surface = pygame.transform.scale(game_surface, (screen_width, screen_height))

    # Center the scaled viewbox inside the window
    screen.fill((0, 0, 0))  # Black background for letterboxing effect
    screen.blit(scaled_surface, ((screen_width - BASE_WIDTH) // 2, (screen_height - BASE_HEIGHT) // 2))

    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
