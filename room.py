import pygame

room_1 = pygame.image.load("assets/images/Rooms/Room_1.png")

room_1 = pygame.transform.scale(room_1, (600, 500))

def draw_room(screen):
    screen.blit(room_1, (0, 0))