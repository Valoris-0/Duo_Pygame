import pygame
import settings

paper = pygame.image.load("assets/images/Rooms/code_paper.png")
paper = pygame.transform.scale(paper, (200, 200))

def open_doos(screen):
    font = pygame.font.SysFont(None, 50)
    
    screen.blit(paper, (200, 150))

    code_string = "".join(map(str, settings.code))
    text = font.render(code_string, True, (0,0,0))

    screen.blit(text, (255, 240))