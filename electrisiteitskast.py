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

dragging_blue = False
dragging_orange = False
dragging_roze = False
dragging_yellow = False

blue_connected = False
orange_connected = False
roze_connected = False
yellow_connected = False

blue_end_pos = (0,0)
orange_end_pos = (0,0)
roze_end_pos = (0,0)   
yellow_end_pos = (0,0)


def meterkast(screen, mouse_x, mouse_y):
    global blue_kabel_rect_left, orange_kabel_rect_left, roze_kabel_rect_left, yellow_kabel_rect_left, dragging_blue, dragging_orange, dragging_roze, dragging_yellow, kabel_1_x, kabel_2_x, kabel_3_x, kabel_4_x, blue_connected, blue_end_pos, orange_connected, orange_end_pos, roze_connected, roze_end_pos, yellow_connected, yellow_end_pos

    screen.blit(electrisiteitskast, (150, 125))
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

    if blue_kabel_rect_left.collidepoint(mouse_x, mouse_y):
        if mouse_pressed and not settings.mouse_was_pressed and not dragging_orange and not dragging_roze and not dragging_yellow: 
            dragging_blue = True 
    
    elif orange_kabel_rect_left.collidepoint(mouse_x, mouse_y):
        if mouse_pressed and not settings.mouse_was_pressed and not dragging_blue and not dragging_roze and not dragging_yellow: 
            dragging_orange = True 
    
    elif roze_kabel_rect_left.collidepoint(mouse_x, mouse_y):
        if mouse_pressed and not settings.mouse_was_pressed and not dragging_blue and not dragging_orange and not dragging_yellow: 
            dragging_roze = True

    elif yellow_kabel_rect_left.collidepoint(mouse_x, mouse_y):
        if mouse_pressed and not settings.mouse_was_pressed and not dragging_blue and not dragging_orange and not dragging_roze: 
            dragging_yellow = True


    if dragging_blue:
        pygame.draw.line(screen, (0,0,255), (175, 245), pygame.mouse.get_pos(), 10)

    elif dragging_orange:
        pygame.draw.line(screen, (255,0,0), (175, 300), pygame.mouse.get_pos(), 10)

    elif dragging_roze:
        pygame.draw.line(screen, (255,20,147), (175, 360), pygame.mouse.get_pos(), 10)

    elif dragging_yellow:
        pygame.draw.line(screen, (255,165,0), (175, 180), pygame.mouse.get_pos(), 10)


    if dragging_blue and blue_kabel_rect_right.collidepoint(mouse_x, mouse_y):
        if mouse_pressed and not settings.mouse_was_pressed:
            dragging_blue = False
            blue_end_pos = pygame.mouse.get_pos()
            blue_connected = True
    
    elif dragging_orange and orange_kabel_rect_right.collidepoint(mouse_x, mouse_y):
        if mouse_pressed and not settings.mouse_was_pressed:
            dragging_orange = False
            orange_end_pos = pygame.mouse.get_pos()
            orange_connected = True

    elif dragging_roze and roze_kabel_rect_right.collidepoint(mouse_x, mouse_y):
        if mouse_pressed and not settings.mouse_was_pressed:
            dragging_roze = False
            roze_end_pos = pygame.mouse.get_pos()
            roze_connected = True

    elif dragging_yellow and yellow_kabel_rect_right.collidepoint(mouse_x, mouse_y):
        if mouse_pressed and not settings.mouse_was_pressed:
            dragging_yellow = False
            yellow_end_pos = pygame.mouse.get_pos()
            yellow_connected = True

    if blue_connected:
        pygame.draw.line(screen, (0,0,255), (175, 245), blue_end_pos, 10)

    if orange_connected:
        pygame.draw.line(screen, (255,0,0), (175, 300), orange_end_pos, 10)

    if roze_connected:
        pygame.draw.line(screen, (255,20,147), (175, 360), roze_end_pos, 10)
    
    if yellow_connected:
        pygame.draw.line(screen, (255,165,0), (175, 180), yellow_end_pos, 10)
            

            



