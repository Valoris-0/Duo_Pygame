import pygame

code = pygame.image.load("assets/images/Rooms/kluis.jpeg")
code = pygame.transform.scale(code, (200, 150))

def open_kluis(screen):
    screen.blit(code, (200, 150))