import pygame
import random

WIDTH = 800
HEIGHT = 400
TITLE = "HORROR"

PLAYER_WIDTH = 80
PLAYER_HEIGHT = 144

LOOKING_RIGHT = True
MOVING = False
IS_MOVING_NOW = False

HALLWAY_X = 0

LEFT_MOVEMENT = pygame.K_LEFT
RIGHT_MOVEMENT = pygame.K_RIGHT
UP_MOVEMENT = pygame.K_UP
DOWN_MOVEMENT = pygame.K_DOWN
E_PRESS = pygame.K_e
K_ESCAPE = pygame.K_ESCAPE

FPS = 120
SPEED = 350

last_mover = "up"

MONSTER_SPEED = 60

debugmode = False

in_room = False
current_mode = "begin"
room_reset = True
current_room = 0

interactive_spot = None
opened_object = None

e_knop_on_screen = ""
solving = False

code = []
for i in range (4):
    code.append(random.randint(0, 9))

code_ingevoerd = []
code_correct = False

animating_safe = False

mouse_was_pressed = False
keys_were_pressed = set()

scare_active = False
scare_countdown = 2.0
gereedschap_got = False

scare = False

HALLWAY_DOOR_X = 375


def generate_code():
    return [random.randint(0, 9) for _ in range(4)]


def reset_game_state(new_code=True):
    global game_over
    global WIDTH, HEIGHT, LOOKING_RIGHT, MOVING, IS_MOVING_NOW, HALLWAY_X
    global last_mover, in_room, current_mode, room_reset, interactive_spot
    global opened_object, e_knop_on_screen, solving, code, code_ingevoerd
    global code_correct, mouse_was_pressed, keys_were_pressed, scare_active
    global scare_countdown, scare, HALLWAY_DOOR_X, gereedschap_got

    game_over = False

    WIDTH = 800
    HEIGHT = 400

    LOOKING_RIGHT = True
    MOVING = False
    IS_MOVING_NOW = False
    HALLWAY_X = 0
    last_mover = "up"

    in_room = False
    current_mode = "begin"
    room_reset = True

    interactive_spot = None
    opened_object = None
    e_knop_on_screen = ""
    solving = False

    if new_code:
        code = generate_code()
    code_ingevoerd = []
    code_correct = False

    mouse_was_pressed = False
    keys_were_pressed = set()

    scare_active = False
    scare_countdown = 2.0
    gereedschap_got = False
    scare = False

    HALLWAY_DOOR_X = 375
