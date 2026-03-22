import os
import pygame

pygame.init()
import highscore
import settings

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)

start_screen = pygame.image.load("assets/images/Start_screen.png").convert_alpha()
start_screen = pygame.transform.scale(start_screen, (800, 400))

victory_screen = pygame.image.load("assets/images/Victory_screen.png")
victory_screen = pygame.transform.scale(victory_screen, (800, 400))

import game
import sys
from player import Player
from music import MusicManager
from game_reset import reset_game
import settings
import monster
from settings_screen import SettingsMenu
from game import GameScreen
import random
import loading_screen
import death_screen
import victory_screen as victory_screen_module

font_normal = pygame.font.Font("assets/fonts/Heartless.ttf", 36)
font_large = pygame.font.Font("assets/fonts/Heartless.ttf", 96)

clock = pygame.time.Clock()

def main():

    player = Player(x=0, width=50, height=50)
    game.init_resources()
    
    settings_screen = SettingsMenu()
    game_screen = GameScreen(player, settings_screen)

    running = True

    while running:
        global screen
        dt = clock.tick(settings.FPS) / 1000.0
        desired_size = (settings.WIDTH, settings.HEIGHT)
        if screen.get_size() != desired_size:
            screen = pygame.display.set_mode(desired_size)

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and game.start_text_rect.collidepoint(event.pos) and settings.start_menu:
                reset_game(player)
                settings.start_menu = False
                settings_screen.active = False
                settings_screen.waiting_for_key_left = False
                settings_screen.waiting_for_key_right = False
                settings.is_loading = True
                settings.loading_timer = 0.0
                settings.target_load_time = random.uniform(3.0, 7.0)
                settings.display_progress = 0.0
            if event.type == pygame.MOUSEBUTTONDOWN and game.options_text_rect.collidepoint(event.pos) and settings.start_menu:
                settings_screen.active = True
                game_screen.active = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                settings.debugmode = not settings.debugmode
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                if settings.e_knop_on_screen == "door":
                    settings.in_room = not settings.in_room
                    settings.e_knop_on_screen = ""
                elif settings.e_knop_on_screen == "exit":
                    settings.start_menu = False
                    game_screen.active = False
                    settings_screen.active = False
                    settings.victory_screen_active = True
            
            if settings.debugmode:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    settings.in_room = not settings.in_room
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    settings.MONSTER_SPEED *= 2
                if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    settings.MONSTER_SPEED /= 2
                if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                    settings.HEARTRATE += 10
                if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                    print(game.rooms)
                    
            if not settings.solving and not settings.scare_active:
                settings_screen.handle_event(event)

        #Settings menu
        if settings_screen.active:
            settings_screen.draw(screen)

        #Start menu
        elif settings.start_menu:
            screen.fill((0, 0, 0))
            game_screen.update(screen, dt)

        #Loading screen
        elif settings.is_loading:
            settings.loading_timer, settings.display_progress, loading_finished = loading_screen.update(screen, dt, settings.loading_timer, settings.target_load_time, settings.display_progress)
            if loading_finished:
                settings.is_loading = False
                game_screen.active = True

        #Game
        elif game_screen.active and not settings.scare and not settings.heartrate_scare:
            screen.fill((0, 0, 0))
            game_screen.update(screen, dt)

        elif settings.scare or settings.heartrate_scare:
            settings.scare_timer = death_screen.update(screen, dt, settings.scare_timer, player, font_normal, settings_screen, game_screen)

        #victory screen
        elif settings.victory_screen_active:
            settings.victory_timer = victory_screen_module.update(screen, dt, settings.victory_timer, font_normal, victory_screen)
            if settings.start_menu:
                settings.victory_screen_active = False

        if not settings.start_menu and not settings.scare and not settings.heartrate_scare and not settings_screen.active and not settings.is_loading and not settings.victory_screen_active:
            settings.HIGHSCORE += dt

        pygame.display.update()
        clock.tick(settings.FPS)


    pygame.quit()
    sys.exit()

main()
