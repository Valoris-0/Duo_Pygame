import pygame
import settings
import random

monster = pygame.image.load("assets/images/Monster.png")
monster_x = -500

jumpscare_1 = pygame.image.load("assets/images/jumpscares/jumpscare_monster_1.png")
jumpscare_2 = pygame.image.load("assets/images/jumpscares/jumpscare_monster_2.png")
jumpscare_3 = pygame.image.load("assets/images/jumpscares/jumpscare_monster_3.png")
jumpscare_4 = pygame.image.load("assets/images/jumpscares/jumpscare_monster_4.png")

jumpscare_1 = pygame.transform.scale(jumpscare_1, (settings.WIDTH, settings.HEIGHT))
jumpscare_2 = pygame.transform.scale(jumpscare_2, (settings.WIDTH, settings.HEIGHT))
jumpscare_3 = pygame.transform.scale(jumpscare_3, (settings.WIDTH, settings.HEIGHT))
jumpscare_4 = pygame.transform.scale(jumpscare_4, (settings.WIDTH, settings.HEIGHT))

jumpscare_images = [
    jumpscare_1,
    jumpscare_2,
    jumpscare_3,
    jumpscare_4
    ]

scare = random.choice(jumpscare_images)

monster_hitbox = pygame.Rect(0, 0, 0, 0)
monster_speed = settings.MONSTER_SPEED

def moving_monster(screen, moved, player_x):
    global total_x, monster_speed,monster_x, monster_hitbox
    monster_hitbox = monster.get_rect(topleft=(monster_x - 80, 40))
    monster_hitbox = monster_hitbox.inflate(-390, -200)

    monster_x += monster_speed - moved
    screen.blit(monster, (monster_x, 0))

    total_x = player_x - settings.HALLWAY_X

    monster_speed = settings.MONSTER_SPEED + (total_x // 1000) * 0.1

    if settings.debugmode:
        pygame.draw.rect(screen, (255, 0, 0), monster_hitbox, 2)

def jumpscare(screen):
    global scare, jumpscare_1, jumpscare_2, jumpscare_3, jumpscare_4

    screen.blit(scare, (0, 0))