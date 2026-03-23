
import game
import pygame
import room_2_file
import settings
import random

elektriciteitskast = pygame.image.load("assets/images/Rooms/elektriciteit/electrisiteits kast.png").convert()
elektriciteitskast = pygame.transform.scale(elektriciteitskast, (300, 300))

test = pygame.image.load("assets/images/Rooms/elektriciteit/test.jpg").convert()
test = pygame.transform.scale(test, (300, 300))

class Cable:
    def __init__(self, name, rgb, y_left_options, image_path):
        self.name = name
        self.rgb = rgb

        img = pygame.image.load(image_path).convert_alpha()
        self.img_left = pygame.transform.scale(img, (300, 300))
        self.img_right = pygame.transform.flip(self.img_left, True, False)

        self.y_left_options = y_left_options
        self.y_left = 0
        self.y_right = 0

        self.rect_left = None
        self.rect_right = None

        self.is_dragging = False
        self.is_connected = False
        self.end_pos = (0, 0)

cables = [
    Cable("blue", (0, 0, 255), [60, 125, 180, 240], "assets/images/Rooms/elektriciteit/blue_kabel.png"),
    Cable("orange", (255, 0, 0), [5, 70, 125, 185], "assets/images/Rooms/elektriciteit/orange_kabel.png"),
    Cable("roze", (255, 20, 147), [-55, 10, 65, 125], "assets/images/Rooms/elektriciteit/roze_kabel.png"),
    Cable("yellow", (255, 165, 0), [125, 190, 245, 305], "assets/images/Rooms/elektriciteit/yellow_kabel.png")
]

cable_sound = pygame.mixer.Sound("assets\sounds\cable_sound.mp3")
sound_playing = False

def reset_elektriciteitskast():
    global key_shown, key_cooldown, solved

    key_shown = False
    key_cooldown = 2.0
    solved = False

    rect_ys = [30, 95, 150, 210]
    ys_left = [0, 1, 2, 3]
    random.shuffle(ys_left)

    for i, cable in enumerate(cables):
        cable.y_left = cable.y_left_options[ys_left[i]]
        cable.rect_left = cable.img_left.get_rect(topleft=(28, rect_ys[ys_left[i]])).inflate(-250, -280)
        cable.is_dragging = False
        cable.is_connected = False
        cable.end_pos = (0, 0)

    ys_right = [0, 1, 2, 3]
    random.shuffle(ys_right)
    for i, cable in enumerate(cables):
        cable.y_right = cable.y_left_options[ys_right[i]]
        cable.rect_right = cable.img_right.get_rect(topleft=(270, rect_ys[ys_right[i]])).inflate(-250, -280)

reset_elektriciteitskast()

def meterkast(screen, mouse_x, mouse_y, dt):
    global key_shown, key_cooldown, solved

    if not key_shown:
        screen.blit(test, (150, 125))
        for cable in cables:
            screen.blit(cable.img_left, (150, cable.y_left))
            screen.blit(cable.img_right, (150, cable.y_right))

    if settings.debugmode:
        for cable in cables:
            pygame.draw.rect(screen, cable.rgb, cable.rect_left, 2)
            pygame.draw.rect(screen, cable.rgb, cable.rect_right, 2)

    mouse_buttons = pygame.mouse.get_pressed()
    mouse_pressed = mouse_buttons[0]

    if mouse_pressed and not settings.mouse_was_pressed:
        for cable in cables:
            if cable.rect_left.collidepoint(mouse_x, mouse_y):
                cable.is_dragging = True
                break
    
    for cable in cables:
        if cable.is_dragging:
            pygame.draw.line(screen, cable.rgb, cable.rect_left.center, (mouse_x, mouse_y), 10)

            if not mouse_pressed and settings.mouse_was_pressed:
                if cable.rect_right.collidepoint(mouse_x, mouse_y):
                    cable.is_connected = True
                    cable.end_pos = (mouse_x, mouse_y)
                cable.is_dragging = False

        if cable.is_connected:
            pygame.draw.line(screen, cable.rgb, cable.rect_left.center, cable.end_pos, 10)

    if all(cable.is_connected for cable in cables) and not key_shown:
        key_shown = True
        settings.solved = True
        key_cooldown = 2.0
        for cable in cables:
            cable.is_connected = False
        settings.keys_collected[1] = True

    if key_shown:
        key_image = pygame.image.load("assets/images/Rooms/sleutel_2.png").convert_alpha()
        key_image = pygame.transform.scale(key_image, (300, 200))
        screen.blit(key_image, (150, 150))
        key_cooldown -= dt
        solved = True

        if room_2_file in game.rooms:
            game.rooms.remove(room_2_file)
        
        if key_cooldown <= 0:
            key_shown = False           
            settings.opened_object = None
            settings.e_knop_on_screen = ""
            settings.solving = False

    settings.mouse_was_pressed = mouse_pressed