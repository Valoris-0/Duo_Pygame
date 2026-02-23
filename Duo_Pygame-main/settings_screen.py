import pygame
import settings

class SettingsMenu:
    def __init__(self):
        self.active = False
        self.waiting_for_key_left = False
        self.waiting_for_key_right = False

        self.btn = pygame.Rect(700, 30, 50, 50)
        self.lbs = pygame.Rect(150, 50, 75, 50)
        self.rbs = pygame.Rect(150, 125, 75, 50)

        self.font = pygame.font.SysFont(None, 24)
        self.lbs_text = self.font.render("Left Control", True, (0, 0, 0))
        self.rbs_text = self.font.render("Right Control", True, (0, 0, 0))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.active = not self.active
            self.waiting_for_key_left = False
            self.waiting_for_key_right = False
        if event.type == pygame.MOUSEBUTTONDOWN and self.btn.collidepoint(event.pos):
            if self.active:
                self.active = False
                self.waiting_for_key_left = False
                self.waiting_for_key_right = False
            else:
                self.active = True
        
        if self.active:
            if event.type == pygame.MOUSEBUTTONDOWN and self.lbs.collidepoint(event.pos):
                self.waiting_for_key_left = True
            if event.type == pygame.KEYDOWN and self.waiting_for_key_left:
                settings.LEFT_MOVEMENT = event.key
                self.waiting_for_key_left = False

            if event.type == pygame.MOUSEBUTTONDOWN and self.rbs.collidepoint(event.pos):
                self.waiting_for_key_right = True
            if event.type == pygame.KEYDOWN and self.waiting_for_key_right:
                settings.RIGHT_MOVEMENT = event.key
                self.waiting_for_key_right = False
    
    def draw(self, screen):
        if self.active:
            screen.fill((100, 149, 237))

            if self.waiting_for_key_left:
                pygame.draw.rect(screen, (200, 200, 200), self.lbs, border_radius=20)
            else:
                pygame.draw.rect(screen, (0, 200, 0), self.lbs, border_radius=20)
                l_key_name = pygame.key.name(settings.LEFT_MOVEMENT)
                l_key_surf = self.font.render(f"({l_key_name})", True, (0, 0, 0))
                screen.blit(l_key_surf, l_key_surf.get_rect(center=self.lbs.center))
            
            screen.blit(self.lbs_text, self.lbs_text.get_rect(right=self.lbs.left - 20, centery=self.lbs.centery))

            if self.waiting_for_key_right:
                pygame.draw.rect(screen, (200, 200, 200), self.rbs, border_radius=20)
            else:
                pygame.draw.rect(screen, (0, 200, 0), self.rbs, border_radius=20)
                r_key_name = pygame.key.name(settings.RIGHT_MOVEMENT)
                r_key_surf = self.font.render(f"({r_key_name})", True, (0, 0, 0))
                screen.blit(r_key_surf, r_key_surf.get_rect(center=self.rbs.center))
            
            screen.blit(self.rbs_text, self.rbs_text.get_rect(right=self.rbs.left - 20, centery=self.rbs.centery))
        
        pygame.draw.rect(screen, (0, 200, 0), self.btn, border_radius=45)
