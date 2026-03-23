import pygame
import game
import highscore
import settings

def reset():
    return 0.0

def update(screen, dt, victory_timer, font_normal, victory_screen_image):
    screen.blit(victory_screen_image, (0, 0))
    font_victory = pygame.font.Font("assets/fonts/Heartless.ttf", 80)
    text = font_victory.render("VICTORY", True, (255, 215, 0))
    screen.blit(text, text.get_rect(center=(settings.WIDTH // 2, settings.HEIGHT // 2 - 50)))
    game.play_music_game.stop_music()
    game.play_music_victory.play_music()

    score = settings.HIGHSCORE
    correct_highscore = highscore.load_highscore()

    font = pygame.font.SysFont(None, 40)
    score_text = font.render(f"Score: {highscore.format_time(int(score))}", True, (255, 100, 0))
    screen.blit(score_text, score_text.get_rect(center=(settings.WIDTH // 2, settings.HEIGHT // 2 + 50)))

    if score > correct_highscore:
        new_highscore_text = font.render("NEW HIGHSCORE!", True, (255, 215, 0))
        screen.blit(new_highscore_text, new_highscore_text.get_rect(center=(settings.WIDTH // 2, settings.HEIGHT // 2 + 100)))
        highscore.save_highscore(int(score))

    if victory_timer <= 2.0:
        victory_timer += dt
    if victory_timer > 2.0:
        text = font_normal.render("Press any key or click to restart", True, (255, 100, 0))
        screen.blit(text, text.get_rect(center=(settings.WIDTH // 2, settings.HEIGHT - 50)))
        if any(pygame.key.get_pressed()) or pygame.mouse.get_pressed()[0]:
            settings.start_menu = True
            settings.won = False
            game.play_music_victory.stop_music()
            victory_timer = 0.0
    
    return victory_timer
