import pygame
import random


hallway = []
hallway_normal_v1 = pygame.image.load("assets/images/Hallway/Standard_Hallway_V1.png")
hallway_normal_v2 = pygame.image.load("assets/images/Hallway/Standard_Hallway_V2.jpeg")
hallway_door = pygame.image.load("assets/images/Hallway/Door_Hallway.jpeg")
hallway_bloed_v1 = pygame.image.load("assets/images/Hallway/Blood_Hallway_V1.jpeg")
hallway_bloed_v2 = pygame.image.load("assets/images/Hallway/Blood_Hallway_V2.jpeg")
hallway_bloed_v3 = pygame.image.load("assets/images/Hallway/Blood_Hallway_V3.jpeg")

hallway_normal_v1 = pygame.transform.scale(hallway_normal_v1, (600, 400))
hallway_normal_v2 = pygame.transform.scale(hallway_normal_v2, (600, 400))
hallway_door = pygame.transform.scale(hallway_door, (600, 400))
hallway_bloed_v1 = pygame.transform.scale(hallway_bloed_v1, (600, 400))
hallway_bloed_v2 = pygame.transform.scale(hallway_bloed_v2, (600, 400))
hallway_bloed_v3 = pygame.transform.scale(hallway_bloed_v3, (600, 400))



hallway.extend([hallway_normal_v1] * 5)
hallway_x = 0



def moving(screen, x):
    global hallway_x

    if x > 0:
        hallway_x -= 3
    elif x < 0:
        hallway_x += 3
    
    x_offset = hallway_x
        
    for hall in hallway:
        screen.blit(hall, (x_offset, 0))
        x_offset += hall.get_width()

    if hallway_x % 600 == 0:
        hallway.append(
            random.choices(
                [
                    hallway_normal_v2,  # 10
                    hallway_door,       # 1
                    hallway_bloed_v1,   # 1
                    hallway_bloed_v2,   # 1
                    hallway_bloed_v3    # 1
                ],
                weights=[10, 1, 1, 1, 1],  # gewichten
                k=1
            )[0]
        )
    

    
    
    