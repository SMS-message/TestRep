import pygame

from data.classes import Bomb


def main() -> int:
    pygame.init()
    size = width, height = (500, 500)
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()
    for _ in range(20):
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


if __name__ == '__main__':
    main()
