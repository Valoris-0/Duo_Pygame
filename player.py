import pygame
import hallway

class Player:
    def __init__(self, x, y, width, height, color=(255, 0, 0), speed=5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def handle_input(self, surface):
        moved = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.x > 200:
                self.x -= self.speed
            else:
                moved = -self.speed
        if keys[pygame.K_RIGHT]:
            if self.x < 500:
                self.x += self.speed
            else:
                moved = self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        return moved
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        
    def update(self):
        pass
