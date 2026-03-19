import pygame
import settings


def get_interaction_at_position(x, y):
    room_number = getattr(settings, "current_room_module_name", "room_1_file")

    if room_number == "room_1_file":
        if 240 < x < 290 and y >= 320:
            return "door"

        if 110 < x < 235 and 0 < y < 200:
            return "bed"

        if x >= 405 and 200 <= y < 400:
            return "kluis"

        if 330 < x < 420 and 0 <= y <= 115:
            return "doos"
        
    elif room_number == "room_2_file":
        if 230 < x < 285 and y >= 320:
            return "door"
        
        if x >= 360 and y >= 150:
            return "bed"
        
        if x <= 115 and 110 <= y <= 210:
            return "doos"
        
        if 210 < x < 300 and y <= 100:
            return "electrisiteitskast"
        

    elif room_number == "room_3_file":
        if 110 < x < 235 and y < 135: 
            return "rolstoel"
        
        if 385 > x > 280 and y > 195: 
            return "bed"
        
        if x > 360 and 205 > y > 120:
            return "machine"
        
        if 340 < x < 420 and y < 95:
            return "doos"
        
        if 240 < x < 290 and y >= 325:
            return "door"

    return ""


def update_interaction_prompt(x, y):
    settings.e_knop_on_screen = get_interaction_at_position(x, y)

def check(x, y):
    room_number = getattr(settings, "current_room_module_name", "room_1_file")

    if room_number == "room_1_file":
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

    elif room_number == "room_2_file":
        if x < 90:
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
        
        if x > 360 and y > 160: #bed
            return False
        if x < 150 and 120 < y < 200: #doos
            return False
        if 225 < x < 290 and y < 90: #electrischiteits kast
            return False

    elif room_number == "room_3_file":
        if x < 85: 
            return False
        if y < 40: 
            return False
        if x > 440: 
            return False
        if 240 < x < 290:
            if y > 340:
                return False
        else:
            if y > 325:
                return False
        
        if 120 < x < 225 and y < 125: #rolstoel
            return False
        
        if 350 < x < 410 and y < 85: #doos
            return False
        
        if 385 > x > 290 and y > 205: #bed
            return False
        
        if x > 380 and y > 130: #machine dingie
            return False



    return True

