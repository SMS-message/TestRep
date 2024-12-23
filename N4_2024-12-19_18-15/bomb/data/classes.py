import pygame
from random import randrange
from data.functions import load_image


class Bomb(pygame.sprite.Sprite):
    def __init__(self, group: pygame.sprite.Group, width: int, height: int):
        super().__init__(group)

        self.image = load_image('bomb.png')

        self.rect = self.image.get_rect()
        self.rect.x = randrange(width - 120)
        self.rect.y = randrange(height - 114)

    def update(self, *args, **kwargs):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(args[0].pos):
                self.image = load_image('boom.png')
