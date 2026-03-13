import pygame
import settings


room_2_picture = pygame.image.load("assets/images/Rooms/Room_2.png")
room_2_picture = pygame.transform.scale(room_2_picture, (600, 500))

e_knop = pygame.image.load("assets/images/e_knop.png")
e_knop = pygame.transform.scale(e_knop, (50, 50))



def draw_room(screen):
    screen.blit(room_2_picture, (0, 0))
    
    keys = pygame.key.get_pressed()

    if not settings.solving:
        if settings.e_knop_on_screen == "door":
                screen.blit(e_knop, (200, 350))
                if keys[settings.E_PRESS]:
                    settings.in_room = False
                    settings.room_reset = True
                    settings.e_knop_on_screen = ""
                    settings.opened_object = None

        elif settings.e_knop_on_screen == "bed":
                screen.blit(e_knop, (350, 200))
                if keys[settings.E_PRESS]:
                    pass
        
        elif settings.e_knop_on_screen == "doos":
                screen.blit(e_knop, (50, 150))
                if keys[settings.E_PRESS]:
                    pass

        elif settings.e_knop_on_screen == "electrisiteitskast":
                screen.blit(e_knop, (250, 50))
                if keys[settings.E_PRESS]:
                    settings.solving = True
                    settings.opened_object = "electrisiteitskast"
                    settings.e_knop_on_screen = ""
                    
                    
                    


    else:
          if keys[settings.K_ESCAPE]:
            settings.solving = False
            settings.e_knop_on_screen = ""
            settings.opened_object = None
