import pygame
import settings

paper = pygame.image.load("assets/images/Rooms/code_paper.png").convert_alpha()
paper = pygame.transform.scale(paper, (200, 200))
font = pygame.font.SysFont(None, 50)
paper_sound_played = False

def open_paper(screen):
    global font, paper_sound_played
    
    screen.blit(paper, (200, 150))

    code_string = "".join(map(str, settings.code))
    text = font.render(code_string, True, (0,0,0))

    screen.blit(text, (255, 240))