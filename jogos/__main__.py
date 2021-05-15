import pygame
import pygame_gui

FPS = 40
SCREEN_SIZE = (400, 400)

WHITE = (255, 255, 255)


def update(surface, manager, clock):
    """Atualizar o jogo"""
    time_delta = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        manager.process_events(event)

    manager.update(time_delta)

    surface.fill(WHITE)
    manager.draw_ui(surface)
    pygame.display.update()
    pygame.display.flip()

    return True


def main():
    """Criar e roda um jogo"""
    pygame.init()
    surface = pygame.display.set_mode(SCREEN_SIZE)
    manager = pygame_gui.UIManager(SCREEN_SIZE)
    clock = pygame.time.Clock()
    running = True

    while running:
        running = update(surface, manager, clock)


if __name__ == '__main__':
    main()
