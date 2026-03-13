import pygame
import settings


def check(x, y, room_number):

    if room_number == "room_1_file":
        if x < 120:
            return False
        if y < 50:
            return False
        if x > 460:
            return False

        if 280 < x < 320:
            if y > 340:
                settings.e_knop_on_screen = "door"
                return False
        else:
            if y > 320:
                return False

        # voor bed:
        if x > 155 and x < 250 and y < 190:
            settings.e_knop_on_screen = "bed"
            return False

        # voor kluis:
        if x > 450 and y > 190 and y < 290:
            settings.e_knop_on_screen = "kluis"
            return False

        # voor doos:
        if x > 380 and x < 450 and y > 0 and y < 85:
            settings.e_knop_on_screen = "doos"
            return False

        settings.e_knop_on_screen = ""
        return True

    
    if room_number == "room_2_file":
        if x < 35:
            return False
        if y < 40:
            return False
        if x > 380:
            return False
        if 180 < x <230:
            if y > 330:
                settings.e_knop_on_screen = "door"
                return False
        else:
            if y > 320:
                return False
        
        #voor bed
        if x > 300 and y > 150:
            settings.e_knop_on_screen = "bed"
            return False
        
        #voor doos
        if x < 85 and 110 < y < 200:
            settings.e_knop_on_screen = "doos"
            return False
        
        #voor electrisiteitskast
        if 160 < x < 230 and y < 90: 
            settings.e_knop_on_screen = "electrisiteitskast"
            return False


    

        settings.e_knop_on_screen = ""
        return True


    if room_number == "room_3_file":
        # nog maken voor room 3
        settings.e_knop_on_screen = ""
        return True

    # Default: allow movement in unknown rooms
    settings.e_knop_on_screen = ""
    return True

