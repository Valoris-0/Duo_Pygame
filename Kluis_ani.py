import pygame
import random

kluis_animaties = []
for i in range(1,7):
    kluis = pygame.image.load(f"assets/kluis_openen_{i}.png").convert()
    kluis_animaties.append(kluis)

sleutel_1 = pygame.image.load("assets/images/Rooms/sleutel_1.png").convert_alpha()
sleutel_2 = pygame.image.load("assets/images/Rooms/sleutel_2.png").convert_alpha()
sleutel_3 = pygame.image.load("assets/images/Rooms/sleutel_3.png").convert_alpha()

sleutels = []

for i in range (3):
    sleutels.append(random.choice([sleutel_1, sleutel_2, sleutel_3]))

animatie_timer_kluis = 0
animatie_timer_sleutel = 0


def kluis_openen(screen):
    global animatie_timer_kluis, animatie_timer_sleutel
    if animatie_timer_kluis < 10:
        screen.blit(kluis_animaties[0], (250, 100))
    elif animatie_timer_kluis < 20:
        screen.blit(kluis_animaties[1], (250, 100))
    elif animatie_timer_kluis < 30:
        screen.blit(kluis_animaties[2], (250, 100))
    elif animatie_timer_kluis < 40:
        screen.blit(kluis_animaties[3], (250, 100))
    elif animatie_timer_kluis < 50:
        screen.blit(kluis_animaties[4], (250, 100))
    elif animatie_timer_kluis < 60:
        screen.blit(kluis_animaties[5], (250, 100))
    
    if animatie_timer_kluis > 50:
        animatie_timer_sleutel += 1
        if animatie_timer_sleutel < 10:
            screen.blit(sleutels[0], (0,0))