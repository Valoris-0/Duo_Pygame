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

hallway.extend([hallway_normal_v1] * 10)
hallway_x = 0

def moving(screen, x):
    global hallway_x
    if x > 0:
        hallway_x -= 5
    elif x < 0:
        hallway_x += 5
    screen.blit(hallway_normal_v1, (hallway_x, 0))
    