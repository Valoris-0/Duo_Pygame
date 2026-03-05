
import pygame


WIDTH = 800
HEIGHT = 400
TITLE = "HORROR"

HALLWAY_X = 0

LEFT_MOVEMENT = pygame.K_LEFT
RIGHT_MOVEMENT = pygame.K_RIGHT
UP_MOVEMENT = pygame.K_UP
DOWN_MOVEMENT = pygame.K_DOWN

SPEED = 3 #in x per second
FPS = 60

last_mover = "up"

MONSTER_SPEED = 0.5


debugmode = False

in_room = True         #voor het verranderen van of je in kamer of hallway bent moet je de in_room en current mode allebei verranderen
current_mode = "begin"