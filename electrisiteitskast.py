import pygame
import settings
import random

electrisiteitskast = pygame.image.load("assets/images/Rooms/elektriciteit/electrisiteits kast.png")
electrisiteitskast = pygame.transform.scale(electrisiteitskast, (300, 300))

kabel_1_x = 30
kabel_2_x = 95
kabel_3_x = 150
kabel_4_x = 210


blue_kabel = pygame.image.load("assets/images/Rooms/elektriciteit/blue_kabel.png")
blue_kabel = pygame.transform.scale(blue_kabel, (300, 300))

blue_kabel_rect_left = blue_kabel.get_rect(topleft=(28, kabel_2_x))
blue_kabel_rect_left = blue_kabel_rect_left.inflate(-250, -280)

blue_kabel_rect_right = blue_kabel.get_rect(topleft=(270, kabel_2_x))
blue_kabel_rect_right = blue_kabel_rect_right.inflate(-250, -280)


orange_kabel = pygame.image.load("assets/images/Rooms/elektriciteit/orange_kabel.png")
orange_kabel = pygame.transform.scale(orange_kabel, (300, 300))

orange_kabel_rect_left = orange_kabel.get_rect(topleft=(28, kabel_3_x))
orange_kabel_rect_left = orange_kabel_rect_left.inflate(-250, -280)

orange_kabel_rect_right = orange_kabel.get_rect(topleft=(270, kabel_1_x))
orange_kabel_rect_right = orange_kabel_rect_right.inflate(-250, -280)


roze_kabel = pygame.image.load("assets/images/Rooms/elektriciteit/roze_kabel.png")
roze_kabel = pygame.transform.scale(roze_kabel, (300, 300))

roze_kabel_rect_left = roze_kabel.get_rect(topleft=(28, kabel_4_x))
roze_kabel_rect_left = roze_kabel_rect_left.inflate(-250, -280)

roze_kabel_rect_right = roze_kabel.get_rect(topleft=(270, kabel_4_x))
roze_kabel_rect_right = roze_kabel_rect_right.inflate(-250, -280)


yellow_kabel = pygame.image.load("assets/images/Rooms/elektriciteit/yellow_kabel.png")
yellow_kabel = pygame.transform.scale(yellow_kabel, (300, 300))

yellow_kabel_rect_left = yellow_kabel.get_rect(topleft=(28, kabel_1_x))
yellow_kabel_rect_left = yellow_kabel_rect_left.inflate(-250, -280)

yellow_kabel_rect_right = yellow_kabel.get_rect(topleft=(270, kabel_3_x))
yellow_kabel_rect_right = yellow_kabel_rect_right.inflate(-250, -280)

dragging_colors = [False, False, False, False] # Blue, Orange, Roze, Yellow
connected_colors = [False, False, False, False] # Blue, Orange, Roze, Yellow
color_end_positions = [(0,0), (0,0), (0,0), (0,0)] # Blue, Orange, Roze, Yellow



def meterkast(screen, mouse_x, mouse_y):
    global dragging_colors, connected_colors, color_end_positions, settings

    screen.blit(electrisiteitskast, (150, 125))

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
        pygame.draw.line(screen, (0, 0, 255), (175, 245), (mouse_x, mouse_y), 10)
    if dragging_colors[1]:
        pygame.draw.line(screen, (255, 0, 0), (175, 300), (mouse_x, mouse_y), 10)
    if dragging_colors[2]:
        pygame.draw.line(screen, (255, 20, 147), (175, 360), (mouse_x, mouse_y), 10)
    if dragging_colors[3]:
        pygame.draw.line(screen, (255, 165, 0), (175, 180), (mouse_x, mouse_y), 10)

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
        pygame.draw.line(screen, (0, 0, 255), (175, 245), color_end_positions[0], 10)
    if connected_colors[1]:
        pygame.draw.line(screen, (255, 0, 0), (175, 300), color_end_positions[1], 10)
    if connected_colors[2]:
        pygame.draw.line(screen, (255, 20, 147), (175, 360), color_end_positions[2], 10)
    if connected_colors[3]:
        pygame.draw.line(screen, (255, 165, 0), (175, 180), color_end_positions[3], 10)

    # Update mouse_was_pressed zodat drag-release werkt
    settings.mouse_was_pressed = mouse_pressed

            


