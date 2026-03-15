import pygame
import settings
import random

electrisiteitskast = pygame.image.load("assets/images/Rooms/elektriciteit/electrisiteits kast.png")
electrisiteitskast = pygame.transform.scale(electrisiteitskast, (300, 300))

test = pygame.image.load("assets/images/Rooms/elektriciteit/test.jpg")
test = pygame.transform.scale(test, (300, 300))

blue_kabel = pygame.image.load("assets/images/Rooms/elektriciteit/blue_kabel.png")
blue_kabel = pygame.transform.scale(blue_kabel, (300, 300))
blue_kabel_right = pygame.transform.flip(blue_kabel, True, False)

orange_kabel = pygame.image.load("assets/images/Rooms/elektriciteit/orange_kabel.png")
orange_kabel = pygame.transform.scale(orange_kabel, (300, 300))
orange_kabel_right = pygame.transform.flip(orange_kabel, True, False)

roze_kabel = pygame.image.load("assets/images/Rooms/elektriciteit/roze_kabel.png")
roze_kabel = pygame.transform.scale(roze_kabel, (300, 300))
roze_kabel_right = pygame.transform.flip(roze_kabel, True, False)

yellow_kabel = pygame.image.load("assets/images/Rooms/elektriciteit/yellow_kabel.png")
yellow_kabel = pygame.transform.scale(yellow_kabel, (300, 300))
yellow_kabel_right = pygame.transform.flip(yellow_kabel, True, False)


dragging_colors = [False, False, False, False] # Blue, Orange, Roze, Yellow
connected_colors = [False, False, False, False] # Blue, Orange, Roze, Yellow
color_end_positions = [(0,0), (0,0), (0,0), (0,0)] # Blue, Orange, Roze, Yellow

key_shown = False
key_cooldown = 120

blue = [60, 125, 180, 240]
orange = [5, 70, 125, 185]
roze = [-55, 10, 65, 125]
yellow = [125, 190, 245, 305]


rect_ys = [30, 95, 150, 210]
ys = [0, 1, 2, 3]

random.shuffle(ys)

blue_y_left = blue[ys[0]]
orange_y_left = orange[ys[1]]
roze_y_left = roze[ys[2]]
yellow_y_left = yellow[ys[3]]

blue_kabel_rect_left = blue_kabel.get_rect(topleft=(28, rect_ys[ys[0]]))
blue_kabel_rect_left = blue_kabel_rect_left.inflate(-250, -280)
orange_kabel_rect_left = orange_kabel.get_rect(topleft=(28, rect_ys[ys[1]]))
orange_kabel_rect_left = orange_kabel_rect_left.inflate(-250, -280)
roze_kabel_rect_left = roze_kabel.get_rect(topleft=(28, rect_ys[ys[2]]))
roze_kabel_rect_left = roze_kabel_rect_left.inflate(-250, -280)
yellow_kabel_rect_left = yellow_kabel.get_rect(topleft=(28, rect_ys[ys[3]]))
yellow_kabel_rect_left = yellow_kabel_rect_left.inflate(-250, -280)

random.shuffle(ys)

blue_y_right = blue[ys[0]]
orange_y_right = orange[ys[1]]
roze_y_right = roze[ys[2]]
yellow_y_right = yellow[ys[3]]


blue_kabel_rect_right = blue_kabel.get_rect(topleft=(270, rect_ys[ys[0]]))
blue_kabel_rect_right = blue_kabel_rect_right.inflate(-250, -280)
orange_kabel_rect_right = orange_kabel.get_rect(topleft=(270, rect_ys[ys[1]]))
orange_kabel_rect_right = orange_kabel_rect_right.inflate(-250, -280)
roze_kabel_rect_right = roze_kabel.get_rect(topleft=(270, rect_ys[ys[2]]))
roze_kabel_rect_right = roze_kabel_rect_right.inflate(-250, -280)
yellow_kabel_rect_right = yellow_kabel.get_rect(topleft=(270, rect_ys[ys[3]]))
yellow_kabel_rect_right = yellow_kabel_rect_right.inflate(-250, -280)

