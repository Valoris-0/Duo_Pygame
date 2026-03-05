import pygame
import hallway
import settings

player_1 = pygame.image.load("assets/images/player_1.png")
player_2 = pygame.image.load("assets/images/player_2.png")
player_3 = pygame.image.load("assets/images/player_3.png")
player_4 = pygame.image.load("assets/images/player_4.png")
player_5 = pygame.image.load("assets/images/player_5.png")
player_6 = pygame.image.load("assets/images/player_6.png")

player_1 = pygame.transform.scale(player_1, (200, 150))
player_2 = pygame.transform.scale(player_2, (200, 150))
player_3 = pygame.transform.scale(player_3, (200, 150))
player_4 = pygame.transform.scale(player_4, (200, 150))
player_5 = pygame.transform.scale(player_5, (200, 150))
player_6 = pygame.transform.scale(player_6, (200, 150))

animation = 0


class Player:
    def __init__(self, x, width, height, color=(255, 0, 0), speed=settings.SPEED, y=140):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.player_hitbox = pygame.Rect(self.x, self.y, self.width, self.height)


    def handle_input(self, surface):
        # use the module-level animation counter so movement frames cycle
        global animation

        moved = 0
        keys = pygame.key.get_pressed()
        if keys[settings.LEFT_MOVEMENT]:
            if self.x < 200 and settings.HALLWAY_X < 0:
                moved -= self.speed
            else:
                self.x -= self.speed
            animation += 1
        if keys[settings.RIGHT_MOVEMENT]:
            if self.x > 500:
                moved += self.speed
            else:
                self.x += self.speed
            animation += 1
        if animation >= 60:
            animation = 0
        if self.x < 0: 
            self.x = 0
        if moved < 0 - self.x:
            moved = 0

        self.player_hitbox = pygame.Rect(self.x + 65, self.y + 50, self.width, self.height)
        self.player_hitbox = self.player_hitbox.inflate(40, 100)
        

        return moved

    def draw(self, screen):
        global animation

        # draw the current animation frame
        if animation >= 0 and animation < 10:
            screen.blit(player_1, (self.x, self.y))
        elif animation >= 10 and animation < 20:
            screen.blit(player_2, (self.x, self.y))
        elif animation >= 20 and animation < 30:
            screen.blit(player_3, (self.x, self.y))
        elif animation >= 30 and animation < 40:
            screen.blit(player_4, (self.x, self.y)) 
        elif animation >= 40 and animation < 50:
            screen.blit(player_5, (self.x, self.y))
        elif animation >= 50 and animation < 60:
            screen.blit(player_6, (self.x, self.y))

        if settings.debugmode:
            pygame.draw.rect(screen, (255, 0, 0), self.player_hitbox, 2)

    def update(self):
        pass
        





