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

SPEED = 3
FPS = 60

last_mover = "up"

MONSTER_SPEED = 0.5


debugmode = True

in_room = False
current_mode = "begin"
room_reset = True

interactive_spot = None
opened_object = None

e_knop_on_screen = ""
solving = False

code = []
for i in range (4):
    code.append(random.randint(0, 9))

code_ingevoerd = []
code_correct = False

mouse_was_pressed = False
keys_were_pressed = set()

scare_active = False
scare_countdown = 120