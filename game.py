import pygame
import heartrate
import settings
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

class GameScreen:
    def __init__(self, player, settings_menu_screen):
        self.active = settings.in_room
        self.player = player
        self.settings_menu_screen = settings_menu_screen

    def update(self, screen, dt):
        screen.fill((0, 0, 0))
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
                # Room randomizer:
                #room_1_file, room_2_file, room_3_file
                self.current_room_module = random.choice([room_2_file])
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
                            kluis.open_kluis(screen, pos)
                        elif settings.opened_object in ("bed", "doos"):
                            paper_code.open_paper(screen)
                    elif rm == "room_2_file":
                        if settings.opened_object == "electrisiteitskast":
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            elektriciteitskast.meterkast(screen, mouse_x, mouse_y)
                        elif settings.opened_object in ("bed", "doos"):
                            gereedschap = pygame.image.load("assets/images/Rooms/elektriciteit/gereedschap.png")
                            gereedschap = pygame.transform.scale(gereedschap, (600, 500))
                            screen.blit(gereedschap, (0, 0))
                            settings.gereedschap_got = True
                    elif rm == "room_3_file":
                        if settings.opened_object == "bed":
                            heartrate.meten(screen, dt)

        self.settings_menu_screen.draw(screen)

