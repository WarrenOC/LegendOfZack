class Player:
    def __init__(self, x, y, tile_size):
        self.x = x
        self.y = y
        self.size = tile_size  # Match tile size
        self.color = (0, 255, 0)  # Bright green
        self.speed = 0.5  # Slower movement for better control

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
