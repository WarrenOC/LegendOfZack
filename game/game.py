import pygame
import os
import json

# Constants
BASE_WIDTH, BASE_HEIGHT = 256, 240  # NES resolution
TILE_SIZE = 16  # Default tile size
ASPECT_RATIO = BASE_WIDTH / BASE_HEIGHT

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((BASE_WIDTH * 3, BASE_HEIGHT * 3), pygame.RESIZABLE)
pygame.display.set_caption("Legend of Zack")

# Load world.json
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
WORLD_PATH = os.path.join(BASE_DIR, "worlds", "Sample", "world.json")

with open(WORLD_PATH, "r") as f:
    world_data = json.load(f)

# Load asset packs
asset_packs = {}
for pack_id, pack_info in world_data["asset_packs"].items():
    tileset_path = os.path.join(BASE_DIR, pack_info["path"], "tiles.json")
    with open(tileset_path, "r") as f:
        asset_packs[pack_id] = json.load(f)

# Load textures
textures = {}
for pack_id, tiles in asset_packs.items():
    for tile_name, tile_info in tiles.items():
        texture_path = os.path.join(BASE_DIR, world_data["asset_packs"][pack_id]["path"], tile_info["path"])
        textures[f"{pack_id}:{tile_name}"] = pygame.image.load(texture_path)

# Player class
class Player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 255, 0)  # Bright green
        self.speed = 1.5  # Adjusted speed

    def move(self, keys):
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.speed

    def draw(self, surface, scale_factor):
        scaled_x = int(self.x * scale_factor)
        scaled_y = int(self.y * scale_factor)
        scaled_size = int(self.size * scale_factor)
        pygame.draw.rect(surface, self.color, (scaled_x, scaled_y, scaled_size, scaled_size))

# Initialize player
player = Player(100, 100, TILE_SIZE)

# Function to draw map
def draw_map(surface, scale_factor):
    tile_size = int(TILE_SIZE * scale_factor)  # Adjust tile size
    for row_index, row in enumerate(world_data["map"]):
        for col_index, tile_key in enumerate(row):
            if tile_key in textures:
                scaled_texture = pygame.transform.scale(textures[tile_key], (tile_size, tile_size))
                surface.blit(scaled_texture, (col_index * tile_size, row_index * tile_size))

# Game loop
running = True
while running:
    screen_width, screen_height = screen.get_size()

    # Maintain aspect ratio
    if screen_width / screen_height > ASPECT_RATIO:
        new_height = screen_height
        new_width = int(new_height * ASPECT_RATIO)
    else:
        new_width = screen_width
        new_height = int(new_width / ASPECT_RATIO)

    scale_factor = new_width / BASE_WIDTH  # Scaling factor based on width
    game_surface = pygame.Surface((BASE_WIDTH, BASE_HEIGHT))

    game_surface.fill((0, 0, 0))  # Black background
    draw_map(game_surface, scale_factor)

    # Player input
    keys = pygame.key.get_pressed()
    player.move(keys)

    # Draw player
    player.draw(game_surface, scale_factor)

    # Scale game surface to window size
    scaled_surface = pygame.transform.scale(game_surface, (new_width, new_height))

    # Center the scaled surface with black bars
    screen.fill((0, 0, 0))
    screen.blit(scaled_surface, ((screen_width - new_width) // 2, (screen_height - new_height) // 2))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.w, event.h  # Update dimensions but DO NOT reset window

pygame.quit()
