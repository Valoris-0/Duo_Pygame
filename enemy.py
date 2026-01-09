import pygame

class Enemy:
    def __init__(self, x, y, image_path, speed=2):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 1  # 1 = moving right, -1 = moving left

        # Load the enemy image
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self):
        # Move left and right
        self.x += self.speed * self.direction
        
        # Bounce back if hitting screen edges
        if self.x < 0:
            self.x = 0
            self.direction = 1
        if self.x + self.rect.width > 800:
            self.x = 800 - self.rect.width
            self.direction = -1

        self.rect.x = self.x

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
