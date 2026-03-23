import pygame
import random
import settings


kluis_animaties = []
for i in range(1, 6):
    kluis = pygame.image.load(f"assets/images/Rooms/kluis_animatie/animatie_kluis_{i}.png").convert_alpha()
    kluis_animaties.append(kluis)



sleutel_img = pygame.image.load(f"assets/images/Rooms/sleutel_1.png").convert_alpha()
sleutel_img = pygame.transform.scale(sleutel_img, (300, 200))

kluis_sound = pygame.mixer.Sound("assets\sounds\kluis_openen.mp3")



def reset_kluis_animatie():
    global animatie_timer_kluis, animatie_timer_sleutel, gekozen_sleutel
    animatie_timer_kluis = 0
    animatie_timer_sleutel = 0
    gekozen_sleutel = None

reset_kluis_animatie()

def kluis_openen(screen):
    global animatie_timer_kluis, animatie_timer_sleutel, gekozen_sleutel
    animatie_timer_kluis += 1
    
    if animatie_timer_kluis == 1:
        kluis_sound.play()
    if animatie_timer_kluis < 15:
        screen.blit(kluis_animaties[0], (250, 100))
    elif animatie_timer_kluis < 30:
        screen.blit(kluis_animaties[1], (255, 100))
    elif animatie_timer_kluis < 45:
        screen.blit(kluis_animaties[2], (260, 100))
    elif animatie_timer_kluis < 60:
        screen.blit(kluis_animaties[3], (265, 100))
    elif animatie_timer_kluis < 75:
        screen.blit(kluis_animaties[4], (250, 100))
    
    if animatie_timer_kluis > 75:          
        animatie_timer_sleutel += 1
        if animatie_timer_sleutel < 60:
            screen.blit(sleutel_img, (150, 150))
            settings.keys_collected[0] = True
            
    
    if animatie_timer_kluis > 135:
        settings.animating_safe = False
