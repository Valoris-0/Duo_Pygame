import os
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame
import sys
from player import Player
from music import MusicManager
import hallway
import settings
from settings_screen import SettingsMenu

pygame.init()


#Scherm
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)

#buttons
start_button = pygame.Rect(settings.WIDTH // 2 - 100, settings.HEIGHT // 2 - 50, 200, 100)

#textjes
font = pygame.font.SysFont(None, 24)
start_text = font.render("START", True, (0, 0, 0))

clock = pygame.time.Clock()

def main():
    player = Player(x=0)

    #Muziek
    music_manager = MusicManager("assets/sounds/background.mp3")
    music_manager.play_music()

    settings_menu_screen = SettingsMenu()

    #Variabelen
    running = True
    start_menu = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #starting the game
            if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos):
                if start_menu:
                    start_menu = False

            if not start_menu:
                settings_menu_screen.handle_event(event)

        #Game menu
        if not settings_menu_screen.active and not start_menu:
            moved = player.handle_input(screen)
            player.update()

            #alle blits
            screen.fill((100, 149, 237))
            hallway.moving(screen, moved)
            player.draw(screen)

            settings_menu_screen.draw(screen)
        
        #Settings menu
        elif settings_menu_screen.active and not start_menu:
            settings_menu_screen.draw(screen)

        #Start menu
        elif start_menu and not settings_menu_screen.active:
            screen.fill((0, 0, 0))

            pygame.draw.rect(screen, (0, 200, 0), start_button, border_radius=50)
            screen.blit(start_text, start_text.get_rect(center=start_button.center))
        
        pygame.display.update()
        clock.tick(settings.FPS)


    pygame.quit()
    sys.exit()

main()
