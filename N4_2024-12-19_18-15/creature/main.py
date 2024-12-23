import pygame
from data.functions import load_image


def main() -> int:
    pygame.init()
    size = width, height = (300, 300)
    screen = pygame.display.set_mode(size)

    image = load_image('creature.png', -1)
    creature_pos = [0, 0]

    screen.fill("#121212")
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("#121212")
        screen.blit(image, creature_pos)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            creature_pos[1] -= 10
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            creature_pos[1] += 10
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            creature_pos[0] += 10
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            creature_pos[0] -= 10

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    return 0


if __name__ == '__main__':
    main()
