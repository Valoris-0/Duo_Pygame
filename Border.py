import pygame
import settings


def get_interaction_at_position(x, y):
    if 240 < x < 290 and y >= 320:
        return "door"

    if 110 < x < 235 and 0 < y < 200:
        return "bed"

    if x >= 405 and 200 <= y < 400:
        return "kluis"

    if 330 < x < 420 and 0 <= y <= 115:
        return "doos"

    return ""


def update_interaction_prompt(x, y):
    settings.e_knop_on_screen = get_interaction_at_position(x, y)


def check(x, y, width, height, screen):

    #voor buiten scherm
    if x < 100:  
        return False
    if y < 50: 
        return False
    if x > 430: 
        return False
    if 240 < x < 290:
        if y > 340:
            return False
    else:
        if y > 320:
            return False
    
    #voor bed:
    if x > 130 and x < 225 and y < 190:
        return False
    
    #voor kluis:
    if x > 425 and y > 190 and y < 290:
        return False
    
    #voor doos:
    if x > 350 and x < 410 and y > 0 and y < 85:
        return False

    return True

