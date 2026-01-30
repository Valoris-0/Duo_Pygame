import os
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame
import sys
from player import Player
from music import MusicManager
import hallway
import settings

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
        # 1. Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Update
        player.update()

        # 3. Draw
        
        screen.fill((100, 149, 237))
        moved = player.handle_input(screen)
        hallway.moving(screen, moved)
        player.draw(screen)
        pygame.display.update()
        clock.tick(settings.FPS)


    pygame.quit()
    sys.exit()

main()
