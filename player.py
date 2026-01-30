import pygame
import hallway
import settings

class Player:
    def __init__(self, x, width, height, color=(255, 0, 0), speed=settings.SPEED, y=225):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def handle_input(self, surface):
        
        moved = 0
        keys = pygame.key.get_pressed()
        if keys[settings.LEFT_MOVEMENT]:
            if self.x < 200 and settings.HALLWAY_X < 0:
                moved -= self.speed
            else:
                self.x -= self.speed
        if keys[settings.RIGHT_MOVEMENT]:
            if self.x > 500:
                moved += self.speed
            else:
                self.x += self.speed
        if self.x < 0: 
            self.x = 0
        if moved < 0 - self.x:
            moved = 0
        
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

        return moved
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        
    def update(self):
        pass
