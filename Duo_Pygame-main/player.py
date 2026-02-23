import pygame
import hallway
import settings
import main

#Moving animation
sprites_moving = []

for i in range(1, 7):
    image = pygame.image.load(f"assets/images/Player/player_{i}.png")
    image = pygame.transform.scale(image, (settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT))
    sprites_moving.append(image)

#Idle animation
sprites_idle = []

for i in range(1,5):
    image = pygame.image.load(f"assets/images/Player/idle_{i}.png")
    image = pygame.transform.scale(image, (settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT))
    sprites_idle.append(image)


animation = 0


class Player:
    def __init__(self, x, speed=settings.SPEED, y=140):
        self.x = x
        self.y = y
        self.speed = speed

    #Input
    def handle_input(self, surface):
        global animation

        moved = 0
        settings.IS_MOVING_NOW = False

        keys = pygame.key.get_pressed()
        if keys[settings.LEFT_MOVEMENT]:
            settings.LOOKING_RIGHT = False
            if self.x < 100 and settings.HALLWAY_X < 0:
                moved -= self.speed
            else:
                self.x -= self.speed
            settings.IS_MOVING_NOW = True
        
        if keys[settings.RIGHT_MOVEMENT]:
            settings.LOOKING_RIGHT = True
            if self.x > 500:
                moved += self.speed
            else:
                self.x += self.speed
            settings.IS_MOVING_NOW = True

        if settings.IS_MOVING_NOW != settings.MOVING:
            animation = 0


        settings.MOVING = settings.IS_MOVING_NOW

        animation += 1

        if animation >= 600:
            animation = 0

        if self.x < 0: 
            self.x = 0
        if moved < 0 - self.x:
            moved = 0

        return moved

    #Animations using sprites
    def draw(self, screen):
        global animation

        if settings.MOVING:
            current_list = sprites_moving
            anim_speed = 10
        elif not settings.MOVING:
            current_list = sprites_idle
            anim_speed = 25
        
        frame_index = (animation // anim_speed) % len(current_list)
        current_sprite = current_list[frame_index]

        if settings.LOOKING_RIGHT:
            screen.blit(current_sprite, (self.x, self.y))
        else:
            flipped_sprite = pygame.transform.flip(current_sprite, True, False)
            screen.blit(flipped_sprite, (self.x, self.y))

    def update(self):
        pass
