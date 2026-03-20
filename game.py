
import pygame
import heartrate
import settings
import highscore
import hallway
import monster
import room_1_file
import room_2_file
import room_3_file
import jumpscare
import kluis
import paper_code
import elektriciteitskast
import random

def init_resources():
    global start_screen, start_text, start_text_rect, titel_text, rooms, options_text, options_text_rect, highscore_text, highscore_text_rect, highscore_number, highscore_number_rect
    rooms = [room_1_file, room_2_file, room_3_file]
    start_screen = pygame.image.load("assets/images/Start_screen.png").convert_alpha()
    start_screen = pygame.transform.scale(start_screen, (800, 400))

    font_normal = pygame.font.Font("assets/fonts/Heartless.ttf", 36)
    start_text = font_normal.render("START", True, (255, 100, 0))
    start_text_rect = start_text.get_rect(center=(800 // 2, 400 // 2))
    options_text = font_normal.render("OPTIONS", True, (255, 100, 0))
    options_text_rect = options_text.get_rect(center=(800 // 2, 400 // 2 + 50))
    
    font_highscore = pygame.font.SysFont(None, 40)
    highscore_text = font_normal.render("HIGHSCORE", True, (255, 100, 0))
    highscore_text_rect = highscore_text.get_rect(center=(800 // 2 - 60, 400 // 2 + 100))
    highscore_number = font_highscore.render(f"{highscore.format_time(int(highscore.highscore))}", True, (255, 100, 0))
    highscore_number_rect = highscore_number.get_rect(center=(800 // 2 + 65, 400 // 2 + 100))

    font_large = pygame.font.Font("assets/fonts/Heartless.ttf", 96)
    titel_text = font_large.render("CARNAGE CORRIDOR", True, (136, 8, 8))

class GameScreen:
    def __init__(self, player, settings_menu_screen):
        self.active = settings.in_room
        self.player = player
        self.settings_menu_screen = settings_menu_screen

    def update(self, screen, dt):
        screen.fill((0, 0, 0))
        if settings.start_menu:
            screen.blit(start_screen, (0, 0))
            screen.blit(start_text, start_text_rect)
            screen.blit(titel_text, titel_text.get_rect(center=(800 // 2, 100)))
            screen.blit(options_text, options_text_rect)
            screen.blit(highscore_text, highscore_text_rect)
            screen.blit(highscore_number, highscore_number_rect)
            return

        if not settings.in_room:
            if settings.current_mode != "hallway":

                came_from_room = (settings.current_mode == "room")

                settings.WIDTH = 800
                settings.HEIGHT = 400
                if screen.get_size() != (settings.WIDTH, settings.HEIGHT):
                    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
                    screen.fill((0, 0, 0))

                self.player.y = 155

                if came_from_room:
                    self.player.x = float(settings.HALLWAY_DOOR_X) - self.player.width / 2

                settings.current_mode = "hallway"
            else:
                moved = self.player.handle_input_side(screen, dt)

                self.player.update()

                hallway.moving(screen, moved, self.player.x)
                monster.moving_monster(screen, moved, self.player.x, dt)
                self.player.draw_side(screen)

                if self.player.player_hitbox.colliderect(monster.monster_hitbox) and not settings.scare:
                    monster.jumpscare(screen)

        else:
            if settings.current_mode != "room":
                settings.WIDTH = 600
                settings.HEIGHT = 500
                if screen.get_size() != (settings.WIDTH, settings.HEIGHT):
                    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
                    screen.fill((0, 0, 0))

                settings.current_mode = "room"
                if not settings.won and len(rooms) > 0:
                    self.current_room_module = random.choice(rooms)
                settings.current_room_module_name = self.current_room_module.__name__
            else:
                screen.fill((0, 0, 0))
                self.current_room_module.draw_room(screen, dt)
                self.player.handle_input_top(screen, dt)
                self.player.update()
                self.player.draw_top(screen)

                if settings.scare_active:
                    jumpscare.scare(screen)

                if settings.solving:
                    rm = settings.current_room_module_name
                    if rm == "room_1_file":
                        if settings.opened_object == "kluis":
                            pos = pygame.mouse.get_pos()
                            kluis.open_kluis(screen, pos, dt)
                        elif settings.opened_object in ("bed", "doos"):
                            paper_code.open_paper(screen)
                    elif rm == "room_2_file":
                        if settings.opened_object == "electrisiteitskast":
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            elektriciteitskast.meterkast(screen, mouse_x, mouse_y, dt)
                        elif settings.opened_object in ("bed", "doos"):
                            gereedschap = pygame.image.load("assets/images/Rooms/elektriciteit/gereedschap.png")
                            gereedschap = pygame.transform.scale(gereedschap, (600, 500))
                            screen.blit(gereedschap, (0, 0))
                            settings.gereedschap_got = True
                    elif rm == "room_3_file":
                        if settings.opened_object == "bed":
                            heartrate.meten(screen, dt)
        if not settings.in_room and not settings.scare and not settings.heartrate_scare:
            font = pygame.font.SysFont(None, 24)
            time = settings.HIGHSCORE
            time_text = highscore.format_time(int(time))
            time_surface = font.render(f"Time: {time_text}", True, (255, 255, 255))
            screen.blit(time_surface, (settings.WIDTH - 250, 50))

        self.settings_menu_screen.draw(screen)

