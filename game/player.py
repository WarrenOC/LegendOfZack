import pygame

class Player:
    def __init__(self, x, y):
        # Create a 16x16 green square as a placeholder
        self.image = pygame.Surface((16, 16))
        self.image.fill((0, 255, 0))  # Green color
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2  # Keep movement smooth

    def move(self, keys):
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
