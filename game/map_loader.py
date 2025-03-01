import json


class TileMap:
    def __init__(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)

        self.asset_packs = data["asset_packs"]
        self.width = data["width"]
        self.height = data["height"]
        self.tiles = data["tiles"]

    def get_tile(self, x, y):
        """Returns the tile identifier at a given coordinate."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]  # Row-major order
        return None
