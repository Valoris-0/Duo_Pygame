import pygame
import random
from player import Player

hallway = []
hallway_normal_v1 = pygame.image.load("assets/images/Hallway/Standard_Hallway_V1.png")
hallway_normal_v2 = pygame.image.load("assets/images/Hallway/Standard_Hallway_V2.jpeg")
hallway_door = pygame.image.load("assets/images/Hallway/Door_Hallway.jpeg")
hallway_bloed_v1 = pygame.image.load("assets/images/Hallway/Blood_Hallway_V1.jpeg")
hallway_bloed_v2 = pygame.image.load("assets/images/Hallway/Blood_Hallway_V2.jpeg")
hallway_bloed_v3 = pygame.image.load("assets/images/Hallway/Blood_Hallway_V3.jpeg")

hallway.extend([hallway_normal_v1] * 10)


def moving():
    print(Player.x)