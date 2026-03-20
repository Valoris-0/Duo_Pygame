import os
import pygame

pygame.init()
import settings

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)

start_screen = pygame.image.load("assets/images/Start_screen.png").convert_alpha()
start_screen = pygame.transform.scale(start_screen, (800, 400))

victory_screen = pygame.image.load("assets/images/Victory_screen.png")
victory_screen = pygame.transform.scale(victory_screen, (800, 400))

victory_screen_active = False
victory_timer = 0


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

font_normal = pygame.font.Font("assets/fonts/Heartless.ttf", 36)
font_large = pygame.font.Font("assets/fonts/Heartless.ttf", 96)

clock = pygame.time.Clock()

def main():
    player = Player(x=0, width=50, height=50)

    game.init_resources()
    
    settings_screen = SettingsMenu()
    game_screen = GameScreen(player, settings_screen)

    running = True
    scare_timer = 0.0
    is_loading = False
    loading_timer = 0.0
    target_load_time = 0.0
    display_progress = 0.0

    while running:
        dt = clock.tick(settings.FPS) / 1000.0
        global screen, victory_screen_active, victory_timer
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
                is_loading = True
                loading_timer = 0.0
                target_load_time = random.uniform(3.0, 7.0)
                display_progress = 0.0
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
                    start_menu = False
                    game_screen.active = False
                    settings_screen.active = False
                    victory_screen_active = True
            
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
        elif start_menu:
            screen.fill((0, 0, 0))
            screen.blit(start_screen, (0, 0))
            screen.blit(start_text, start_text_rect)
            screen.blit(titel_text, titel_text.get_rect(center=(800 // 2, 100)))
        
        #Victory screen
        elif victory_screen_active:
            screen.blit(victory_screen, (0, 0))
            font_normal = pygame.font.Font("assets/fonts/Heartless.ttf", 80)
            text = font_normal.render("VICTORY", True, (255, 215, 0))
            screen.blit(text, text.get_rect(center=(settings.WIDTH // 2, settings.HEIGHT // 2 - 50)))

        #Loading screen
        elif is_loading:
            screen.fill((0, 0, 0))
            screen.blit(game.start_screen, (0, 0))
            
            loading_timer += dt
            
            bar_width = 400
            bar_height = 30
            bar_x = (settings.WIDTH - bar_width) // 2
            bar_y = settings.HEIGHT // 2 + 50
            
            pygame.draw.rect(screen, (50, 50, 50), (bar_x, bar_y, bar_width, bar_height), border_radius=15)
            
            real_progress = loading_timer / target_load_time
            # Made by AI
            # ---------------------------------------------------------------------------------------
            if random.random() < 0.05:
                display_progress += random.uniform(0.05, 0.2)
            else:
                display_progress += dt * 0.05

            display_progress = max(real_progress - 0.2, min(display_progress, real_progress + 0.15))
            display_progress = min(1.0, display_progress)
            # --------------------------------------------------------------------------------------
            if loading_timer >= target_load_time:
                display_progress = 1.0
            
            fill_width = int(bar_width * display_progress)
            if fill_width > 0:
                pygame.draw.rect(screen, (0, 200, 0), (bar_x, bar_y, fill_width, bar_height), border_radius=15)

            if loading_timer >= target_load_time - 0.3:
                game.play_music.stop_music()

            if loading_timer >= target_load_time:
                is_loading = False
                game_screen.active = True

        #Start menu
        elif settings.start_menu:
            screen.fill((0, 0, 0))
            game_screen.update(screen, dt)

        #Game
        elif game_screen.active and not settings.scare and not settings.heartrate_scare:
            screen.fill((0, 0, 0))
            game_screen.update(screen, dt)

        elif settings.scare or settings.heartrate_scare:
            screen.fill((0, 0, 0))
            screen.blit(monster.scare, (0, 0))
            scare_timer += dt
            if settings.heartrate_scare and scare_timer < 2.0:
                heartrate_text = font_normal.render("HEARTRATE TOO HIGH THE MONSTER FOUND YOU!", True, (255, 0, 0))
                screen.blit(heartrate_text, heartrate_text.get_rect(center=(settings.WIDTH // 2, settings.HEIGHT // 2)))
            if scare_timer > 2.0:
                font_normal = pygame.font.Font("assets/fonts/Heartless.ttf", 36)
                text = font_normal.render("Press any key or click to restart", True, (255, 100, 0))
                screen.blit(text, text.get_rect(center=(settings.WIDTH // 2, settings.HEIGHT - 50)))
                game.play_music_scare.stop_music()
                if any(pygame.key.get_pressed()) or pygame.mouse.get_pressed()[0]:
                    reset_game(player)
                    game_screen.active = False
                    settings_screen.active = False
                    settings_screen.waiting_for_key_left = False
                    settings_screen.waiting_for_key_right = False
                    settings.start_menu = True
                    scare_timer = 0

        elif victory_screen_active:
            victory_timer += dt
            if victory_timer > 3.0:
                font_normal = pygame.font.Font("assets/fonts/Heartless.ttf", 36)
                text = font_normal.render("Press any key or click to restart", True, (255, 100, 0))
                screen.blit(text, text.get_rect(center=(settings.WIDTH // 2, settings.HEIGHT - 50)))
                if any(pygame.key.get_pressed()) or pygame.mouse.get_pressed()[0]:
                    victory_screen_active = False
                    victory_timer = 0
                    start_menu = True
                    
        if not settings.start_menu and not settings.scare and not settings.heartrate_scare and not settings_screen.active and not is_loading:
            settings.HIGHSCORE += dt

        pygame.display.update()
        clock.tick(settings.FPS)


    pygame.quit()
    sys.exit()

main()
