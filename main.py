import os

import electrisiteitskast
os.environ["SDL_AUDIODRIVER"] = "dummy"
import pygame
import random



import kluis
import sys
from player import Player
from music import MusicManager
import hallway
import settings
import monster
import room_1_file
import room_2_file
import room_3_file
import paper_code
import jumpscare

pygame.init()


# Set up the display
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption(settings.TITLE)

clock = pygame.time.Clock()
#room_1_file.draw_room, room_2_file.draw_room, room_3_file.draw_room
rooms = [room_2_file.draw_room]


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
                # entering hallway: adjust window size and reset player position
                settings.WIDTH = 800
                settings.HEIGHT = 400
                if screen.get_size() != (settings.WIDTH, settings.HEIGHT):
                    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

                player.x = 0
                player.y = 140

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
                chosen_room = random.choice(rooms)
                
                if screen.get_size() != (settings.WIDTH, settings.HEIGHT):
                    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

                settings.current_mode = "room"
            else:
                screen.fill((0, 0, 0)) 
                chosen_room(screen)
                moved = player.handle_input_top(screen, room_number = chosen_room.__module__)
                player.update()
                player.draw_top(screen)
                
                if settings.scare_active:
                    jumpscare.scare(screen)
                

                if settings.solving and chosen_room.__module__ == "room_1_file":
                    
                    # Verchil tussen opened object en e_knop_on_screen is zodat je niet meerdere keeren kan openen als je het al geopend/gedaan hebt
                    if settings.opened_object == "kluis":
                        pos = pygame.mouse.get_pos()
                        kluis.open_kluis(screen, pos)
                    elif settings.opened_object in ("bed", "doos"):
                        paper_code.open_paper(screen)

                elif settings.solving and chosen_room.__module__ == "room_2_file":
                    if settings.opened_object == "electrisiteitskast":
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        electrisiteitskast.meterkast(screen, mouse_x, mouse_y)
                    elif settings.opened_object in ("bed", "doos"):
                        gereedschap = pygame.image.load("assets/images/Rooms/elektriciteit/gereedschap.png")
                        gereedschap = pygame.transform.scale(gereedschap, (600, 500))
                        screen.blit(gereedschap, (0, 0))
                        settings.gereedschap_got = True




        pygame.display.update()
        clock.tick(settings.FPS)


    pygame.quit()
    sys.exit()

main()
