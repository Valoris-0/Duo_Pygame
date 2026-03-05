import os
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame
import sys
from player import Player
from music import MusicManager
import hallway
import settings
import monster
import room

pygame.init()


# Set up the display
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)

clock = pygame.time.Clock()

def main():
    player = Player(x=0, width=50, height=50)

    # Initialize and play background music
    music_manager = MusicManager("assets/sounds/background.mp3")
    music_manager.play_music()

    running = True

    while running:
        global screen
        # 1. Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if not settings.in_room:
            if settings.current_mode != "hallway":
                settings.WIDTH = 800
                settings.HEIGHT = 400
                screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
                settings.current_mode = "hallway"
            else:    
                moved = player.handle_input(screen)
                
                player.update()

                hallway.moving(screen, moved)
                monster.moving_monster(screen, moved, player.x)
                player.draw(screen)

                if player.player_hitbox.colliderect(monster.monster_hitbox):
                    monster.jumpscare(screen)

        else:
            if settings.current_mode != "room":
                settings.WIDTH = 600
                settings.HEIGHT = 500
                screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
                settings.current_mode = "room"
            else:
                screen.fill((0, 0, 0))
                room.draw_room(screen)



        pygame.display.update()
        clock.tick(settings.FPS)


    pygame.quit()
    sys.exit()

main()
