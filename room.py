import pygame
import settings
import kluis

room_1 = pygame.image.load("assets/images/Rooms/Room_1.png")

room_1 = pygame.transform.scale(room_1, (600, 500))

e_knop = pygame.image.load("assets/images/e_knop.png")
e_knop = pygame.transform.scale(e_knop, (50, 50))

def draw_room(screen):
    keys = pygame.key.get_pressed()
    screen.blit(room_1, (0, 0))

    if settings.e_knop_on_screen == "bed":
        screen.blit(e_knop, (200, 160))

    elif settings.e_knop_on_screen == "kluis":
        screen.blit(e_knop, (450, 240))
        if keys[settings.E_PRESS]:
            settings.solving = True
            

            

    elif settings.e_knop_on_screen == "doos":
        screen.blit(e_knop, (360, 40))