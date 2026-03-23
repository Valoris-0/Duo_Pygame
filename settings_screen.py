import game
import pygame
import settings

class SettingsMenu:
    def __init__(self):
        self.active = False

        self.btn = pygame.Rect(700, 30, 50, 50)
        self.font = pygame.font.SysFont(None, 24)

        self.controls = [
            {"name": "left", "label": self.font.render("Left Control", True, (0, 0, 0)), "rect": pygame.Rect(150, 25, 75, 50), "waiting": False},
            {"name": "right", "label": self.font.render("Right Control", True, (0, 0, 0)), "rect": pygame.Rect(150, 100, 75, 50), "waiting": False},
            {"name": "up", "label": self.font.render("Up Control", True, (0, 0, 0)), "rect": pygame.Rect(150, 175, 75, 50), "waiting": False},
            {"name": "down", "label": self.font.render("Down Control", True, (0, 0, 0)), "rect": pygame.Rect(150, 250, 75, 50), "waiting": False},
        ]

        self.music_slider_bg = pygame.Rect(150, 335, 200, 10)
        self.music_slider_knob = pygame.Rect(150 + int(settings.MUSIC_VOLUME * 200) - 10, 325, 20, 30)
        self.slider_dragging = False

        self.music_text = self.font.render("Music Volume", True, (0, 0, 0)) 

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

            # The slider handling is deels ai generate, want ik kreeg t niet voor elkaar

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

            for ctrl in self.controls:
                rect = ctrl["rect"]
                if ctrl["waiting"]:
                    pygame.draw.rect(screen, (200, 200, 200), rect, border_radius=20)
                else:
                    pygame.draw.rect(screen, (0, 200, 0), rect, border_radius=20)
                    
                    key_val = None
                    if ctrl["name"] == "left":
                        key_val = settings.LEFT_MOVEMENT
                    elif ctrl["name"] == "right":
                        key_val = settings.RIGHT_MOVEMENT
                    elif ctrl["name"] == "up":
                        key_val = settings.UP_MOVEMENT
                    elif ctrl["name"] == "down":
                        key_val = settings.DOWN_MOVEMENT

                    key_name = pygame.key.name(key_val)
                    key_surf = self.font.render(f"({key_name})", True, (0, 0, 0))
                    screen.blit(key_surf, key_surf.get_rect(center=rect.center))
                
                label = ctrl["label"]
                screen.blit(label, label.get_rect(right=rect.left - 20, centery=rect.centery))

            pygame.draw.rect(screen, (50, 50, 50), self.music_slider_bg, border_radius=5)
            pygame.draw.rect(screen, (0, 200, 0), self.music_slider_knob, border_radius=5)
            percentage = int(settings.MUSIC_VOLUME * 100)
            volume_text = self.font.render(f"{percentage}%", True, (0, 0, 0))
            screen.blit(volume_text, volume_text.get_rect(center=(self.music_slider_knob.centerx, self.music_slider_knob.top - 20)))
            screen.blit(self.music_text, self.music_text.get_rect(right=self.music_slider_bg.left - 20, centery=self.music_slider_bg.centery))
        
        pygame.draw.rect(screen, (0, 200, 0), self.btn, border_radius=45)