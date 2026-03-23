import pygame
import game
import settings
import monster
from game_reset import reset_game

def reset():
    """Reset death screen variables."""
    return 0.0

def update(screen, dt, scare_timer, player, font_normal, settings_screen, game_screen):
    screen.fill((0, 0, 0))
    screen.blit(monster.scare, (0, 0))
    scare_timer += dt
    
    if settings.heartrate_scare and scare_timer < 2.0:
        heartrate_text = font_normal.render("HEARTRATE TOO HIGH THE MONSTER FOUND YOU!", True, (255, 0, 0))
        screen.blit(heartrate_text, heartrate_text.get_rect(center=(settings.WIDTH // 2, settings.HEIGHT // 2)))
    
    if scare_timer > 2.0:
        text = font_normal.render("Press any key or click to restart", True, (255, 100, 0))
        screen.blit(text, text.get_rect(center=(settings.WIDTH // 2, settings.HEIGHT - 50)))
        game.play_music_scare.stop_music()
        if any(pygame.key.get_pressed()) or pygame.mouse.get_pressed()[0]:
            reset_game(player)
            game.play_music.play_music()
            game_screen.active = False
            settings_screen.active = False
            settings_screen.waiting_for_key_left = False
            settings_screen.waiting_for_key_right = False
            settings.start_menu = True
            scare_timer = 0
    
    return scare_timer
