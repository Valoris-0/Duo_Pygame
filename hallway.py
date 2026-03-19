import monster
import pygame
import random
import settings

hallway = []
hallway_normal_v1 = pygame.image.load("assets/images/Hallway/Hallway_test.png").convert()
hallway_normal_v2 = pygame.image.load("assets/images/Hallway/Standard_Hallway_V2.jpeg").convert()
hallway_door = pygame.image.load("assets/images/Hallway/Door_Hallway.jpeg").convert()
hallway_bloed_v1 = pygame.image.load("assets/images/Hallway/Blood_Hallway_V1.jpeg").convert()
hallway_bloed_v2 = pygame.image.load("assets/images/Hallway/Blood_Hallway_V2.jpeg").convert()
hallway_bloed_v3 = pygame.image.load("assets/images/Hallway/Blood_Hallway_V3.jpeg").convert()
Exit_hallway = pygame.image.load("assets/images/Hallway/Exit_Hallway.png").convert()

hallway_normal_v1 = pygame.transform.scale(hallway_normal_v1, (800, 400))
hallway_normal_v2 = pygame.transform.scale(hallway_normal_v2, (800, 400))
hallway_door = pygame.transform.scale(hallway_door, (800, 400))
hallway_bloed_v1 = pygame.transform.scale(hallway_bloed_v1, (800, 400))
hallway_bloed_v2 = pygame.transform.scale(hallway_bloed_v2, (800, 400))
hallway_bloed_v3 = pygame.transform.scale(hallway_bloed_v3, (800, 400))
Exit_hallway = pygame.transform.scale(Exit_hallway, (800, 400))

e_knop = pygame.image.load("assets/images/e_knop.png").convert_alpha()
e_knop = pygame.transform.scale(e_knop, (50, 50))

hallway.extend([hallway_normal_v1] * 1)

def reset_hallway():
    global hallway, e_knop_on_screen

    hallway = [hallway_normal_v1]
    e_knop_on_screen = None
    settings.e_knop_on_screen = ""

reset_hallway()

def moving(screen, x, player_x):
    global e_knop_on_screen

    settings.HALLWAY_X -= x
    items_to_remove = 0

    x_offset = settings.HALLWAY_X
    e_knop_on_screen = None
    settings.e_knop_on_screen = ""
        
    for hall in hallway:
        if x_offset + hall.get_width() > 0 and x_offset < settings.WIDTH:
            screen.blit(hall, (x_offset, 0))
        
        if hall is hallway_door:
            btn_x = x_offset + 375
            btn_y = 150
            e_knop_on_screen = btn_x

            if 0 <= btn_x <= settings.WIDTH and abs(player_x - btn_x) <= 50:
                screen.blit(e_knop, (btn_x, btn_y))
                settings.e_knop_on_screen = "door"
                settings.HALLWAY_DOOR_X = btn_x

        elif hall is Exit_hallway:
            btn_x = x_offset + 375
            btn_y = 150
            e_knop_on_screen = btn_x

            if 0 <= btn_x <= settings.WIDTH and abs(player_x - btn_x) <= 50:
                screen.blit(e_knop, (btn_x, btn_y))
                settings.e_knop_on_screen = "exit"
                settings.HALLWAY_DOOR_X = btn_x

        if x_offset + hall.get_width() < monster.monster_x:
            items_to_remove += 1

        x_offset += hall.get_width()

    for i in range(items_to_remove):
        verwijderde_hall = hallway.pop(0)
        settings.HALLWAY_X += verwijderde_hall.get_width()
        print(len(hallway))

    hallway_end = settings.HALLWAY_X + len(hallway) * hallway_normal_v1.get_width()
    if hallway_end <= settings.WIDTH:
        # Basis lijst met hallway segmenten
        hallway_options = [
            hallway_normal_v2,  # 5
            hallway_door,       # 1
            hallway_bloed_v1,   # 1
            hallway_bloed_v2,   # 1
            hallway_bloed_v3    # 1
        ]
        hallway_weights = [5, 1, 1, 1, 1]
        
        # Als alle sleutels zijn verzameld, voeg Exit_hallway toe aan de opties
        if all(settings.keys_collected):
            hallway_options.append(Exit_hallway)
            hallway_weights.append(1)  # Kleine kans op uitgang
        
        hallway.append(
            random.choices(
                hallway_options,
                weights=hallway_weights,
                k=1
            )[0]
        )
    

    
    
    