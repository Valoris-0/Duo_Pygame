import pygame
import settings

room_3_picture = pygame.image.load("assets/images/Rooms/room_3.png")
room_3_picture = pygame.transform.scale(room_3_picture, (600, 500))

def draw_room(screen):
    screen.blit(room_3_picture, (0, 0))

    if settings.e_knop_on_screen == "bed":
        e_knop = pygame.image.load("assets/images/e_knop.png").convert_alpha()
        e_knop = pygame.transform.scale(e_knop, (50, 50))
        screen.blit(e_knop, (350, 350))
       