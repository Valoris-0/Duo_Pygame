import pygame


spin_scare = pygame.image.load("assets/images/jumpscares/jumpscare_spin.png").convert()
spin_scare = pygame.transform.scale(spin_scare, (600, 500))

def scare(screen):
    screen.blit(spin_scare, (0, 0))