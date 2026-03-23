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
import schakelaar
from music import MusicManager

play_music_game = None
play_music = None

def init_resources():
    global start_screen, start_text, start_text_rect, titel_text, rooms, options_text, options_text_rect, font_normal, font_large
    global highscore_text, highscore_text_rect, highscore_number, highscore_number_rect, play_music, play_music_game, play_music_scare, play_music_victory
    rooms = [room_1_file, room_2_file, room_3_file]
    start_screen = pygame.image.load("assets/images/Start_screen.png").convert_alpha()
    start_screen = pygame.transform.scale(start_screen, (800, 400))

    font_normal = pygame.font.Font("assets/fonts/Heartless.ttf", 36)
    start_text = font_normal.render("START", True, (255, 100, 0))
    start_text_rect = start_text.get_rect(center=(800 // 2, 400 // 2))
    options_text = font_normal.render("OPTIONS", True, (255, 100, 0))
    options_text_rect = options_text.get_rect(center=(800 // 2, 400 // 2 + 50))

    font_large = pygame.font.Font("assets/fonts/Heartless.ttf", 96)
    titel_text = font_large.render("CARNAGE CORRIDOR", True, (136, 8, 8))

    play_music = MusicManager("assets/sounds/start_background.mp3")
    play_music_game = MusicManager("assets/sounds/game_background.mp3")
    play_music_scare = MusicManager("assets/sounds/Jumpscare.mp3")
    play_music_victory = MusicManager("assets/sounds/victory.mp3")

key_1 = pygame.image.load("assets/images/Rooms/sleutel_1.png").convert_alpha()
key_1 = pygame.transform.scale(key_1, (100, 50))

key_2 = pygame.image.load("assets/images/Rooms/sleutel_2.png").convert_alpha()
key_2 = pygame.transform.scale(key_2, (100, 50))

key_3 = pygame.image.load("assets/images/Rooms/sleutel_3.png").convert_alpha()
key_3 = pygame.transform.scale(key_3, (100, 50))

key_1_silhoute = pygame.image.load("assets/images/Rooms/sleutel_1_silhoute.png").convert_alpha()
key_1_silhoute = pygame.transform.scale(key_1_silhoute, (100, 50))

key_2_silhoute = pygame.image.load("assets/images/Rooms/sleutel_2_silhoute.png").convert_alpha()
key_2_silhoute = pygame.transform.scale(key_2_silhoute, (100, 50))

key_3_silhoute = pygame.image.load("assets/images/Rooms/sleutel_3_silhoute.png").convert_alpha()
key_3_silhoute = pygame.transform.scale(key_3_silhoute, (100, 50))

class GameScreen:
    def __init__(self, player, settings_menu_screen):
        self.active = settings.in_room
        self.player = player
        self.settings_menu_screen = settings_menu_screen

    def update(self, screen, dt):
        screen.fill((0, 0, 0))
        if settings.start_menu:
            play_music_game.stop_music()
            
            correct_highscore = highscore.load_highscore()

            font_highscore = pygame.font.SysFont(None, 40)
            highscore_text = font_normal.render("HIGHSCORE", True, (255, 100, 0))
            highscore_text_rect = highscore_text.get_rect(center=(800 // 2 - 60, 400 // 2 + 100))
            highscore_number = font_highscore.render(f"{highscore.format_time(int(correct_highscore))}", True, (255, 100, 0))
            highscore_number_rect = highscore_number.get_rect(center=(800 // 2 + 65, 400 // 2 + 100))

            screen.blit(start_screen, (0, 0))
            screen.blit(start_text, start_text_rect)
            screen.blit(titel_text, titel_text.get_rect(center=(800 // 2, 100)))
            screen.blit(options_text, options_text_rect)
            screen.blit(highscore_text, highscore_text_rect)
            screen.blit(highscore_number, highscore_number_rect)

            play_music.play_music()
            return

        if not settings.in_room:
            # Herstart achtergrondmuziek NIET als het monster je net aan het pakken is!
            if not settings.scare and not settings.heartrate_scare:
                play_music.stop_music()
                play_music_game.play_music()
                
            if settings.current_mode != "hallway":
                came_from_room = (settings.current_mode == "room")

                settings.WIDTH = 800
                settings.HEIGHT = 400
                if screen.get_size() != (settings.WIDTH, settings.HEIGHT):
                    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
                    screen.fill((0, 0, 0))

                self.player.y = 155

                if came_from_room:
                    self.player.x = float(settings.HALLWAY_DOOR_X) - self.player.width / 2 + 80

                settings.current_mode = "hallway"
            else:
                moved = self.player.handle_input_side(dt)

                hallway.moving(screen, moved, self.player.x)
                monster.moving_monster(screen, moved, self.player.x, dt)
                self.player.draw_side(screen)

                if self.player.player_hitbox.colliderect(monster.monster_hitbox) and not settings.scare:
                    monster.jumpscare(screen)
            
            if settings.keys_collected[0]:
                screen.blit(key_1, (0, 10))
            else:
                screen.blit(key_1_silhoute, (0, 10))
            if settings.keys_collected[1]:
                screen.blit(key_2, (50, 10))
            else:
                screen.blit(key_2_silhoute, (50, 10))
            if settings.keys_collected[2]:
                screen.blit(key_3, (100, 10))
            else:
                screen.blit(key_3_silhoute, (100, 10))

        else:
            if settings.current_mode != "room":
                settings.WIDTH = 600
                settings.HEIGHT = 500
                if screen.get_size() != (settings.WIDTH, settings.HEIGHT):
                    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
                    screen.fill((0, 0, 0))

                settings.current_mode = "room"
                self.current_room_module = random.choice(rooms)
                settings.current_room_module_name = self.current_room_module.__name__
            else:
                screen.fill((0, 0, 0))
                self.current_room_module.draw_room(screen, dt)
                self.player.handle_input_top(screen, dt)
                self.player.draw_top(screen)
                
                monster.monster_x += monster.monster_speed * dt
                if monster.monster_x > settings.HALLWAY_DOOR_X and not settings.scare and not settings.scare_active:
                    settings.in_room = False  
                    monster.jumpscare(screen) 
                    
                if settings.scare_active:
                    play_music_game.stop_music()
                    jumpscare.scare(screen)
                    play_music_scare.play_music()
                elif not settings.scare and not settings.heartrate_scare:
                    play_music_scare.stop_music()
                    play_music_game.play_music()

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
                            pos = pygame.mouse.get_pos()
                            heartrate.meten(screen, dt)
                        if settings.opened_object == "doos" or settings.opened_object == "rolstoel":
                            pos = pygame.mouse.get_pos()
                            schakelaar.game(screen, dt, pos)

        if not settings.in_room and not settings.scare and not settings.heartrate_scare:
            font = pygame.font.SysFont(None, 24)
            time = settings.HIGHSCORE
            time_text = highscore.format_time(int(time))
            time_surface = font.render(f"Time: {time_text}", True, (255, 255, 255))
            screen.blit(time_surface, (settings.WIDTH - 250, 50))

        self.settings_menu_screen.draw(screen)

