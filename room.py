import pygame
import settings
import kluis
import random

room_1 = pygame.image.load("assets/images/Rooms/Room_1.png")

room_1 = pygame.transform.scale(room_1, (600, 500))

e_knop = pygame.image.load("assets/images/e_knop.png")
e_knop = pygame.transform.scale(e_knop, (50, 50))

print(settings.code)

def draw_room(screen):
    
    if settings.room_reset:
        settings.interactive_spot = random.choice(["bed", "doos"])
        print(f"interactive spot this visit: {settings.interactive_spot}")

    keys = pygame.key.get_pressed()
    screen.blit(room_1, (0, 0))

    if not settings.solving:
        if settings.e_knop_on_screen == "bed":
            screen.blit(e_knop, (200, 160))
            
            if settings.interactive_spot == "bed" and keys[settings.E_PRESS]:
                settings.solving = True
                settings.opened_object = "bed"
                settings.e_knop_on_screen = ""

        elif settings.e_knop_on_screen == "kluis":
            screen.blit(e_knop, (450, 240))
            if keys[settings.E_PRESS]:
                settings.solving = True
                settings.opened_object = "kluis"
                settings.e_knop_on_screen = ""

        elif settings.e_knop_on_screen == "doos":
            screen.blit(e_knop, (360, 40))
            # only respond if doos was chosen
            if settings.interactive_spot == "doos" and keys[settings.E_PRESS]:
                settings.solving = True
                settings.opened_object = "doos"
                settings.e_knop_on_screen = ""

    else:
        # when solving, allow the user to exit with escape, clear prompt plus opened_object
        if keys[settings.K_ESCAPE]:
            settings.solving = False
            settings.e_knop_on_screen = ""
            settings.opened_object = None
            