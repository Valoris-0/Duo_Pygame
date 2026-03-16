import pygame
import settings
import hallway
import monster
import room
import jumpscare
import kluis
import paper_code


class GameScreen:
    def __init__(self, player, settings_menu_screen):
        self.active = settings.in_room
        self.player = player
        self.settings_menu_screen = settings_menu_screen

    def update(self, screen, dt):
        if not settings.in_room:
            if settings.current_mode != "hallway":
                came_from_room = (settings.current_mode == "room")

                settings.WIDTH = 800
                settings.HEIGHT = 400
                if screen.get_size() != (settings.WIDTH, settings.HEIGHT):
                    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

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
                # entering room: change size if needed
                settings.WIDTH = 600
                settings.HEIGHT = 500
                if screen.get_size() != (settings.WIDTH, settings.HEIGHT):
                    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

                settings.current_mode = "room"
            else:
                screen.fill((0, 0, 0))
                room.draw_room(screen)
                self.player.handle_input_top(screen, dt)
                self.player.update()
                self.player.draw_top(screen)

                if settings.scare_active:
                    jumpscare.scare(screen)

                if settings.solving:
                    if settings.opened_object == "kluis":
                        pos = pygame.mouse.get_pos()
                        kluis.open_kluis(screen, pos)
                    elif settings.opened_object in ("bed", "doos"):
                        paper_code.open_paper(screen)

        self.settings_menu_screen.draw(screen)

        return screen
