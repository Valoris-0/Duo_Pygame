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

DEFAULTS = {
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

WIDTH = DEFAULTS['WIDTH']
HEIGHT = DEFAULTS['HEIGHT']
LOOKING_RIGHT = DEFAULTS['LOOKING_RIGHT']
MOVING = DEFAULTS['MOVING']
IS_MOVING_NOW = DEFAULTS['IS_MOVING_NOW']
HALLWAY_X = DEFAULTS['HALLWAY_X']
last_mover = DEFAULTS['last_mover']
HEARTRATE = DEFAULTS['HEARTRATE']
HIGHSCORE = DEFAULTS['HIGHSCORE']
debugmode = DEFAULTS['debugmode']
in_room = DEFAULTS['in_room']
current_mode = DEFAULTS['current_mode']
room_reset = DEFAULTS['room_reset']
current_room = DEFAULTS['current_room']
interactive_spot = DEFAULTS['interactive_spot']
opened_object = DEFAULTS['opened_object']
start_menu = DEFAULTS['start_menu']
e_knop_on_screen = DEFAULTS['e_knop_on_screen']
solving = DEFAULTS['solving']
keys_collected = DEFAULTS['keys_collected']
code_ingevoerd = DEFAULTS['code_ingevoerd']
code_correct = DEFAULTS['code_correct']
animating_safe = DEFAULTS['animating_safe']
mouse_was_pressed = DEFAULTS['mouse_was_pressed']
keys_were_pressed = DEFAULTS['keys_were_pressed']
scare_active = DEFAULTS['scare_active']
scare_countdown = DEFAULTS['scare_countdown']
gereedschap_got = DEFAULTS['gereedschap_got']
scare = DEFAULTS['scare']
heartrate_scare = DEFAULTS['heartrate_scare']
HALLWAY_DOOR_X = DEFAULTS['HALLWAY_DOOR_X']
won = DEFAULTS['won']
code = generate_code()

scare_timer = 0.0
victory_timer = 0.0
is_loading = False
loading_timer = 0.0
target_load_time = 0.0
display_progress = 0.0
victory_screen_active = False

def reset_game_state(new_code=True):
    global WIDTH, HEIGHT, LOOKING_RIGHT, MOVING, IS_MOVING_NOW, HALLWAY_X
    global last_mover, in_room, current_mode, room_reset, interactive_spot
    global opened_object, e_knop_on_screen, solving, code, code_ingevoerd
    global code_correct, mouse_was_pressed, keys_were_pressed, scare_active
    global scare_countdown, scare, HALLWAY_DOOR_X, gereedschap_got, keys_collected
    global HEARTRATE, HIGHSCORE, debugmode, MONSTER_SPEED, animating_safe, heartrate_scare, won, current_room

    WIDTH = DEFAULTS['WIDTH']
    HEIGHT = DEFAULTS['HEIGHT']
    LOOKING_RIGHT = DEFAULTS['LOOKING_RIGHT']
    MOVING = DEFAULTS['MOVING']
    IS_MOVING_NOW = DEFAULTS['IS_MOVING_NOW']
    HALLWAY_X = DEFAULTS['HALLWAY_X']
    last_mover = DEFAULTS['last_mover']
    HEARTRATE = DEFAULTS['HEARTRATE']
    HIGHSCORE = DEFAULTS['HIGHSCORE']
    in_room = DEFAULTS['in_room']
    current_mode = DEFAULTS['current_mode']
    room_reset = DEFAULTS['room_reset']
    interactive_spot = DEFAULTS['interactive_spot']
    opened_object = DEFAULTS['opened_object']
    e_knop_on_screen = DEFAULTS['e_knop_on_screen']
    solving = DEFAULTS['solving']
    keys_collected = DEFAULTS['keys_collected'].copy()
    code_ingevoerd = DEFAULTS['code_ingevoerd'].copy()
    code_correct = DEFAULTS['code_correct']
    mouse_was_pressed = DEFAULTS['mouse_was_pressed']
    keys_were_pressed = DEFAULTS['keys_were_pressed'].copy()
    scare_active = DEFAULTS['scare_active']
    scare_countdown = DEFAULTS['scare_countdown']
    gereedschap_got = DEFAULTS['gereedschap_got']
    scare = DEFAULTS['scare']
    heartrate_scare = DEFAULTS['heartrate_scare']
    HALLWAY_DOOR_X = DEFAULTS['HALLWAY_DOOR_X']
    won = DEFAULTS['won']
    
    if new_code:
        code = generate_code()
