import pygame
from random import *


def draw1(screen: pygame.display) -> None:
    screen.fill("#121212")
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, PyGame!", True, '#FFFFFF')
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, '#353535',
                     (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 1)


def draw_square(screen: pygame.display) -> None:
    color = pygame.Color('#303030')
    pygame.draw.rect(screen, color, (20, 20, 100, 100), 0)

    hsv = color.hsva

    color.hsva = (hsv[0], hsv[1], hsv[2] + 30, hsv[3] - 0.5)
    pygame.draw.rect(screen, color, (10, 10, 100, 100), 0)


def draw_pixels(screen: pygame.display) -> None:
    for _ in range(10000):
        screen.fill(pygame.Color('#353535'), (random() * width, random() * height, 10, 2))


if __name__ == '__main__':
    pygame.init()
    size = width, height = (800, 600)
    my_screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        draw1(my_screen)
        draw_pixels(my_screen)
        draw_square(my_screen)


        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
