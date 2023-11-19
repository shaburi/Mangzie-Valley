import pygame, sys
from settings import *
from level import Level
from tutorial import Tutorial
from pause_screen import PauseScreen
from mainmenu import MainMenu


class Game:
    def __init__(self, game_state='main_menu'):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Mangzie Valley')
        self.clock = pygame.time.Clock()

        self.level = Level(self.pause)
        self.tutorial = Tutorial(self.pause, self.start_game)
        self.pause_screen = PauseScreen(self.unpause, quit_game)
        self.main_menu = MainMenu(self.start_game, quit_game)

        self.game_state = game_state
        self.previous_game_state = self.game_state

        # music
        pygame.mixer.music.load('../audio/music.mp3')
        pygame.mixer.music.set_volume(VOLUME)

    def start_game(self, name, game_mode):
        self.level.player.get_name(name)
        self.game_state = game_mode
        pygame.mixer.music.stop()
        pygame.mixer.music.play(loops=-1)

    def unpause(self):

        self.game_state = self.previous_game_state
        pygame.mixer.music.unpause()

    def pause(self):
        black_filter = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        black_filter.fill((0, 0, 0))
        black_filter.set_alpha(230)

        self.screen.blit(black_filter, (0, 0))
        paused_background = self.screen.copy()
        self.pause_screen.bg = paused_background

        pygame.display.flip()

        self.previous_game_state = self.game_state
        self.game_state = 'paused'
        pygame.mixer.music.pause()

    def toggle_pause(self):
        if self.game_state == 'paused':
            self.unpause()
        elif self.game_state != 'main_menu':
            self.pause()

    def run(self):

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.level.shop_active:
                            self.level.toggle_shop()
                        else:
                            self.toggle_pause()

                    if event.key == pygame.K_u:
                        self.level.toggle_handbook()

            dt = self.clock.tick() / 1000
            if self.game_state == 'level':
                self.level.run(dt)
            elif self.game_state == 'paused':
                self.pause_screen.run()
            elif self.game_state == 'tutorial':
                self.tutorial.run(dt)
            elif self.game_state == 'main_menu':
                self.main_menu.run(events)
            pygame.display.update()


def quit_game():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    game = Game(game_state='main_menu')
    game.run()
