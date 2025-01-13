import pygame
import os as potatos
import sys as sus
from random import randint, randrange

ALL_SPRITES = pygame.sprite.Group()
HORIZONTAL_BORDERS = pygame.sprite.Group()
VERTICAL_BORDERS = pygame.sprite.Group()


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(ALL_SPRITES)
        if x1 == x2:  # вертикальная стенка
            self.add(VERTICAL_BORDERS)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(HORIZONTAL_BORDERS)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(ALL_SPRITES)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        while 1:
            self.vx = randint(-25, 25)
            self.vy = randrange(-5, 25)
            if self.vx and self.vy:
                break

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, HORIZONTAL_BORDERS):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, VERTICAL_BORDERS):
            self.vx = -self.vx


def load_image(name: str, color_key: None | int = None) -> pygame.surface.Surface:
    fullname = potatos.path.join('img', name)
    if not potatos.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не найден.')
        sus.exit(1)
    image = pygame.image.load(fullname)
    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((1, 1))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()

    return image


def main() -> int:
    pygame.init()
    size = width, height = (1280, 720)
    screen = pygame.display.set_mode(size)

    for _ in range(50):
        Ball(20, 400, 400)

    Border(5, 5, width - 5, 5)
    Border(5, height - 5, width - 5, height - 5)
    Border(5, 5, 5, height - 5)
    Border(width - 5, 5, width - 5, height - 5)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ALL_SPRITES.update(event)
        screen.fill("#121212")

        ALL_SPRITES.draw(screen)
        ALL_SPRITES.update()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    return 0


if __name__ == '__main__':
    main()