def meterkast(screen, mouse_x, mouse_y):
    global dragging_colors, connected_colors, color_end_positions, key_shown, key_cooldown

    screen.blit(test, (150, 125))
    screen.blit(blue_kabel, (150, blue_y_left))
    screen.blit(orange_kabel, (150, orange_y_left))
    screen.blit(roze_kabel, (150, roze_y_left))
    screen.blit(yellow_kabel, (150, yellow_y_left))
    screen.blit(blue_kabel_right, (150, blue_y_right))
    screen.blit(orange_kabel_right, (150, orange_y_right))
    screen.blit(roze_kabel_right, (150, roze_y_right))
    screen.blit(yellow_kabel_right, (150, yellow_y_right))

    # Teken alle vakken
    pygame.draw.rect(screen, (0, 0, 255), blue_kabel_rect_left, 2)
    pygame.draw.rect(screen, (255, 0, 0), orange_kabel_rect_left, 2)
    pygame.draw.rect(screen, (255, 20, 147), roze_kabel_rect_left, 2)
    pygame.draw.rect(screen, (255, 165, 0), yellow_kabel_rect_left, 2)

    pygame.draw.rect(screen, (0, 0, 255), blue_kabel_rect_right, 2)
    pygame.draw.rect(screen, (255, 0, 0), orange_kabel_rect_right, 2)
    pygame.draw.rect(screen, (255, 20, 147), roze_kabel_rect_right, 2)
    pygame.draw.rect(screen, (255, 165, 0), yellow_kabel_rect_right, 2)

    mouse_buttons = pygame.mouse.get_pressed()
    mouse_pressed = mouse_buttons[0]

    # START DRAG
    if mouse_pressed and not settings.mouse_was_pressed:
        if blue_kabel_rect_left.collidepoint(mouse_x, mouse_y):
            dragging_colors[0] = True
        elif orange_kabel_rect_left.collidepoint(mouse_x, mouse_y):
            dragging_colors[1] = True
        elif roze_kabel_rect_left.collidepoint(mouse_x, mouse_y):
            dragging_colors[2] = True
        elif yellow_kabel_rect_left.collidepoint(mouse_x, mouse_y):
            dragging_colors[3] = True

    # DRAGGING lijnen
    if dragging_colors[0]:
        start = blue_kabel_rect_left.center
        pygame.draw.line(screen, (0, 0, 255), start, (mouse_x, mouse_y), 10)

    if dragging_colors[1]:
        start = orange_kabel_rect_left.center
        pygame.draw.line(screen, (255, 0, 0), start, (mouse_x, mouse_y), 10)

    if dragging_colors[2]:
        start = roze_kabel_rect_left.center
        pygame.draw.line(screen, (255, 20, 147), start, (mouse_x, mouse_y), 10)

    if dragging_colors[3]:
        start = yellow_kabel_rect_left.center
        pygame.draw.line(screen, (255, 165, 0), start, (mouse_x, mouse_y), 10)

    # MOUSE RELEASE
    if not mouse_pressed and settings.mouse_was_pressed:
        if dragging_colors[0]:
            if blue_kabel_rect_right.collidepoint(mouse_x, mouse_y):
                connected_colors[0] = True
                color_end_positions[0] = (mouse_x, mouse_y)
            dragging_colors[0] = False

        if dragging_colors[1]:
            if orange_kabel_rect_right.collidepoint(mouse_x, mouse_y):
                connected_colors[1] = True
                color_end_positions[1] = (mouse_x, mouse_y)
            dragging_colors[1] = False

        if dragging_colors[2]:
            if roze_kabel_rect_right.collidepoint(mouse_x, mouse_y):
                connected_colors[2] = True
                color_end_positions[2] = (mouse_x, mouse_y)
            dragging_colors[2] = False

        if dragging_colors[3]:
            if yellow_kabel_rect_right.collidepoint(mouse_x, mouse_y):
                connected_colors[3] = True
                color_end_positions[3] = (mouse_x, mouse_y)
            dragging_colors[3] = False

    # Teken verbonden lijnen
    if connected_colors[0]:
        pygame.draw.line(screen, (0, 0, 255), blue_kabel_rect_left.center, color_end_positions[0], 10)

    if connected_colors[1]:
        pygame.draw.line(screen, (255, 0, 0), orange_kabel_rect_left.center, color_end_positions[1], 10)

    if connected_colors[2]:
        pygame.draw.line(screen, (255, 20, 147), roze_kabel_rect_left.center, color_end_positions[2], 10)

    if connected_colors[3]:
        pygame.draw.line(screen, (255, 165, 0), yellow_kabel_rect_left.center, color_end_positions[3], 10)

    if all(connected_colors):
        key_shown = True
        key_cooldown = 180
    
    if key_shown:
        key_image = pygame.image.load("assets/images/Rooms/sleutel_2.png")
        key_image = pygame.transform.scale(key_image, (600, 500))
        screen.blit(key_image, (0, 0))
        key_cooldown -= 1
        

        if key_cooldown <= 0:
            key_shown = False           
            settings.opened_object = None
            settings.e_knop_on_screen = ""
            settings.solving = False

    # Update mouse_was_pressed zodat drag-release werkt
    settings.mouse_was_pressed = mouse_pressed

            


