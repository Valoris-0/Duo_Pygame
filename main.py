import os

os.environ["SDL_AUDIODRIVER"] = "dummy"
import pygame

pygame.init()
import settings

# Scherm
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)

start_screen = pygame.image.load("assets/images/Start_screen.png").convert_alpha()
start_screen = pygame.transform.scale(start_screen, (800, 400))

victory_screen = pygame.image.load("assets/images/Victory_screen.png")
victory_screen = pygame.transform.scale(victory_screen, (800, 400))

victory_screen_active = False
victory_timer = 0


import sys
from player import Player
from music import MusicManager
from game_reset import reset_game
import settings
import monster
import room_2_file
from settings_screen import SettingsMenu
from game import GameScreen

font_normal = pygame.font.Font("assets/fonts/Heartless.ttf", 36)
start_text = font_normal.render("START", True, (255, 100, 0))
start_text_rect = start_text.get_rect(center=(800 // 2, 400 // 2))

font_large = pygame.font.Font("assets/fonts/Heartless.ttf", 96)
titel_text = font_large.render("CARNAGE CORRIDOR", True, (136, 8, 8))

clock = pygame.time.Clock()

def main():
    player = Player(x=0, width=50, height=50)

    # Initialize and play background music
    music_manager = MusicManager("assets/sounds/background.mp3")
    music_manager.play_music()

    settings_screen = SettingsMenu()
    game_screen = GameScreen(player, settings_screen)

    running = True
    start_menu = True
    scare_timer = 0.0

    while running:
        dt = clock.tick(settings.FPS) / 1000.0
        global screen, victory_screen_active, victory_timer
        desired_size = (settings.WIDTH, settings.HEIGHT)
        if screen.get_size() != desired_size:
            screen = pygame.display.set_mode(desired_size)
        #Event handling
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and start_text_rect.collidepoint(event.pos) and start_menu:
                if start_menu:
                    reset_game(player)
                    start_menu = False
                    settings_screen.active = False
                    settings_screen.waiting_for_key_left = False
                    settings_screen.waiting_for_key_right = False
                    game_screen.active = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                settings.debugmode = not settings.debugmode
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                if settings.e_knop_on_screen == "door":
                    settings.in_room = not settings.in_room
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
                    
            if not start_menu and not settings.solving and not settings.scare_active:
                settings_screen.handle_event(event)
            
        #Start menu
        if start_menu:
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

            
        
        #Settings menu
        elif settings_screen.active:
            settings_screen.draw(screen)

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
                if any(pygame.key.get_pressed()) or pygame.mouse.get_pressed()[0]:
                    reset_game(player)
                    game_screen.active = False
                    settings_screen.active = False
                    settings_screen.waiting_for_key_left = False
                    settings_screen.waiting_for_key_right = False
                    start_menu = True
                    scare_timer = 0

        if victory_screen_active:
            victory_timer += dt
            if victory_timer > 3.0:
                font_normal = pygame.font.Font("assets/fonts/Heartless.ttf", 36)
                text = font_normal.render("Press any key or click to restart", True, (255, 100, 0))
                screen.blit(text, text.get_rect(center=(settings.WIDTH // 2, settings.HEIGHT - 50)))
                if any(pygame.key.get_pressed()) or pygame.mouse.get_pressed()[0]:
                    victory_screen_active = False
                    victory_timer = 0
                    start_menu = True
                    

        pygame.display.update()
        clock.tick(settings.FPS)


    pygame.quit()
    sys.exit()

main()
