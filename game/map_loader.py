import os
import json
import pygame

class TileMap:
    def __init__(self, world_path, base_dir):
        self.world_data = self.load_world(world_path)
        self.asset_packs = self.load_asset_packs(base_dir, self.world_data)
        self.textures = self.load_textures(base_dir)

    def load_world(self, world_path):
        with open(world_path, "r") as f:
            return json.load(f)

    def load_asset_packs(self, base_dir, world_data):
        asset_packs = {}
        for pack_id, pack_info in world_data["asset_packs"].items():
            tileset_path = os.path.join(base_dir, pack_info["path"], "tiles.json")
            with open(tileset_path, "r") as f:
                asset_packs[pack_id] = json.load(f)
        return asset_packs

    def load_textures(self, base_dir):
        textures = {}
        for pack_id, tiles in self.asset_packs.items():
            for tile_name, tile_info in tiles.items():
                texture_path = os.path.join(base_dir, self.world_data["asset_packs"][pack_id]["path"], tile_info["path"])
                textures[f"{pack_id}:{tile_name}"] = pygame.image.load(texture_path)
        return textures

    def draw_map(self, surface, scale_factor):
        tile_size = int(16 * scale_factor)  # Default TILE_SIZE = 16
        for row_index, row in enumerate(self.world_data["map"]):
            for col_index, tile_key in enumerate(row):
                if tile_key in self.textures:
                    scaled_texture = pygame.transform.scale(self.textures[tile_key], (tile_size, tile_size))
                    surface.blit(scaled_texture, (col_index * tile_size, row_index * tile_size))
