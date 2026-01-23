import pygame
import hallway

player = pygame.image.load("assets/images/image-removebg-preview (1).png").convert_alpha()

class Player:
    def __init__(self, x, width, height, color=(255, 0, 0), speed=3, y=225):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def handle_input(self, screen):
        moved = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.x < 150:
                moved -= self.speed
            else:
                self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            if self.x > 450:
                moved += self.speed
            else:
                self.x += self.speed
        
        
        

        return moved

    def draw(self, screen):
        screen.blit(player, (self.x, self.y))

    def update(self):
        pass
