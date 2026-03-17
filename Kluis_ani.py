import pygame
import random
import settings

kluis_animaties = []
# Fixed index: loop van 1 tot en met 5 (stop bij 6)
for i in range(1, 6):
    kluis = pygame.image.load(f"assets/images/Rooms/kluis_animatie/animatie_kluis_{i}.png").convert_alpha()
    kluis_animaties.append(kluis)

sleutels = []

for i in range(1, 4):
    sleutel_img = pygame.image.load(f"assets/images/Rooms/sleutel_{i}.png").convert_alpha()
    sleutel_img = pygame.transform.scale(sleutel_img, (600, 500))
    sleutels.append(sleutel_img)

animatie_timer_kluis = 0
animatie_timer_sleutel = 0
gekozen_sleutel = None

def kluis_openen(screen):
    global animatie_timer_kluis, animatie_timer_sleutel, gekozen_sleutel
    animatie_timer_kluis += 1
    
    if animatie_timer_kluis < 15:
        screen.blit(kluis_animaties[0], (250, 100))
    elif animatie_timer_kluis < 30:
        screen.blit(kluis_animaties[1], (250, 100))
    elif animatie_timer_kluis < 45:
        screen.blit(kluis_animaties[2], (250, 100))
    elif animatie_timer_kluis < 60:
        screen.blit(kluis_animaties[3], (250, 100))
    elif animatie_timer_kluis < 75:
        screen.blit(kluis_animaties[4], (250, 100))
    
    if animatie_timer_kluis > 75:
        if gekozen_sleutel is None:
            gekozen_sleutel = random.choice(sleutels)
            
        animatie_timer_sleutel += 1
        if animatie_timer_sleutel < 60:
            screen.blit(gekozen_sleutel, (0, 0))
    
    if animatie_timer_kluis > 135:
        settings.animating_safe = False
