import pygame

import hallway
import kluis
import Kluis_ani
import monster
import player as player_module
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
    kluis.reset_kluis_state()

    room_3_file.Heartrate = None
    
    
    return pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))