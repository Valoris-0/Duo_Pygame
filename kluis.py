import pygame
import settings
import Kluis_ani as animatie

kluis_enter_number = pygame.image.load("assets/images/Rooms/kluis_enter-number.jpeg").convert_alpha()
kluis_enter_number = pygame.transform.scale(kluis_enter_number, (300, 300))

kluis_leeg = pygame.image.load("assets/images/Rooms/kluis_leeg.png").convert_alpha()
kluis_leeg = pygame.transform.scale(kluis_leeg, (300, 300))

kluis_wrong_code = pygame.image.load("assets/images/Rooms/kluis_wrong_code.png").convert_alpha()
kluis_wrong_code = pygame.transform.scale(kluis_wrong_code, (300, 300))

font = pygame.font.SysFont(None, 50)

def reset_kluis_state():
    global wrong_countdown
    wrong_countdown = 2.0

reset_kluis_state()

def open_kluis(screen, pos, dt):
    global wrong_countdown, font
    if len(settings.code_ingevoerd) == 0:
        screen.blit(kluis_enter_number, (150, 100))
    else:
        screen.blit(kluis_leeg, (150, 100))

    mouse_buttons = pygame.mouse.get_pressed()
    mouse_pressed = mouse_buttons[0]
    
    keys = pygame.key.get_pressed()
    current_keys_pressed = set()

    rect_1 = pygame.Rect(235, 180, 45, 35)
    rect_2 = pygame.Rect(283, 180, 45, 35)
    rect_3 = pygame.Rect(331, 180, 45, 35)
    rect_4 = pygame.Rect(235, 225, 45, 35)
    rect_5 = pygame.Rect(283, 225, 45, 35)
    rect_6 = pygame.Rect(331, 225, 45, 35)
    rect_7 = pygame.Rect(235, 270, 45, 35)
    rect_8 = pygame.Rect(283, 270, 45, 35)
    rect_9 = pygame.Rect(331, 270, 45, 35)
    rect_0 = pygame.Rect(283, 315, 45, 35)

    if mouse_pressed and not settings.mouse_was_pressed and len(settings.code_ingevoerd) < 4:
        if rect_1.collidepoint(pos):
            settings.code_ingevoerd.append(1)
        elif rect_2.collidepoint(pos):
            settings.code_ingevoerd.append(2)
        elif rect_3.collidepoint(pos):
            settings.code_ingevoerd.append(3)
        elif rect_4.collidepoint(pos):
            settings.code_ingevoerd.append(4)
        elif rect_5.collidepoint(pos):
            settings.code_ingevoerd.append(5)
        elif rect_6.collidepoint(pos):
            settings.code_ingevoerd.append(6)
        elif rect_7.collidepoint(pos):
            settings.code_ingevoerd.append(7)
        elif rect_8.collidepoint(pos):
            settings.code_ingevoerd.append(8)
        elif rect_9.collidepoint(pos):
            settings.code_ingevoerd.append(9)
        elif rect_0.collidepoint(pos):
            settings.code_ingevoerd.append(0)

    ingevoerd_string = "".join(map(str, settings.code_ingevoerd))
    text = font.render(ingevoerd_string, True, (255,255,0))

    screen.blit(text, (265, 120))

    if len(settings.code_ingevoerd) >= 4:
        
        if settings.code_ingevoerd == settings.code:
            settings.solving = False
            settings.opened_object = None
            settings.e_knop_on_screen = ""
            settings.code_ingevoerd = []
            settings.code_correct = True
            settings.animating_safe = True
            animatie.animatie_timer_kluis = 0
            animatie.animatie_timer_sleutel = 0
            print("kluis open!")
            animatie.kluis_openen(screen)
        else:
            wrong_countdown -= dt
            screen.blit(kluis_wrong_code, (150, 100))
            if wrong_countdown <= 0:
                wrong_countdown = 2.0
                settings.code_ingevoerd = []
                print("verkeerde code, probeer opnieuw")
    
    settings.mouse_was_pressed = mouse_pressed
    settings.keys_were_pressed = current_keys_pressed

    if settings.debugmode:
        pygame.draw.rect(screen, (255, 0, 0), rect_1, 2)
        pygame.draw.rect(screen, (255, 0, 0), rect_2, 2)
        pygame.draw.rect(screen, (255, 0, 0), rect_3, 2)
        pygame.draw.rect(screen, (255, 0, 0), rect_4, 2)
        pygame.draw.rect(screen, (255, 0, 0), rect_5, 2)
        pygame.draw.rect(screen, (255, 0, 0), rect_6, 2)
        pygame.draw.rect(screen, (255, 0, 0), rect_7, 2)
        pygame.draw.rect(screen, (255, 0, 0), rect_8, 2)
        pygame.draw.rect(screen, (255, 0, 0), rect_9, 2)
        pygame.draw.rect(screen, (255, 0, 0), rect_0, 2)
    