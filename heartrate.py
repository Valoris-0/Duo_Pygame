import pygame
import settings
import random

hartratemeter = pygame.image.load("assets/images/Rooms/hartslagmeter/scherm.png").convert_alpha()
hartratemeter = pygame.transform.scale(hartratemeter, (450, 400))

indicator = pygame.image.load("assets/images/Rooms/hartslagmeter/pijltje.png").convert_alpha()
indicator = pygame.transform.scale(indicator, (30, 30))

sleutel = pygame.image.load("assets/images/Rooms/sleutel_3.png").convert_alpha()
sleutel = pygame.transform.scale(sleutel, (600, 500))

def reset_heartrate():
    global indicator_x, speed_change_cooldown, indicator_speed, border_collision, heartrate, sleutel_shown, sleutel_cooldown
    indicator_x = 322
    speed_change_cooldown = 0
    indicator_speed = 0
    border_collision = False
    heartrate = 150
    sleutel_shown = False
    sleutel_cooldown = 0.0

reset_heartrate()

def meten(screen, dt):
    global indicator_x, speed_change_cooldown, indicator_speed, border_collision, heartrate, sleutel_shown, sleutel_cooldown
    
    if not sleutel_shown:
        screen.blit(hartratemeter, (75, 100))
        screen.blit(indicator, (indicator_x, 330))

        keys = pygame.key.get_pressed()
        size = 45
        font = pygame.font.SysFont(None, size)

        indicator_x += indicator_speed

        speed_change_cooldown -= 1
        if speed_change_cooldown <= 0:
            speed_change_cooldown = 60
            indicator_speed = random.randint(-3, 3)
            while indicator_speed == 0:
                indicator_speed = random.randint(-3, 3)

        if indicator_x > 385:
            indicator_x = 385
        
        elif indicator_x < 185:
            indicator_x = 185

        if keys[settings.LEFT_MOVEMENT]:
            indicator_x -= 5
        if keys[settings.RIGHT_MOVEMENT]:
            indicator_x += 5

        if 322 > indicator_x > 245:
            heartrate -= 0.1
            safe = font.render("Safe!", True, (0, 255, 0))
            screen.blit(safe, (190, 170))
        else:
            heartrate += 0.1
        size = 30
        font = pygame.font.SysFont(None, size)
        text = font.render(f"{int(heartrate)} bpm", True, (255, 255, 0))
        screen.blit(text, (330, 170))

        if heartrate >= 200:
            death_text = font.render("You died!", True, (255, 0, 0))
            screen.blit(death_text, (200, 220))
            settings.game_over = True
            settings.solved = False
            settings.opened_object = None
            settings.e_knop_on_screen = ""
            settings.solving = False
            #hier moet je dood gaan

        elif heartrate <= 100:
            sleutel_shown = True
            # 180 frames at 60 FPS = 3 seconds.
            sleutel_cooldown = 3.0

    elif sleutel_shown:
        screen.blit(sleutel, (0, 0))
        sleutel_cooldown -= dt
        
        if sleutel_cooldown <= 0:
            settings.solved = True
            settings.opened_object = None
            settings.e_knop_on_screen = ""
            settings.solving = False

    

    







    

    
