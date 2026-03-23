import pygame
import random
import game
import settings

def update(screen, dt, loading_timer, target_load_time, display_progress):
    screen.fill((0, 0, 0))
    screen.blit(game.start_screen, (0, 0))
    
    loading_timer += dt
    
    bar_width = 400
    bar_height = 30
    bar_x = (settings.WIDTH - bar_width) // 2
    bar_y = settings.HEIGHT // 2 + 50
    
    pygame.draw.rect(screen, (50, 50, 50), (bar_x, bar_y, bar_width, bar_height), border_radius=15)
    
    real_progress = loading_timer / target_load_time
    
    if random.random() < 0.05:
        display_progress += random.uniform(0.05, 0.2)
    else:
        display_progress += dt * 0.05

    display_progress = max(real_progress - 0.2, min(display_progress, real_progress + 0.15))
    display_progress = min(1.0, display_progress)
    
    if loading_timer >= target_load_time:
        display_progress = 1.0
    
    fill_width = int(bar_width * display_progress)
    if fill_width > 0:
        pygame.draw.rect(screen, (0, 200, 0), (bar_x, bar_y, fill_width, bar_height), border_radius=15)

    if loading_timer >= target_load_time - 0.3:
        game.play_music.stop_music()

    finished = loading_timer >= target_load_time
    
    return loading_timer, display_progress, finished
