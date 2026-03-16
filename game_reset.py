import pygame

import hallway
import kluis
import monster
import player as player_module
import settings


def reset_game(player):
    settings.reset_game_state(new_code=True)
    hallway.reset_hallway()
    monster.reset_monster()
    kluis.reset_kluis_state()
    player_module.reset_player_state(player)
    return pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))