import pygame
import settings


def check(x, y, width, height, screen):

    #voor buiten scherm
    if x < 120: 
        return False
    if y < 50: 
        return False
    if x > 460: 
        return False
    # door area has taller threshold; only block when in the doorway
    if 280 < x < 320:
        if y > 340:
            settings.e_knop_on_screen = "door"
            return False
    else:
        if y > 320:
            return False
    
    #voor bed:
    if x > 155 and x < 250 and y < 190:
        settings.e_knop_on_screen = "bed"
        return False
    
    #voor kluis:
    if x > 450 and y > 190 and y < 290:
        settings.e_knop_on_screen = "kluis"
        return False
    
    #voor doos:
    if x >380 and x < 450 and y > 0 and y < 85:
        settings.e_knop_on_screen = "doos"
        return False
    

    

    settings.e_knop_on_screen = ""
    return True

