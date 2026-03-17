import pygame
import hallway
import settings
import Border

sprites_moving_left = []

for i in range(1, 7):
    image = pygame.image.load(f"assets/images/player/player_side_{i}.png").convert_alpha()
    image = pygame.transform.scale(image, (settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT))
    image = pygame.transform.flip(image, True, False)
    sprites_moving_left.append(image)

sprites_moving_right = []

for i in range(1, 7):
    image = pygame.image.load(f"assets/images/player/player_side_{i}.png").convert_alpha()
    image = pygame.transform.scale(image, (settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT))
    sprites_moving_right.append(image)

sprites_top = []

for i in range(1, 5):
    image = pygame.image.load(f"assets/images/player/player_top_{i}.png").convert_alpha()
    image = pygame.transform.scale(image, (settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT))
    sprites_top.append(image)

sprites_idle_right = []

for i in range(1, 5):
    image = pygame.image.load(f"assets/images/player/idle_{i}.png").convert_alpha()
    image = pygame.transform.scale(image, (settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT))
    image = pygame.transform.flip(image, True, False)
    sprites_idle_right.append(image)

sprites_idle_left = []

for i in range(1, 5):
    image = pygame.image.load(f"assets/images/player/idle_{i}.png").convert_alpha()
    image = pygame.transform.scale(image, (settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT))
    sprites_idle_left.append(image)

animation = 0.0
animation_top = 0


def reset_player_state(player):
    global animation, animation_top

    animation = 0.0
    animation_top = 0
    player.x = 0.0
    player.y = 155.0
    player.player_hitbox = pygame.Rect(int(player.x), int(player.y), player.width, player.height)


class Player:
    def __init__(self, x, width, height, speed=settings.SPEED, y=155):
        self.x = float(x)
        self.y = float(y)
        self.width = width
        self.height = height
        self.speed = speed
        self.player_hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def handle_input_side(self, surface, dt):
        if settings.solving:
            return 0

        global animation

        if not settings.room_reset:
            settings.room_reset = True

        moved = 0
        settings.IS_MOVING_NOW = False
        step = self.speed * dt

        keys = pygame.key.get_pressed()
        if keys[settings.LEFT_MOVEMENT]:
            settings.LOOKING_RIGHT = False
            if self.x < 200 and settings.HALLWAY_X < 0:
                moved -= step
            else:
                self.x -= step
            settings.IS_MOVING_NOW = True

        if keys[settings.RIGHT_MOVEMENT]:
            settings.LOOKING_RIGHT = True
            if self.x > 500:
                moved += step
            else:
                self.x += step
            settings.IS_MOVING_NOW = True

        if settings.IS_MOVING_NOW != settings.MOVING:
            animation = 0

        settings.MOVING = settings.IS_MOVING_NOW

        animation += dt
        if animation >= 60.0:
            animation = 0.0

        if self.x < 0:
            self.x = 0
        if moved < 0 - self.x:
            moved = 0

        self.player_hitbox = pygame.Rect(int(self.x + 15), int(self.y + 50), self.width, self.height)
        self.player_hitbox = self.player_hitbox.inflate(40, 100)

        return moved

    def draw_side(self, screen):
        if settings.MOVING:
            current_list = sprites_moving_right if settings.LOOKING_RIGHT else sprites_moving_left
            animation_fps = 6.0
        else:
            current_list = sprites_idle_left if settings.LOOKING_RIGHT else sprites_idle_right
            animation_fps = 2.4

        frame_index = int(animation * animation_fps) % len(current_list)
        current_sprite = current_list[frame_index]

        screen.blit(current_sprite, (int(self.x), int(self.y)))

        if settings.debugmode:
            pygame.draw.rect(screen, (255, 0, 0), self.player_hitbox, 2)

    def update(self):
        pass

    def handle_input_top(self, surface, dt):
        # block movement while solving an interaction
        if settings.solving:
            return 0

        global animation_top

        keys = pygame.key.get_pressed()
        moved = 0
        step = self.speed * dt

        if settings.room_reset:
            self.x = 240
            self.y = 290
            settings.room_reset = False

        if keys[settings.UP_MOVEMENT]:
            new_y = self.y - step
            if Border.check(self.x, new_y, self.width, self.height, surface):
                self.y = new_y
                settings.last_mover = "up"
                animation_top += 1
        if keys[settings.DOWN_MOVEMENT]:
            new_y = self.y + step
            if Border.check(self.x, new_y, self.width, self.height, surface):
                self.y = new_y
                settings.last_mover = "down"
                animation_top += 1
        if keys[settings.RIGHT_MOVEMENT]:
            new_x = self.x + step
            if Border.check(new_x, self.y, self.width, self.height, surface):
                self.x = new_x
                settings.last_mover = "right"
                animation_top += 1
        if keys[settings.LEFT_MOVEMENT]:
            new_x = self.x - step
            if Border.check(new_x, self.y, self.width, self.height, surface):
                self.x = new_x
                settings.last_mover = "left"
                animation_top += 1

        Border.update_interaction_prompt(self.x, self.y)
        self.player_hitbox = pygame.Rect(int(self.x + 15), int(self.y + 15), self.width, self.height + 40)

        return moved

    def draw_top(self, screen):
        direction_map = {
            "up":    sprites_top[0],
            "down":  sprites_top[1],
            "left":  sprites_top[2],
            "right": sprites_top[3],
        }
        current_sprite = direction_map.get(settings.last_mover, sprites_top[1])
        screen.blit(current_sprite, (int(self.x), int(self.y)))

        if settings.debugmode:
            pygame.draw.rect(screen, (255, 0, 0), self.player_hitbox, 2)
    
