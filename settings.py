import pygame
import random

WIDTH = 800
HEIGHT = 400
TITLE = "HORROR"

HALLWAY_X = 0

LEFT_MOVEMENT = pygame.K_LEFT
RIGHT_MOVEMENT = pygame.K_RIGHT
UP_MOVEMENT = pygame.K_UP
DOWN_MOVEMENT = pygame.K_DOWN
E_PRESS = pygame.K_e
K_ESCAPE = pygame.K_ESCAPE

SPEED = 3 #in x per second
FPS = 60

last_mover = "up"

MONSTER_SPEED = 0.5


debugmode = True

in_room = True  #voor het verranderen van of je in kamer of hallway bent moet je alleen in_room verrrenderen, current_mode gaat automatisch mee!
current_mode = "begin"
room_reset = True
current_room = 0

interactive_spot = None #bed of doos voor code
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

scare_active = False
scare_countdown = 120
gereedschap_got = True