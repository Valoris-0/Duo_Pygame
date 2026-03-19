import pygame
import settings

room_3_picture = pygame.image.load("assets/images/Rooms/room_3.png")
room_3_picture = pygame.transform.scale(room_3_picture, (600, 500))

def draw_room(screen):
    screen.blit(room_3_picture, (0, 0))

    if settings.e_knop_on_screen == "bed":
        e_knop = pygame.image.load("assets/images/e_knop.png").convert_alpha()
        e_knop = pygame.transform.scale(e_knop, (50, 50))
        screen.blit(e_knop, (375, 325))
    elif settings.e_knop_on_screen == "machine":
        e_knop = pygame.image.load("assets/images/e_knop.png").convert_alpha()
        e_knop = pygame.transform.scale(e_knop, (50, 50))
        screen.blit(e_knop, (440, 230))
    elif settings.e_knop_on_screen == "doos":
        e_knop = pygame.image.load("assets/images/e_knop.png").convert_alpha()
        e_knop = pygame.transform.scale(e_knop, (50, 50))
        screen.blit(e_knop, (390, 100))
    elif settings.e_knop_on_screen == "rolstoel":
        e_knop1 = pygame.image.load("assets/images/e_knop.png").convert_alpha()
        e_knop1 = pygame.transform.scale(e_knop1, (50, 50))
        screen.blit(e_knop1, (190, 120))
    elif settings.e_knop_on_screen == "door":
        e_knop = pygame.image.load("assets/images/e_knop.png").convert_alpha()
        e_knop = pygame.transform.scale(e_knop, (50, 50))
        screen.blit(e_knop, (215, 380))
       