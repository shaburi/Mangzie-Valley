import pygame
from settings import *


class HandBook:

    def __init__(self):
        self.offset = 50
        self.width = SCREEN_WIDTH / 4
        self.height = SCREEN_HEIGHT - 2 * self.offset
        self.rect = pygame.rect.Rect(SCREEN_WIDTH - self.width - self.offset, self.offset, self.width,
                                     self.height)
        self.bg_color = (249,216,167)
        self.seed = None
        self.title = None
        self.description = None
        self.icon = None

        font_path = '../font/LycheeSoda.ttf'
        self.title_font = pygame.font.Font(font_path, 40)
        self.font = pygame.font.Font(font_path, 20)
        self.text_color = (0, 0, 0)
        self.title = self.title_font.render('Testing', False, self.text_color)
        self.title_y = self.rect.y + 30
        self.description_pos = (self.rect.x + 15, self.title_y + 50)
        self.icon_pos = (self.rect.x+5, self.rect.bottom - TILE_SIZE - 5)

    def update(self, seed):
        self.seed = seed
        self.title = self.title_font.render(self.seed, False, self.text_color)
        description = SEED_DESCRIPTIONS[self.seed]
        self.description = Text(description, self.description_pos, font=self.font)
        self.icon = pygame.image.load(f'../graphics/plants/icons/{self.seed}.png')
        self.icon = pygame.transform.scale_by(self.icon, TILE_SIZE/self.icon.get_width())

    def draw(self, screen):
        # draw the background
        pygame.draw.rect(screen, self.bg_color, self.rect)
        pygame.draw.rect(screen, self.text_color, self.rect, width=3)

        # draw the title
        screen.blit(self.title, (self.rect.x + (self.width - self.title.get_width()) / 2, self.title_y))

        # draw the description
        self.description.draw(screen)

        # draw the icon
        screen.blit(self.icon, self.icon_pos)


class Text:

    def __init__(self, text, pos, font=None, text_color=(0, 0, 0)):
        self.text_color = text_color

        lines = text.splitlines()

        if font is None:
            self.font = pygame.font.SysFont(None, 12)
        else:
            self.font = font
        self.text_image = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.text_image.fill((255, 0, 255))
        self.text_image.set_colorkey((255, 0, 255))
        y = pos[1]
        x = pos[0]
        for i, l in enumerate(lines):
            line_image = self.font.render(l, False, self.text_color)
            self.text_image.blit(line_image, (x, y + i * line_image.get_height()))

    def draw(self, screen):
        # text
        screen.blit(self.text_image, (0, 0))
