import heartrate
import pygame
import random
import settings


room_3_picture = pygame.image.load("assets/images/Rooms/room_3.png").convert()
room_3_picture = pygame.transform.scale(room_3_picture, (600, 500))

e_knop = pygame.image.load("assets/images/e_knop.png").convert_alpha()
e_knop = pygame.transform.scale(e_knop, (50, 50))

Heartrate = None

def draw_room(screen, dt):
    global Heartrate
    screen.blit(room_3_picture, (0, 0))

    keys = pygame.key.get_pressed()

    if settings.room_reset:
        settings.interactive_spot = random.choice(["doos","rolstoel"])
    if not settings.solving and not heartrate.solved:
        if settings.e_knop_on_screen == "bed":
            screen.blit(e_knop, (375, 325))
            if keys[settings.E_PRESS]:
                settings.solving = True
                Heartrate = True
                settings.opened_object = "bed"
                settings.e_knop_on_screen = ""
        elif settings.e_knop_on_screen == "doos":
            screen.blit(e_knop, (390, 100))
            if keys[settings.E_PRESS]:
                if settings.interactive_spot == "doos":
                    settings.solving = True
                    Heartrate = False
                    settings.opened_object = "doos"
                    settings.e_knop_on_screen = ""
                else:
                    settings.scare_active = True
                    Heartrate = False
                    settings.scare_countdown = 2.0
        elif settings.e_knop_on_screen == "rolstoel":
            screen.blit(e_knop, (190, 120))
            if keys[settings.E_PRESS]:
                if settings.interactive_spot == "rolstoel":
                    settings.solving = True
                    Heartrate = False
                    settings.opened_object = "rolstoel"
                    settings.e_knop_on_screen = ""
                else:
                    settings.scare_active = True
                    Heartrate = False
                    settings.scare_countdown = 2.0
        elif settings.e_knop_on_screen == "door":
            screen.blit(e_knop, (215, 380))
            if keys[settings.E_PRESS]:
                    settings.in_room = False
                    settings.room_reset = True
                    settings.e_knop_on_screen = ""
                    settings.opened_object = None

    elif heartrate.solved:
        if settings.e_knop_on_screen == "door":
            screen.blit(e_knop, (215, 380))
            if keys[settings.E_PRESS]:
                    settings.in_room = False
                    settings.room_reset = True
                    settings.e_knop_on_screen = ""
                    settings.opened_object = None
    
        if settings.scare_active:
            settings.scare_countdown -= dt
            if settings.scare_countdown <= 0:
                settings.scare_active = False
                settings.scare_countdown = 2.0

    else:
        if keys[settings.K_ESCAPE]:
            settings.solving = False
            settings.e_knop_on_screen = ""
            settings.opened_object = None
        elif any(keys[key] for key in [settings.LEFT_MOVEMENT, settings.RIGHT_MOVEMENT, settings.UP_MOVEMENT, settings.DOWN_MOVEMENT]) and not Heartrate:
            settings.solving = False
            settings.e_knop_on_screen = ""
            settings.opened_object = None
    