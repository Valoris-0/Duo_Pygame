import pygame
import random
import settings

hallway = []
hallway_normal_v1 = pygame.image.load("assets/images/Hallway/Hallway_test.png")
hallway_normal_v2 = pygame.image.load("assets/images/Hallway/Standard_Hallway_V2.jpeg")
hallway_door = pygame.image.load("assets/images/Hallway/Door_Hallway.jpeg")
hallway_bloed_v1 = pygame.image.load("assets/images/Hallway/Blood_Hallway_V1.jpeg")
hallway_bloed_v2 = pygame.image.load("assets/images/Hallway/Blood_Hallway_V2.jpeg")
hallway_bloed_v3 = pygame.image.load("assets/images/Hallway/Blood_Hallway_V3.jpeg")

hallway_normal_v1 = pygame.transform.scale(hallway_normal_v1, (800, 400))
hallway_normal_v2 = pygame.transform.scale(hallway_normal_v2, (800, 400))
hallway_door = pygame.transform.scale(hallway_door, (800, 400))
hallway_bloed_v1 = pygame.transform.scale(hallway_bloed_v1, (800, 400))
hallway_bloed_v2 = pygame.transform.scale(hallway_bloed_v2, (800, 400))
hallway_bloed_v3 = pygame.transform.scale(hallway_bloed_v3, (800, 400))

e_knop = pygame.image.load("assets/images/e_knop.png")
e_knop = pygame.transform.scale(e_knop, (50, 50))

hallway.extend([hallway_normal_v1] * 1)

e_knop_on_screen = None

def moving(screen, x, player_x):
    global e_knop_on_screen

    settings.HALLWAY_X -= x

    x_offset = settings.HALLWAY_X
    e_knop_on_screen = None
    settings.e_knop_on_screen = ""
        
    for hall in hallway:
        screen.blit(hall, (x_offset, 0))
        
        if hall is hallway_door:
            btn_x = x_offset + 375
            btn_y = 150
            e_knop_on_screen = btn_x

            if 0 <= btn_x <= settings.WIDTH and abs(player_x - btn_x) <= 50:
                screen.blit(e_knop, (btn_x, btn_y))
                settings.e_knop_on_screen = "door"
                settings.HALLWAY_DOOR_X = btn_x

        x_offset += hall.get_width()

    if settings.HALLWAY_X % 800 == 0:
        hallway.append(
            random.choices(
                [
                    hallway_normal_v2,  # 10
                    hallway_door,       # 1
                    hallway_bloed_v1,   # 1
                    hallway_bloed_v2,   # 1
                    hallway_bloed_v3    # 1
                ],
                weights=[10, 100, 1, 1, 1],  # gewichten
                k=1
            )[0]
        )
    

    
    
    