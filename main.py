import os
os.environ["SDL_AUDIODRIVER"] = "dummy"
import pygame

import kluis
import sys
from player import Player
from music import MusicManager
import hallway
import settings
import monster
import room
import paper_code
import jumpscare
from settings_screen import SettingsMenu

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

    settings_menu_screen = SettingsMenu()

    running = True
    start_menu = True

    while running:
        global screen
        #Event handling
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos):
                if start_menu:
                    start_menu = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    settings.in_room = not settings.in_room
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                settings.debugmode = not settings.debugmode
            
            if not start_menu and not settings.solving and not settings.scare_active:
                settings_menu_screen.handle_event(event)
        
        #Start menu
        if start_menu:
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (0, 200, 0), start_button, border_radius=50)
            screen.blit(start_text, start_text.get_rect(center=start_button.center))

        #Settings menu
        elif settings_menu_screen.active:
            settings_menu_screen.draw(screen)

        #Game
        else:
            if not settings.in_room:
                if settings.current_mode != "hallway":
                    settings.WIDTH = 800
                    settings.HEIGHT = 400
                    if screen.get_size() != (settings.WIDTH, settings.HEIGHT):
                        screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

                    player.x = 0
                    player.y = 155

                    settings.current_mode = "hallway"
                else:
                    moved = player.handle_input_side(screen)

                    player.update()

                    hallway.moving(screen, moved)
                    monster.moving_monster(screen, moved, player.x)
                    player.draw_side(screen)   # draw side view sprite

                    if player.player_hitbox.colliderect(monster.monster_hitbox):
                        monster.jumpscare(screen)

            else:
                if settings.current_mode != "room":
                    # entering room: change size if needed
                    settings.WIDTH = 600
                    settings.HEIGHT = 500
                    if screen.get_size() != (settings.WIDTH, settings.HEIGHT):
                        screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

                    settings.current_mode = "room"
                else:
                    screen.fill((0, 0, 0))
                    room.draw_room(screen)
                    moved = player.handle_input_top(screen)
                    player.update()
                    player.draw_top(screen)

                    if settings.scare_active:
                        jumpscare.scare(screen)

                    if settings.solving:
                        # use opened_object since e_knop_on_screen is cleared when solved
                        if settings.opened_object == "kluis":
                            pos = pygame.mouse.get_pos()
                            kluis.open_kluis(screen, pos)
                        elif settings.opened_object in ("bed", "doos"):
                            paper_code.open_paper(screen)

            settings_menu_screen.draw(screen)
                
        pygame.display.update()
        clock.tick(settings.FPS)


    pygame.quit()
    sys.exit()

main()
