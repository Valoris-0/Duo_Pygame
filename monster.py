import pygame
import settings
import random

monster = pygame.image.load("assets/images/Monster.png")
monster_x = -500

jumpscare_images = []
for i in range(1,5):
    image = pygame.image.load(f"assets/images/jumpscares/jumpscare_monster_{i}.png")
    image = pygame.transform.scale(image, (settings.WIDTH, settings.HEIGHT))
    jumpscare_images.append(image)

monster_hitbox = pygame.Rect(0, 0, 0, 0)
monster_speed = settings.MONSTER_SPEED
scare = None

def moving_monster(screen, moved, player_x, dt):
    global total_x, monster_speed,monster_x, monster_hitbox
    monster_hitbox = monster.get_rect(topleft=(int(monster_x - 80), 40))
    monster_hitbox = monster_hitbox.inflate(-390, -200)

    monster_x += monster_speed * dt - moved
    screen.blit(monster, (int(monster_x), 0))

    total_x = player_x - settings.HALLWAY_X

    monster_speed = settings.MONSTER_SPEED + (total_x // 1000) * 0.1

    if settings.debugmode:
        pygame.draw.rect(screen, (255, 0, 0), monster_hitbox, 2)

def jumpscare(screen):
    global scare
    scare = random.choice(jumpscare_images)
    settings.scare = True