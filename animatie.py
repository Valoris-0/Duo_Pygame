import pygame
import random
import settings

kluis_openen_1 = pygame.image.load("assets/images/Rooms/kluis_animatie/animatie_kluis_1.png")
kluis_openen_2 = pygame.image.load("assets/images/Rooms/kluis_animatie/animatie_kluis_2.png")
kluis_openen_3 = pygame.image.load("assets/images/Rooms/kluis_animatie/animatie_kluis_3.png")
kluis_openen_4 = pygame.image.load("assets/images/Rooms/kluis_animatie/animatie_kluis_4.png")
kluis_openen_5 = pygame.image.load("assets/images/Rooms/kluis_animatie/animatie_kluis_5.png")


sleutel_1 = pygame.image.load("assets/images/Rooms/sleutel_1.png")
sleutel_2 = pygame.image.load("assets/images/Rooms/sleutel_2.png")
sleutel_3 = pygame.image.load("assets/images/Rooms/sleutel_3.png")

sleutel_1 = pygame.transform.scale(sleutel_1, (600, 500))
sleutel_2 = pygame.transform.scale(sleutel_2, (600, 500))
sleutel_3 = pygame.transform.scale(sleutel_3, (600, 500))

sleutels = []

for i in range (3):
    sleutels.append(random.choice([sleutel_1, sleutel_2, sleutel_3]))

animatie_timer_kluis = 0
animatie_timer_sleutel = 0


def kluis_openen(screen):
    global animatie_timer_kluis, animatie_timer_sleutel
    animatie_timer_kluis += 1
    if animatie_timer_kluis < 15:
        screen.blit(kluis_openen_1, (250, 100))
    elif animatie_timer_kluis < 30:
        screen.blit(kluis_openen_2, (250, 100))
    elif animatie_timer_kluis < 45:
        screen.blit(kluis_openen_3, (250, 100))
    elif animatie_timer_kluis < 60:
        screen.blit(kluis_openen_4, (250, 100))
    elif animatie_timer_kluis < 75:
        screen.blit(kluis_openen_5, (250, 100))

    
    if animatie_timer_kluis > 75:
        animatie_timer_sleutel += 1
        if animatie_timer_sleutel < 30:
            screen.blit(sleutels[0], (0,0))
    
    if animatie_timer_kluis > 105:
        settings.animating_safe = False