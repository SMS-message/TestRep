import pygame

ALL_SPRITES = pygame.sprite.Group()


class Square(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.surface.Surface((100, 100))


def main() -> None:
    pygame.init()
    size = width, height = (1280, 720)
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    running = True

    Square()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("#121212")

        ALL_SPRITES.draw(screen)
        ALL_SPRITES.update()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
