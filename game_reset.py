import game
import pygame

import hallway
import kluis
import Kluis_ani
import monster
import player as player_module
import room_1_file
import room_2_file
import settings
import elektriciteitskast
import heartrate
import room_3_file

def reset_game(player):
    settings.reset_game_state(new_code=True)
    hallway.reset_hallway()
    monster.reset_monster()
    kluis.reset_kluis_state()
    player_module.reset_player_state(player)
    elektriciteitskast.reset_elektriciteitskast()
    heartrate.reset_heartrate()
    Kluis_ani.reset_kluis_animatie()

    room_3_file.Heartrate = None

    #, room_2_file, room_3_file

    game.rooms = [room_1_file, room_2_file, room_3_file ]
    
    return pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))