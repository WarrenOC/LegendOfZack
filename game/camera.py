import pygame

class Camera:
    def __init__(self, width, height, world_width, world_height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.world_width = world_width
        self.world_height = world_height
        self.viewport = pygame.Rect(0, 0, width, height)

    def apply(self, entity):
        """Moves the entity according to the camera's position."""
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        """Centers the camera around the target (player)."""
        x = -target.rect.centerx + int(self.viewport.width / 2)
        y = -target.rect.centery + int(self.viewport.height / 2)

        # Constrain camera to map boundaries
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.world_width - self.viewport.width), x)
        y = max(-(self.world_height - self.viewport.height), y)

        self.camera = pygame.Rect(x, y, self.world_width, self.world_height)
