import pygame
import room_3_file
import settings
import random
import monster
import game

hartratemeter = pygame.image.load("assets/images/Rooms/hartslagmeter/scherm.png").convert_alpha()
hartratemeter = pygame.transform.scale(hartratemeter, (450, 400))

indicator = pygame.image.load("assets/images/Rooms/hartslagmeter/pijltje.png").convert_alpha()
indicator = pygame.transform.scale(indicator, (30, 30))

sleutel = pygame.image.load("assets/images/Rooms/sleutel_3.png").convert_alpha()
sleutel = pygame.transform.scale(sleutel, (300, 200))

heartbeat_sound = pygame.mixer.Sound("assets\sounds\heartbeat.mp3")

def reset_heartrate():
    global indicator_x, speed_change_cooldown, indicator_speed, border_collision, sleutel_shown, sleutel_cooldown, solved, heartbeat_timer, heartbeat_interval
    indicator_x = 322
    speed_change_cooldown = 0
    indicator_speed = 0
    border_collision = False
    sleutel_shown = False
    sleutel_cooldown = 0.0
    solved = False
    heartbeat_timer = 0
    heartbeat_interval = 1.0

solved = False
reset_heartrate()

def meten(screen, dt):
    global indicator_x, speed_change_cooldown, indicator_speed, border_collision, sleutel_shown, sleutel_cooldown, solved, heartbeat_timer, heartbeat_interval
    
    if not sleutel_shown:
        screen.blit(hartratemeter, (75, 100))
        screen.blit(indicator, (indicator_x, 330))

        keys = pygame.key.get_pressed()
        size = 45
        font_normal = pygame.font.Font("assets/fonts/Heartless.ttf", 36)
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
            settings.HEARTRATE -= 0.1
            safe = font.render("Safe!", True, (0, 255, 0))
            screen.blit(safe, (190, 170))
        else:
            settings.HEARTRATE += 0.1
           
        heartbeat_timer -= dt
        if heartbeat_timer <= 0:
            heartbeat_sound.play()
            min_interval = 0.1
            max_interval = 0.5
            clamped_heartrate = max(100, min(200, settings.HEARTRATE))
            heartbeat_interval = max_interval - (clamped_heartrate - 100) * (max_interval - min_interval) / 100
            heartbeat_timer = heartbeat_interval   
            
        size = 30
        font = pygame.font.SysFont(None, size)
        text = font.render(f"{int(settings.HEARTRATE)} bpm", True, (255, 255, 0))
        screen.blit(text, (330, 170))

        if settings.HEARTRATE >= 200:
            settings.heartrate_scare = True
            monster.scare = random.choice(monster.jumpscare_images)
            settings.in_room = False
            settings.WIDTH = 800
            settings.HEIGHT = 400
            screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

        elif settings.HEARTRATE <= 100:
            sleutel_shown = True
            solved = True
            sleutel_cooldown = 3.0
            if room_3_file in game.rooms:
                game.rooms.remove(room_3_file)

    elif sleutel_shown:
        screen.blit(sleutel, (150, 150))
        sleutel_cooldown -= dt
        settings.keys_collected[2] = True
        
        if sleutel_cooldown <= 0:
            settings.opened_object = None
            settings.e_knop_on_screen = ""
            settings.solving = False

    

    







    

    
