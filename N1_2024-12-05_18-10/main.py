import pygame


def main() -> None:
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("#121212")

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()  # Example file showing a basic pygame "game loop"
