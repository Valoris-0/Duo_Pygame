import pygame
import settings


def check(x, y, width, height, screen):

    #voor buiten scherm
    if x < 0 or x + width > settings.WIDTH:
        return False
    if y < 20 or y + height > settings.HEIGHT:
        return False
    if x > 360: 
        return False
    if y > 350:
        return False
    
    #voor bed:
    if x > 75 and x < 170 and y < 190:
        settings.e_knop_on_screen = "bed"
        return False
    
    #voor kluis:
    if x >350 and y > 190 and y < 290:
        settings.e_knop_on_screen = "kluis"
        return False
    
    #voor doos:
    if x >280 and x < 350 and y > 0 and y < 85:
        settings.e_knop_on_screen = "doos"
        return False

    settings.e_knop_on_screen = ""
    return True

