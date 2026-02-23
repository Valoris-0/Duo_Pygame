import pygame
import random
import settings

#Hallway images
hallway = []
hallway_normal_v1 = pygame.image.load("assets/images/Hallway/Hallway_test.png")
hallway_normal_v2 = pygame.image.load("assets/images/Hallway/Standard_Hallway_V2.jpeg")
hallway_door = pygame.image.load("assets/images/Hallway/Hallway_Door.jpeg")
hallway_bloed_v1 = pygame.image.load("assets/images/Hallway/Blood_Hallway_V1.jpeg")
hallway_bloed_v2 = pygame.image.load("assets/images/Hallway/Blood_Hallway_V2.jpeg")
hallway_bloed_v3 = pygame.image.load("assets/images/Hallway/Blood_Hallway_V3.jpeg")

hallway_normal_v1 = pygame.transform.scale(hallway_normal_v1, (600, 400))
hallway_normal_v2 = pygame.transform.scale(hallway_normal_v2, (600, 400))
hallway_door = pygame.transform.scale(hallway_door, (600, 400))
hallway_bloed_v1 = pygame.transform.scale(hallway_bloed_v1, (600, 400))
hallway_bloed_v2 = pygame.transform.scale(hallway_bloed_v2, (600, 400))
hallway_bloed_v3 = pygame.transform.scale(hallway_bloed_v3, (600, 400))


#Hallway start
hallway.extend([hallway_normal_v1] * 3)


#Background moving def
def moving(screen, x):

    if x > 0:
        settings.HALLWAY_X -= settings.SPEED
    elif x < 0:
        settings.HALLWAY_X += settings.SPEED
    
    x_offset = settings.HALLWAY_X
        
    for hall in hallway:
        screen.blit(hall, (x_offset, 0))
        x_offset += hall.get_width()

    if settings.HALLWAY_X % 600 == 0:
        hallway.append(
            random.choices(
                [
                    hallway_normal_v2,  # 10
                    hallway_normal_v1,  # 5
                    hallway_door,       # 1
                    hallway_bloed_v1,   # 5
                    hallway_bloed_v2,   # 5
                    hallway_bloed_v3    # 5
                ],
                weights=[10, 5, 100, 5, 5, 5],  # gewichten
                k=1
            )[0]
        )
    

    
    
    