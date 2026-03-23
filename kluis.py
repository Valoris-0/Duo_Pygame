import game
import pygame
import room_1_file
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
    global wrong_countdown, solved
    wrong_countdown = 2.0
    solved = False

reset_kluis_state()

def open_kluis(screen, pos, dt):
    global wrong_countdown, font, solved
    if len(settings.code_ingevoerd) == 0:
        screen.blit(kluis_enter_number, (150, 100))
    else:
        screen.blit(kluis_leeg, (150, 100))

    mouse_buttons = pygame.mouse.get_pressed()
    mouse_pressed = mouse_buttons[0]
    
    keys = pygame.key.get_pressed()
    current_keys_pressed = set()

    rects = [(i, pygame.Rect(235 + ((i-1)%3)*48, 180 + ((i-1)//3)*45, 45, 35)) for i in range(1, 10)]
    rects.append((0, pygame.Rect(283, 315, 45, 35)))
    
    (rect_1, rect_2, rect_3, rect_4, rect_5, rect_6, rect_7, rect_8, rect_9, rect_0) = [r for _, r in rects]

    if mouse_pressed and not settings.mouse_was_pressed and len(settings.code_ingevoerd) < 4:
        for num, rect in rects:
            if rect.collidepoint(pos):
                settings.code_ingevoerd.append(num)
                break

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
            solved = True
            animatie.kluis_openen(screen)
            if room_1_file in game.rooms:
                game.rooms.remove(room_1_file)
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
        for i in range(10):
            num, rect = rects[i]
            pygame.draw.rect(screen, (255, 0, 0), rect, 2)

    