import pygame
import settings
import random
import jumpscare
import Kluis_ani as animatie

room_1 = pygame.image.load("assets/images/Rooms/Room_1.png").convert()
room_1_picture = pygame.transform.scale(room_1, (600, 500))

e_knop = pygame.image.load("assets/images/e_knop.png").convert_alpha()
e_knop = pygame.transform.scale(e_knop, (50, 50))



def draw_room(screen):
    global scare_active, scare_countdown
    
    if settings.room_reset:
        settings.interactive_spot = random.choice(["bed", "doos"])
        
    keys = pygame.key.get_pressed()
    screen.fill((0, 0, 0))  # Fill with black
    screen.blit(room_1_picture, (0, 0))  # Center the room

    if not settings.solving:
        if settings.e_knop_on_screen == "bed":
            screen.blit(e_knop, (190, 160))           
            if settings.interactive_spot == "bed" and keys[settings.E_PRESS]:
                settings.solving = True
                settings.opened_object = "bed"
                settings.e_knop_on_screen = ""
            elif settings.interactive_spot != "bed" and keys[settings.E_PRESS]:
                settings.scare_active = True
                settings.scare_countdown = 120

        elif settings.e_knop_on_screen == "kluis":
            screen.blit(e_knop, (500, 320))
            if keys[settings.E_PRESS] and not settings.code_correct:
                settings.solving = True
                settings.opened_object = "kluis"
                settings.e_knop_on_screen = ""

        elif settings.e_knop_on_screen == "doos":
            screen.blit(e_knop, (390, 100))          
            if settings.interactive_spot == "doos" and keys[settings.E_PRESS]:
                settings.solving = True
                settings.opened_object = "doos"
                settings.e_knop_on_screen = ""
            elif settings.interactive_spot != "doos" and keys[settings.E_PRESS]:
                settings.scare_active = True
                settings.scare_countdown = 120
        
        elif settings.e_knop_on_screen == "door":
            screen.blit(e_knop, (350, 380))
            if keys[settings.E_PRESS]:
                settings.in_room = False
                settings.room_reset = True
                settings.e_knop_on_screen = ""
                settings.opened_object = None

        if settings.scare_active:
            settings.scare_countdown -= 1  
            if settings.scare_countdown <= 0:
                settings.scare_active = False
                settings.scare_countdown = 120

    else:
        if keys[settings.K_ESCAPE] or any(
            keys[key] for key in [settings.LEFT_MOVEMENT, settings.RIGHT_MOVEMENT, settings.UP_MOVEMENT, settings.DOWN_MOVEMENT]):
            settings.solving = False
            settings.e_knop_on_screen = ""
            settings.opened_object = None

    if settings.animating_safe:
        animatie.kluis_openen(screen)
        