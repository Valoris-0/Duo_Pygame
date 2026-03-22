import game
import pygame
import loading_screen
import settings
import victory_screen

class SettingsMenu:
    def __init__(self):
        self.active = False
        self.waiting_for_key_left = False
        self.waiting_for_key_right = False
        self.waiting_for_key_up = False
        self.waiting_for_key_down = False

        self.btn = pygame.Rect(700, 30, 50, 50)
        self.lbs = pygame.Rect(150, 25, 75, 50)
        self.rbs = pygame.Rect(150, 100, 75, 50)
        self.ubs = pygame.Rect(150, 175, 75, 50)
        self.dbs = pygame.Rect(150, 250, 75, 50)

        self.music_slider_bg = pygame.Rect(150, 335, 200, 10)
        self.music_slider_knob = pygame.Rect(150 + int(settings.MUSIC_VOLUME * 200) - 10, 325, 20, 30)
        self.slider_dragging = False

        self.font = pygame.font.SysFont(None, 24)
        self.lbs_text = self.font.render("Left Control", True, (0, 0, 0))
        self.rbs_text = self.font.render("Right Control", True, (0, 0, 0))
        self.ubs_text = self.font.render("Up Control", True, (0, 0, 0))
        self.dbs_text = self.font.render("Down Control", True, (0, 0, 0))
        self.music_text = self.font.render("Music Volume", True, (0, 0, 0))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not settings.scare_active and not settings.scare and not settings.victory_screen_active and not settings.is_loading:
            self.active = not self.active
            self.waiting_for_key_left = False
            self.waiting_for_key_right = False
        if event.type == pygame.MOUSEBUTTONDOWN and self.btn.collidepoint(event.pos):
            if self.active:
                self.active = False
                self.waiting_for_key_left = False
                self.waiting_for_key_right = False
                self.waiting_for_key_down = False
                self.waiting_for_key_up = False
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

            if event.type == pygame.MOUSEBUTTONDOWN and self.ubs.collidepoint(event.pos):
                self.waiting_for_key_up = True
            if event.type == pygame.KEYDOWN and self.waiting_for_key_up:
                settings.UP_MOVEMENT = event.key
                self.waiting_for_key_up = False

            if event.type == pygame.MOUSEBUTTONDOWN and self.dbs.collidepoint(event.pos):
                self.waiting_for_key_down = True
            if event.type == pygame.KEYDOWN and self.waiting_for_key_down:
                settings.DOWN_MOVEMENT = event.key
                self.waiting_for_key_down = False

            if event.type == pygame.MOUSEBUTTONDOWN and (self.music_slider_bg.collidepoint(event.pos) or self.music_slider_knob.collidepoint(event.pos)):
                self.slider_dragging = True
            
            if event.type == pygame.MOUSEBUTTONUP:
                self.slider_dragging = False

            if event.type == pygame.MOUSEMOTION and self.slider_dragging:
                mouse_x = event.pos[0]
                new_x = max(self.music_slider_bg.left, min(mouse_x, self.music_slider_bg.right))
                self.music_slider_knob.centerx = new_x
                settings.MUSIC_VOLUME = (new_x - self.music_slider_bg.left) / self.music_slider_bg.width
                pygame.mixer.music.set_volume(settings.MUSIC_VOLUME)

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

            if self.waiting_for_key_up:
                pygame.draw.rect(screen, (200, 200, 200), self.ubs, border_radius=20)
            else:
                pygame.draw.rect(screen, (0, 200, 0), self.ubs, border_radius=20)
                u_key_name = pygame.key.name(settings.UP_MOVEMENT)
                u_key_surf = self.font.render(f"({u_key_name})", True, (0, 0, 0))
                screen.blit(u_key_surf, u_key_surf.get_rect(center=self.ubs.center))
            
            screen.blit(self.ubs_text, self.ubs_text.get_rect(right=self.ubs.left - 20, centery=self.ubs.centery))

            if self.waiting_for_key_down:
                pygame.draw.rect(screen, (200, 200, 200), self.dbs, border_radius=20)
            else:
                pygame.draw.rect(screen, (0, 200, 0), self.dbs, border_radius=20)
                d_key_name = pygame.key.name(settings.DOWN_MOVEMENT)
                d_key_surf = self.font.render(f"({d_key_name})", True, (0, 0, 0))
                screen.blit(d_key_surf, d_key_surf.get_rect(center=self.dbs.center))
            
            screen.blit(self.dbs_text, self.dbs_text.get_rect(right=self.dbs.left - 20, centery=self.dbs.centery))

            pygame.draw.rect(screen, (50, 50, 50), self.music_slider_bg, border_radius=5)
            pygame.draw.rect(screen, (0, 200, 0), self.music_slider_knob, border_radius=5)
            percentage = int(settings.MUSIC_VOLUME * 100)
            volume_text = self.font.render(f"{percentage}%", True, (0, 0, 0))
            screen.blit(volume_text, volume_text.get_rect(center=(self.music_slider_knob.centerx, self.music_slider_knob.top - 20)))
            screen.blit(self.music_text, self.music_text.get_rect(right=self.music_slider_bg.left - 20, centery=self.music_slider_bg.centery))
        
        pygame.draw.rect(screen, (0, 200, 0), self.btn, border_radius=45)
