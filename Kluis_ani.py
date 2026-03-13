import pygame
import random

kluis_openen_1 = pygame.image.load("assets/kluis_openen_1.png")
kluis_openen_2 = pygame.image.load("assets/kluis_openen_2.png")
kluis_openen_3 = pygame.image.load("assets/kluis_openen_3.png")
kluis_openen_4 = pygame.image.load("assets/kluis_openen_4.png")
kluis_openen_5 = pygame.image.load("assets/kluis_openen_5.png")
kluis_openen_6 = pygame.image.load("assets/kluis_openen_6.png")

sleutel_1 = pygame.image.load("assets/images/Rooms/sleutel_1.png")
sleutel_2 = pygame.image.load("assets/images/Rooms/sleutel_2.png")
sleutel_3 = pygame.image.load("assets/images/Rooms/sleutel_3.png")

sleutels = []

for i in range (3):
    sleutels.append(random.choice([sleutel_1, sleutel_2, sleutel_3]))

animatie_timer_kluis = 0
animatie_timer_sleutel = 0


def kluis_openen(screen):
    global animatie_timer_kluis, animatie_timer_sleutel
    if animatie_timer_kluis < 10:
        screen.blit(kluis_openen_1, (250, 100))
    elif animatie_timer_kluis < 20:
        screen.blit(kluis_openen_2, (250, 100))
    elif animatie_timer_kluis < 30:
        screen.blit(kluis_openen_3, (250, 100))
    elif animatie_timer_kluis < 40:
        screen.blit(kluis_openen_4, (250, 100))
    elif animatie_timer_kluis < 50:
        screen.blit(kluis_openen_5, (250, 100))
    elif animatie_timer_kluis < 60:
        screen.blit(kluis_openen_6, (250, 100))
    
    if animatie_timer_kluis > 50:
        animatie_timer_sleutel += 1
        if animatie_timer_sleutel < 10:
            screen.blit(sleutels[0], (0,0))