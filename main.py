import os
os.environ["SDL_AUDIODRIVER"] = "dummy"
import pygame

import kluis
import sys
from player import Player
from music import MusicManager
from game_reset import reset_game
import settings
import monster
from settings_screen import SettingsMenu
from game import GameScreen

pygame.init()


# Scherm
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)

#buttons
start_button = pygame.Rect(settings.WIDTH // 2 - 100, settings.HEIGHT // 2 - 50, 200, 100)

#textjes
font = pygame.font.SysFont(None, 24)
start_text = font.render("START", True, (0, 0, 0))

clock = pygame.time.Clock()

def main():
    player = Player(x=0, width=50, height=50)

    #Music
    music_manager = MusicManager("assets/sounds/background.mp3")
    music_manager.play_music()

    settings_screen = SettingsMenu()
    game_screen = GameScreen(player, settings_screen)

    running = True
    start_menu = True
    scare_timer = 0.0

    while running:
        dt = clock.tick(settings.FPS) / 1000.0
        global screen
        #Event handling
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos):
                if start_menu:
                    screen = reset_game(player)
                    start_menu = False
                    settings_screen.active = False
                    settings_screen.waiting_for_key_left = False
                    settings_screen.waiting_for_key_right = False
                    game_screen.active = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q and settings.debugmode:
                    settings.in_room = not settings.in_room
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                settings.debugmode = not settings.debugmode
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                if settings.e_knop_on_screen == "door":
                    settings.in_room = not settings.in_room
                    
            
            if not start_menu and not settings.solving and not settings.scare_active:
                settings_screen.handle_event(event)
        
        #Start menu
        if start_menu:
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (0, 200, 0), start_button, border_radius=50)
            screen.blit(start_text, start_text.get_rect(center=start_button.center))

        #Settings menu
        elif settings_screen.active:
            settings_screen.draw(screen)

        #Game
        elif game_screen.active and not settings.scare:
            screen = game_screen.update(screen, dt)

        elif settings.scare:
            screen.fill((0, 0, 0))
            screen.blit(monster.scare, (0, 0))
            scare_timer += dt
            if scare_timer > 2.0:
                if any(pygame.key.get_pressed()) or pygame.mouse.get_pressed()[0]:
                    screen = reset_game(player)
                    game_screen.active = False
                    settings_screen.active = False
                    settings_screen.waiting_for_key_left = False
                    settings_screen.waiting_for_key_right = False
                    start_menu = True
                    scare_timer = 0
                        

        pygame.display.update()

    pygame.quit()
    sys.exit()

main()
