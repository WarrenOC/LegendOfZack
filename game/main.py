import pygame
from map_loader import TileMap

# Load the map
map_data = TileMap("world.json")

# Define placeholder tile colors
TILE_COLORS = {
    "pack1:grass": (34, 139, 34),
    "pack1:water": (0, 0, 255),
    "pack1:bridge": (139, 69, 19),
}

TILE_SIZE = 32  # Tile size

# Initialize Pygame
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

def draw_map(surface, map_data):
    """Draws the map based on the loaded tile data."""
    for y in range(map_data.height):
        for x in range(map_data.width):
            tile_name = map_data.get_tile(x, y)
            color = TILE_COLORS.get(tile_name, (255, 0, 255))  # Default to magenta
            pygame.draw.rect(surface, color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen
    draw_map(screen, map_data)  # Draw the map

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
