import sys
import pygame
import os
from random import randrange


class Bomb(pygame.sprite.Sprite):
    def __init__(self, group: pygame.sprite.Group, width: int, height: int):
        super().__init__(group)

        self.image = load_image('bomb.png')

        self.rect = self.image.get_rect()
        self.rect.x = randrange(width)
        self.rect.y = randrange(height)

    def update(self, *args, **kwargs):
        self.rect = self.rect.move(randrange(3) - 1,
                                   randrange(3) - 1)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(args[0].pos):
                self.image = load_image('boom.png')


def main() -> int:
    pygame.init()
    size = width, height = (1280, 720)
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()
    for _ in range(100):
        Bomb(all_sprites, width, height)

    screen.fill("#121212")
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)

        screen.fill("#121212")
        all_sprites.draw(screen)
        all_sprites.update()

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    return 0


def load_image(name: str, color_key: None | int = None) -> pygame.surface.Surface:
    fullname = os.path.join('img', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не найден.')
        sys.exit(1)
    image = pygame.image.load(fullname)
    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((1, 1))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()

    return image


if __name__ == '__main__':
    main()
