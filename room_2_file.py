import pygame

room_2_picture = pygame.image.load("assets/images/Rooms/Room_2.png")

room_2_picture = pygame.transform.scale(room_2_picture, (600, 500))

e_knop = pygame.image.load("assets/images/e_knop.png")
e_knop = pygame.transform.scale(e_knop, (50, 50))

def draw_room(screen):
    screen.blit(room_2_picture, (0, 0))