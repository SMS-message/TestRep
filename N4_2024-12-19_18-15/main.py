import sys
import pygame
import os


def main() -> int:
    pygame.init()
    size = width, height = (1280, 720)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    screen.fill("#121212")
    img = load_image('robot.png', -1)

    robot = load_image('robot.png', -1)
    img1 = pygame.transform.scale(robot, (500, 100))
    screen.blit(img1, (100, 200))
    img2 = pygame.transform.scale(robot, (100, 500))
    screen.blit(img2, (400, 200))
    img3 = pygame.transform.scale(robot, (500, 500))
    screen.blit(img3, (700, 200))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 4, 5):
                    screen.blit(img, event.pos)
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
