import pygame
import settings

schakelaar_uit = pygame.image.load("assets\images\Rooms\schakelaar.png")
schakelaar_aan = pygame.transform.rotate(schakelaar_uit, 180)


schakelaar_rect_1 = pygame.Rect(235, 180, 45, 85)
schakelaar_rect_2 = pygame.Rect(285, 180, 45, 85)
schakelaar_rect_3 = pygame.Rect(335, 180, 45, 85)

schakelaar_1_x = 100
schakelaar_2_x = 150
schakelaar_3_x = 200

schakelaren = [False, False, False]

def game(screen, dt, pos):
    if not schakelaren[0]:
        screen.blit(schakelaar_uit, (schakelaar_1_x,100))
    if not schakelaren[1]:
        screen.blit(schakelaar_uit, (schakelaar_2_x,100))
    if not schakelaren[2]:
        screen.blit(schakelaar_uit, (schakelaar_3_x,100))
    if schakelaren[0]:
        screen.blit(schakelaar_aan, (schakelaar_1_x,100))
    if schakelaren[1]:
        screen.blit(schakelaar_aan, (schakelaar_2_x,100))
    if schakelaren[2]:
        screen.blit(schakelaar_aan, (schakelaar_3_x,100))
    
    mouse_buttons = pygame.mouse.get_pressed()
    mouse_pressed = mouse_buttons[0]
    
    
    if mouse_pressed and not settings.mouse_was_pressed:
        if schakelaar_rect_1.collidepoint(pos):
            schakelaren[0] = not schakelaren[0]
        if schakelaar_rect_2.collidepoint(pos):
            schakelaren[1] = not schakelaren[1]
        if schakelaar_rect_3.collidepoint(pos):
            schakelaren[2] = not schakelaren[2]
            
    settings.mouse_was_pressed = mouse_pressed
    
    if all(schakelaren):
        settings.stroom = True
    
    if settings.debugmode:
        pygame.draw.rect(screen, (255, 0, 0), schakelaar_rect_1, 2)
        pygame.draw.rect(screen, (255, 0, 0), schakelaar_rect_2, 2)
        pygame.draw.rect(screen, (255, 0, 0), schakelaar_rect_3, 2)
    
    
    