import game
import pygame
import settings
import os

class SettingsMenu:
    def __init__(self):
        self.active = False

        self.btn = pygame.Rect(700, 30, 50, 50)
        self.font = pygame.font.SysFont(None, 24)
        self.title_font = pygame.font.SysFont(None, 48)

        self.gear_icon = pygame.image.load("assets/images/gear_icon.png").convert_alpha()
        self.gear_icon = pygame.transform.scale(self.gear_icon, (40, 40))

        self.controls = [
            {"name": "left", "label": self.font.render("Left Control", True, (255, 255, 255)), "rect": pygame.Rect(150, 80, 150, 40), "waiting": False},
            {"name": "right", "label": self.font.render("Right Control", True, (255, 255, 255)), "rect": pygame.Rect(150, 130, 150, 40), "waiting": False},
            {"name": "up", "label": self.font.render("Up Control", True, (255, 255, 255)), "rect": pygame.Rect(150, 180, 150, 40), "waiting": False},
            {"name": "down", "label": self.font.render("Down Control", True, (255, 255, 255)), "rect": pygame.Rect(150, 230, 150, 40), "waiting": False},
        ]

        self.music_slider_bg = pygame.Rect(150, 310, 200, 10)
        self.music_slider_knob = pygame.Rect(150 + int(settings.MUSIC_VOLUME * 200) - 10, 300, 20, 30)
        self.slider_dragging = False
        self.music_text = self.font.render("Music", True, (255, 255, 255)) 

        self.reset_btn = pygame.Rect(150, 410, 200, 40)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not settings.scare_active and not settings.scare and not settings.victory_screen_active and not settings.is_loading:
            self.active = not self.active
            for ctrl in self.controls:
                ctrl["waiting"] = False

        if event.type == pygame.MOUSEBUTTONDOWN and self.btn.collidepoint(event.pos):
            self.active = not self.active
            for ctrl in self.controls:
                ctrl["waiting"] = False
        
        if self.active:
            for ctrl in self.controls:
                if event.type == pygame.MOUSEBUTTONDOWN and ctrl["rect"].collidepoint(event.pos):
                    ctrl["waiting"] = True
                
                if event.type == pygame.KEYDOWN and ctrl["waiting"]:
                    if ctrl["name"] == "left":
                        settings.LEFT_MOVEMENT = event.key
                    elif ctrl["name"] == "right":
                        settings.RIGHT_MOVEMENT = event.key
                    elif ctrl["name"] == "up":
                        settings.UP_MOVEMENT = event.key
                    elif ctrl["name"] == "down":
                        settings.DOWN_MOVEMENT = event.key
                    
                    ctrl["waiting"] = False

            if event.type == pygame.MOUSEBUTTONDOWN and self.reset_btn.collidepoint(event.pos):
                settings.LEFT_MOVEMENT = pygame.K_a
                settings.RIGHT_MOVEMENT = pygame.K_d
                settings.UP_MOVEMENT = pygame.K_w
                settings.DOWN_MOVEMENT = pygame.K_s
                settings.MUSIC_VOLUME = 0.5
                self.music_slider_knob.centerx = self.music_slider_bg.left + int(0.5 * 200)
                pygame.mixer.music.set_volume(0.5)

            # The Music Slider handling is deels ai generate, want ik kreeg t niet voor elkaar
            if event.type == pygame.MOUSEBUTTONDOWN and (self.music_slider_bg.collidepoint(event.pos) or self.music_slider_knob.collidepoint(event.pos)):
                self.slider_dragging = True

            if event.type == pygame.MOUSEBUTTONUP:
                self.slider_dragging = False

            if event.type == pygame.MOUSEMOTION:
                mouse_x = event.pos[0]
                if self.slider_dragging:
                    new_x = max(self.music_slider_bg.left, min(mouse_x, self.music_slider_bg.right))
                    self.music_slider_knob.centerx = new_x
                    settings.MUSIC_VOLUME = (new_x - self.music_slider_bg.left) / self.music_slider_bg.width
                    pygame.mixer.music.set_volume(settings.MUSIC_VOLUME)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        
        if self.active:
            overlay = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 200)) # Dark transparent background
            screen.blit(overlay, (0, 0))

            header_text = self.title_font.render("SETTINGS", True, (255, 255, 255))
            screen.blit(header_text, (150, 30))

            for ctrl in self.controls:
                rect = ctrl["rect"]
                hovered = rect.collidepoint(mouse_pos)
                
                if ctrl["waiting"]:
                    pygame.draw.rect(screen, (200, 200, 200), rect, border_radius=10)
                    key_surf = self.font.render("Press any key...", True, (0, 0, 0))
                else:
                    color = (0, 250, 0) if hovered else (0, 200, 0)
                    pygame.draw.rect(screen, color, rect, border_radius=10)
                    
                    key_val = None
                    if ctrl["name"] == "left":
                        key_val = settings.LEFT_MOVEMENT
                    elif ctrl["name"] == "right":
                        key_val = settings.RIGHT_MOVEMENT
                    elif ctrl["name"] == "up":
                        key_val = settings.UP_MOVEMENT
                    elif ctrl["name"] == "down":
                        key_val = settings.DOWN_MOVEMENT

                    key_name = pygame.key.name(key_val).upper()
                    key_surf = self.font.render(key_name, True, (0, 0, 0))
                
                screen.blit(key_surf, key_surf.get_rect(center=rect.center))
                label = ctrl["label"]
                screen.blit(label, label.get_rect(right=rect.left - 20, centery=rect.centery))

            m_hover = self.music_slider_knob.collidepoint(mouse_pos)
            
            pygame.draw.rect(screen, (100, 100, 100), self.music_slider_bg, border_radius=5)
            pygame.draw.rect(screen, (0, 250, 0) if m_hover or self.slider_dragging else (0, 200, 0), self.music_slider_knob, border_radius=5)
            music_pct = self.font.render(f"{int(settings.MUSIC_VOLUME * 100)}%", True, (255, 255, 255))
            screen.blit(music_pct, music_pct.get_rect(left=self.music_slider_bg.right + 15, centery=self.music_slider_bg.centery))
            screen.blit(self.music_text, self.music_text.get_rect(right=self.music_slider_bg.left - 20, centery=self.music_slider_bg.centery))

            reset_hover = self.reset_btn.collidepoint(mouse_pos)
            pygame.draw.rect(screen, (250, 50, 50) if reset_hover else (200, 50, 50), self.reset_btn, border_radius=10)
            reset_text = self.font.render("Reset to Defaults", True, (255, 255, 255))
            screen.blit(reset_text, reset_text.get_rect(center=self.reset_btn.center))

        btn_hover = self.btn.collidepoint(mouse_pos)
        pygame.draw.rect(screen, (150, 150, 150) if btn_hover else (100, 100, 100), self.btn, border_radius=10)
        
        if self.active:
            x_text = self.title_font.render("X", True, (255, 50, 50))
            screen.blit(x_text, x_text.get_rect(center=self.btn.center))
        else:
            if self.gear_icon:
                screen.blit(self.gear_icon, self.gear_icon.get_rect(center=self.btn.center))
            else:
                s_text = self.title_font.render("O", True, (200, 200, 200))
                screen.blit(s_text, s_text.get_rect(center=self.btn.center))