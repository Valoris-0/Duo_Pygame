import os
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame
import sys
from player import Player
from enemy import Enemy
from music import MusicManager

pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
TITLE = "PyGame Final Project"

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

def main():
    player = Player(x=0, y=0, width=50, height=50)
    enemy = Enemy(x=100, y=100, image_path="assets/images/enemy.png", speed=3)

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
        enemy.update()

        # Check collision
        if player.get_rect().colliderect(enemy.rect):
            music_manager.stop_music()
            running = False

        # 3. Draw
        screen.fill((100, 149, 237))
        player.draw(screen)
        enemy.draw(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

main()
