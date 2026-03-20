import pygame
import random

SCORE_FILE = "highscore.txt"

TITLE = "CARNAGE CORRIDOR"
PLAYER_WIDTH = 80
PLAYER_HEIGHT = 144
LEFT_MOVEMENT = pygame.K_LEFT
RIGHT_MOVEMENT = pygame.K_RIGHT
UP_MOVEMENT = pygame.K_UP
DOWN_MOVEMENT = pygame.K_DOWN
E_PRESS = pygame.K_e
K_ESCAPE = pygame.K_ESCAPE
MUSIC_VOLUME = 0.5
FPS = 120
SPEED = 350
MONSTER_SPEED = 60

_DEFAULTS = {
    'WIDTH': 800,
    'HEIGHT': 400,
    'LOOKING_RIGHT': True,
    'MOVING': False,
    'IS_MOVING_NOW': False,
    'HALLWAY_X': 0,
    'last_mover': "up",
    'HEARTRATE': 150,
    'HIGHSCORE': 0.0,
    'debugmode': False,
    'in_room': False,
    'current_mode': "begin",
    'room_reset': True,
    'current_room': 0,
    'interactive_spot': None,
    'opened_object': None,
    'start_menu': True,
    'e_knop_on_screen': "",
    'solving': False,
    'keys_collected': [True, True, True],
    'code_ingevoerd': [],
    'code_correct': False,
    'animating_safe': False,
    'mouse_was_pressed': False,
    'keys_were_pressed': set(),
    'scare_active': False,
    'scare_countdown': 2.0,
    'gereedschap_got': False,
    'scare': False,
    'heartrate_scare': False,
    'HALLWAY_DOOR_X': 375,
    'won': False,
}

def generate_code():
    return [random.randint(0, 9) for _ in range(4)]

WIDTH = _DEFAULTS['WIDTH']
HEIGHT = _DEFAULTS['HEIGHT']
LOOKING_RIGHT = _DEFAULTS['LOOKING_RIGHT']
MOVING = _DEFAULTS['MOVING']
IS_MOVING_NOW = _DEFAULTS['IS_MOVING_NOW']
HALLWAY_X = _DEFAULTS['HALLWAY_X']
last_mover = _DEFAULTS['last_mover']
HEARTRATE = _DEFAULTS['HEARTRATE']
HIGHSCORE = _DEFAULTS['HIGHSCORE']
debugmode = _DEFAULTS['debugmode']
in_room = _DEFAULTS['in_room']
current_mode = _DEFAULTS['current_mode']
room_reset = _DEFAULTS['room_reset']
current_room = _DEFAULTS['current_room']
interactive_spot = _DEFAULTS['interactive_spot']
opened_object = _DEFAULTS['opened_object']
start_menu = _DEFAULTS['start_menu']
e_knop_on_screen = _DEFAULTS['e_knop_on_screen']
solving = _DEFAULTS['solving']
keys_collected = _DEFAULTS['keys_collected']
code_ingevoerd = _DEFAULTS['code_ingevoerd']
code_correct = _DEFAULTS['code_correct']
animating_safe = _DEFAULTS['animating_safe']
mouse_was_pressed = _DEFAULTS['mouse_was_pressed']
keys_were_pressed = _DEFAULTS['keys_were_pressed']
scare_active = _DEFAULTS['scare_active']
scare_countdown = _DEFAULTS['scare_countdown']
gereedschap_got = _DEFAULTS['gereedschap_got']
scare = _DEFAULTS['scare']
heartrate_scare = _DEFAULTS['heartrate_scare']
HALLWAY_DOOR_X = _DEFAULTS['HALLWAY_DOOR_X']
won = _DEFAULTS['won']
code = generate_code()

def reset_game_state(new_code=True):
    global WIDTH, HEIGHT, LOOKING_RIGHT, MOVING, IS_MOVING_NOW, HALLWAY_X
    global last_mover, in_room, current_mode, room_reset, interactive_spot
    global opened_object, e_knop_on_screen, solving, code, code_ingevoerd
    global code_correct, mouse_was_pressed, keys_were_pressed, scare_active
    global scare_countdown, scare, HALLWAY_DOOR_X, gereedschap_got, keys_collected
    global HEARTRATE, HIGHSCORE, debugmode, MONSTER_SPEED, animating_safe, heartrate_scare, won, current_room

    WIDTH = _DEFAULTS['WIDTH']
    HEIGHT = _DEFAULTS['HEIGHT']
    LOOKING_RIGHT = _DEFAULTS['LOOKING_RIGHT']
    MOVING = _DEFAULTS['MOVING']
    IS_MOVING_NOW = _DEFAULTS['IS_MOVING_NOW']
    HALLWAY_X = _DEFAULTS['HALLWAY_X']
    last_mover = _DEFAULTS['last_mover']
    HEARTRATE = _DEFAULTS['HEARTRATE']
    HIGHSCORE = _DEFAULTS['HIGHSCORE']
    in_room = _DEFAULTS['in_room']
    current_mode = _DEFAULTS['current_mode']
    room_reset = _DEFAULTS['room_reset']
    interactive_spot = _DEFAULTS['interactive_spot']
    opened_object = _DEFAULTS['opened_object']
    e_knop_on_screen = _DEFAULTS['e_knop_on_screen']
    solving = _DEFAULTS['solving']
    keys_collected = _DEFAULTS['keys_collected'].copy()
    code_ingevoerd = _DEFAULTS['code_ingevoerd'].copy()
    code_correct = _DEFAULTS['code_correct']
    mouse_was_pressed = _DEFAULTS['mouse_was_pressed']
    keys_were_pressed = _DEFAULTS['keys_were_pressed'].copy()
    scare_active = _DEFAULTS['scare_active']
    scare_countdown = _DEFAULTS['scare_countdown']
    gereedschap_got = _DEFAULTS['gereedschap_got']
    scare = _DEFAULTS['scare']
    heartrate_scare = _DEFAULTS['heartrate_scare']
    HALLWAY_DOOR_X = _DEFAULTS['HALLWAY_DOOR_X']
    won = _DEFAULTS['won']
    
    if new_code:
        code = generate_code()
