import pygame
import hallway
import settings
import border_check

player_side_1 = pygame.image.load("assets/images/player/player_side_1.png")
player_side_2 = pygame.image.load("assets/images/player/player_side_2.png")
player_side_3 = pygame.image.load("assets/images/player/player_side_3.png")
player_side_4 = pygame.image.load("assets/images/player/player_side_4.png")
player_side_5 = pygame.image.load("assets/images/player/player_side_5.png")
player_side_6 = pygame.image.load("assets/images/player/player_side_6.png")

player_side_1 = pygame.transform.scale(player_side_1, (200, 150))
player_side_2 = pygame.transform.scale(player_side_2, (200, 150))
player_side_3 = pygame.transform.scale(player_side_3, (200, 150))
player_side_4 = pygame.transform.scale(player_side_4, (200, 150))
player_side_5 = pygame.transform.scale(player_side_5, (200, 150))
player_side_6 = pygame.transform.scale(player_side_6, (200, 150))

player_top_1 = pygame.image.load("assets/images/player/player_top_1.png")
player_top_2 = pygame.image.load("assets/images/player/player_top_2.png")
player_top_3 = pygame.image.load("assets/images/player/player_top_3.png")
player_top_4 = pygame.image.load("assets/images/player/player_top_4.png")

# scale the top‑down sprites to match the hitbox/player size (same as side for now)
player_top_1 = pygame.transform.scale(player_top_1, (200, 150))
player_top_2 = pygame.transform.scale(player_top_2, (200, 150))
player_top_3 = pygame.transform.scale(player_top_3, (200, 150))
player_top_4 = pygame.transform.scale(player_top_4, (200, 150))


animation_side = 0
animation_top = 0


class Player:
    def __init__(self, x, width, height, color=(255, 0, 0), speed=settings.SPEED, y=140):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.player_hitbox = pygame.Rect(self.x, self.y, self.width, self.height)


    def handle_input_side(self, surface):
        # use the module-level animation counter so movement frames cycle
        global animation_side

        if not settings.room_reset:
            settings.room_reset = True
        moved = 0
        keys = pygame.key.get_pressed()
        if keys[settings.LEFT_MOVEMENT]:
            if self.x < 200 and settings.HALLWAY_X < 0:
                moved -= self.speed
            else:
                self.x -= self.speed
            animation_side += 1
        if keys[settings.RIGHT_MOVEMENT]:
            if self.x > 500:
                moved += self.speed
            else:
                self.x += self.speed
            animation_side += 1
        if animation_side >= 60:
            animation_side = 0
        if self.x < 0: 
            self.x = 0
        if moved < 0 - self.x:
            moved = 0

        self.player_hitbox = pygame.Rect(self.x + 65, self.y + 50, self.width, self.height)
        self.player_hitbox = self.player_hitbox.inflate(40, 100)
        

        return moved

    def draw_side(self, screen):
        global animation_side

        # draw the current animation frame
        if animation_side >= 0 and animation_side < 10:
            screen.blit(player_side_1, (self.x, self.y))
        elif animation_side >= 10 and animation_side < 20:
            screen.blit(player_side_2, (self.x, self.y))
        elif animation_side >= 20 and animation_side < 30:
            screen.blit(player_side_3, (self.x, self.y))
        elif animation_side >= 30 and animation_side < 40:
            screen.blit(player_side_4, (self.x, self.y)) 
        elif animation_side >= 40 and animation_side < 50:
            screen.blit(player_side_5, (self.x, self.y))
        elif animation_side >= 50 and animation_side < 60:
            screen.blit(player_side_6, (self.x, self.y))

        if settings.debugmode:
            pygame.draw.rect(screen, (255, 0, 0), self.player_hitbox, 2)

    def update(self):
        pass

    def handle_input_top(self, surface):
        global animation_top

        keys = pygame.key.get_pressed()
        moved = 0

        # reset player position when entering a room
        if settings.room_reset:
            self.x = 200
            self.y = 340
            settings.room_reset = False

        # attempt movement in each direction but only apply if border_check allows it
        if keys[settings.UP_MOVEMENT]:
            new_y = self.y - self.speed
            if border_check.check(self.x, new_y, self.width, self.height):
                self.y = new_y
                settings.last_mover = "up"
                animation_top += 1
        if keys[settings.DOWN_MOVEMENT]:
            new_y = self.y + self.speed
            if border_check.check(self.x, new_y, self.width, self.height):
                self.y = new_y
                settings.last_mover = "down"
                animation_top += 1
        if keys[settings.LEFT_MOVEMENT]:
            new_x = self.x - self.speed
            if border_check.check(new_x, self.y, self.width, self.height):
                self.x = new_x
                settings.last_mover = "left"
                animation_top += 1
        if keys[settings.RIGHT_MOVEMENT]:
            new_x = self.x + self.speed
            if border_check.check(new_x, self.y, self.width, self.height):
                self.x = new_x
                settings.last_mover = "right"
                animation_top += 1

        if animation_top >= 60:
            animation_top = 0

        # keep the hitbox up to date for collisions, same as side view
        self.player_hitbox = pygame.Rect(self.x + 65, self.y + 50, self.width, self.height)
        self.player_hitbox = self.player_hitbox.inflate(40, 100)

        return moved
    

    def draw_top(self, screen):

        if settings.last_mover == "up":
            screen.blit(player_top_1, (self.x, self.y))
        elif settings.last_mover == "down":
            screen.blit(player_top_2, (self.x, self.y))
        elif settings.last_mover == "left":
            screen.blit(player_top_3, (self.x, self.y))
        elif settings.last_mover == "right":
            screen.blit(player_top_4, (self.x, self.y))


        

        




