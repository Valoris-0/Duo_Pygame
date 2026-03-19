import pygame
import settings
import random
import electrisiteitskast

room_2_picture = pygame.image.load("assets/images/Rooms/Room_2.png").convert()
room_2_picture = pygame.transform.scale(room_2_picture, (600, 500))

e_knop = pygame.image.load("assets/images/e_knop.png")
e_knop = pygame.transform.scale(e_knop, (50, 50))


def draw_room(screen):
    screen.blit(room_2_picture, (0, 0))
    
    keys = pygame.key.get_pressed()
    
    if settings.room_reset:
        settings.interactive_spot = random.choice(["bed", "doos"])

    if not settings.solving:
        if settings.e_knop_on_screen == "door":
                screen.blit(e_knop, (350, 380))
                if keys[settings.E_PRESS]:
                    settings.in_room = False
                    settings.room_reset = True
                    settings.e_knop_on_screen = ""
                    settings.opened_object = None

        elif settings.e_knop_on_screen == "bed":
                screen.blit(e_knop, (425, 325))
                if keys[settings.E_PRESS]:
                    if settings.interactive_spot == "bed":
                        settings.solving = True
                        settings.opened_object = "bed"
                        settings.e_knop_on_screen = ""
                    else:
                        settings.scare_active = True
                        settings.scare_countdown = 120
        
        elif settings.e_knop_on_screen == "doos":
                screen.blit(e_knop, (110, 225))
                if keys[settings.E_PRESS]:
                    if settings.interactive_spot == "doos":
                        settings.solving = True
                        settings.opened_object = "doos"
                        settings.e_knop_on_screen = ""
                    else:
                        settings.scare_active = True
                        settings.scare_countdown = 120

        elif settings.e_knop_on_screen == "electrisiteitskast":
                screen.blit(e_knop, (270, 100))
                if keys[settings.E_PRESS]:
                    if settings.gereedschap_got:
                        settings.solving = True
                        settings.opened_object = "electrisiteitskast"
                        settings.e_knop_on_screen = ""
                    else:
                        settings.scare_active = True
                        settings.scare_countdown = 120
                    
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
