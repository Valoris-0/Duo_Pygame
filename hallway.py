import monster
import pygame
import random
import settings

hallway = []

def load_and_scale(path, size, use_alpha=False):
    image = pygame.image.load(path)
    if use_alpha:
        image = image.convert_alpha()
    else:
        image = image.convert()

    return pygame.transform.scale(image, size)

hall_size = (800, 400)

hallway_normal_v1 = load_and_scale("assets/images/Hallway/Hallway_test.png", hall_size)
hallway_normal_v2 = load_and_scale("assets/images/Hallway/Standard_Hallway_V2.jpeg", hall_size)
hallway_door      = load_and_scale("assets/images/Hallway/Door_Hallway.jpeg", hall_size)
hallway_bloed_v1  = load_and_scale("assets/images/Hallway/Blood_Hallway_V1.jpeg", hall_size)
hallway_bloed_v2  = load_and_scale("assets/images/Hallway/Blood_Hallway_V2.jpeg", hall_size)
hallway_bloed_v3  = load_and_scale("assets/images/Hallway/Blood_Hallway_V3.jpeg", hall_size)
Exit_hallway      = load_and_scale("assets/images/Hallway/Exit_Hallway.png", hall_size)

e_knop = load_and_scale("assets/images/e_knop.png", (50, 50), use_alpha=True)

hallway.extend([hallway_normal_v1] * 3)

def reset_hallway():
    global hallway, e_knop_on_screen, door

    hallway = [hallway_normal_v1]
    e_knop_on_screen = None
    settings.e_knop_on_screen = ""
    door = 5

reset_hallway()

def moving(screen, x, player_x):
    global e_knop_on_screen, door

    settings.HALLWAY_X -= x
    items_to_remove = 0

    x_offset = settings.HALLWAY_X
    e_knop_on_screen = None
    settings.e_knop_on_screen = ""
        
    for i, hall in enumerate(hallway):
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
        if len(hallway) > 0:
            verwijderde_hall = hallway.pop(0)
            settings.HALLWAY_X += verwijderde_hall.get_width()

    hallway_end = settings.HALLWAY_X + len(hallway) * hallway_normal_v1.get_width()
    if hallway_end <= settings.WIDTH:
        hallway_options = [
            hallway_normal_v2,  # 12
            hallway_door,       # 5
            hallway_bloed_v1,   # 3
            hallway_bloed_v2,   # 3
            hallway_bloed_v3    # 3
        ]
        hallway_weights = [12, door, 3, 3, 3]
        
        if all(settings.keys_collected):
            door = 0
            hallway_weights[1] = 0
            
            hallway_options.append(Exit_hallway)
            hallway_weights.append(5)
        
        hallway.append(
            random.choices(
                hallway_options,
                weights=hallway_weights,
                k=1
            )[0]
        )




