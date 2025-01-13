import os
import sys
import pygame

pygame.init()
size = width, height = (789, 600)
screen = pygame.display.set_mode(size)
ALL_SPRITES = pygame.sprite.Group()
HORIZONTAL_BORDERS = pygame.sprite.Group()
VERTICAL_BORDERS = pygame.sprite.Group()


def main() -> None:
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Landing(event.pos)
        screen.fill("#121212")

        ALL_SPRITES.draw(screen)
        ALL_SPRITES.update()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


def load_image(name, colorkey=None) -> pygame.surface.Surface:
    fullname = os.path.join('img', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    print('Изображение загружено!')
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    print('Изображение вернул!')
    return image


class Mountain(pygame.sprite.Sprite):
    image = load_image("mountains.png")

    def __init__(self, size: tuple[int, int]):
        super().__init__(ALL_SPRITES)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = size[1]


class Landing(pygame.sprite.Sprite):
    image = load_image("pt.png")

    def __init__(self, pos):
        super().__init__(ALL_SPRITES)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)


if __name__ == '__main__':
    mountain = Mountain(size)
    main()
