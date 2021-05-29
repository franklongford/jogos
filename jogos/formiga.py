import pygame
import pygame_gui
from pygame.transform import rotate
from pygame.sprite import Sprite, Group
from pygame.math import Vector2
from pygame_gui.elements import UIButton

from jogos.imagens import get_image

# Aqui precisamos chamar init pra instalar fonte de texto pra os butoes
pygame.init()

SCREEN_SIZE = (300, 400)
MAP_SIZE = (300, 320)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60


class Ant(Sprite):

    def __init__(self, size=(25, 25), speed=(2, 2)):
        # Call the parent class (Sprite) constructor
        super(Ant, self).__init__()

        # Load an image of the ant
        self.image = get_image("ant_worker.png")
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(*size)
        self.rect.update(0, 0, *self.rect.size)
        self.vector = Vector2(speed)

    @property
    def direction(self):
        return self.vector.normalize()

    def reverse(self):
        self.vector = self.vector.reflect(self.vector)

    def speed_up(self):
        self.vector *= 1.5

    def slow_down(self):
        self.vector *= 0.5

    def update(self):
        self.rect.move_ip(self.vector)

        if self.rect.left < 0 or self.rect.right > MAP_SIZE[0]:
            self.vector = self.vector.reflect((1, 0))

        if self.rect.top < 0 or self.rect.bottom > MAP_SIZE[1]:
            self.vector = self.vector.reflect((0, 1))

    def draw(self, surface):
        angle = self.vector.angle_to(Vector2(0, -1))
        surface.blit(rotate(self.image, angle), self.rect)


def main():

    # Cria uma janela grafica usando as configuracoes do
    # computador
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Cria um UIManager do Pygame GUI pra controlar procesando
    # os eventos do jogo
    manager = pygame_gui.UIManager(SCREEN_SIZE)

    # Cira os butoes do jogo
    flip_button = UIButton(
        relative_rect=pygame.Rect((0, 320), (100, 80)),
        text='Flip it!',
        manager=manager
    )
    speed_button = UIButton(
        relative_rect=pygame.Rect((100, 320), (100, 80)),
        text='Speed up!',
        manager=manager
    )
    slow_button = UIButton(
        relative_rect=pygame.Rect((200, 320), (100, 80)),
        text='Slow down!',
        manager=manager
    )

    # Cria a formiga
    ant = Ant()

    clock = pygame.time.Clock()
    running = True

    while running:

        time_delta = clock.tick(FPS) / 1000.0

        # Reagir aos eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == flip_button:
                        ant.reverse()
                    elif event.ui_element == speed_button:
                        ant.speed_up()
                    elif event.ui_element == slow_button:
                        ant.slow_down()

            manager.process_events(event)

        # Atualiza os objetos do jogo
        manager.update(time_delta)
        ant.update()

        # Atualiza a janela do jogo
        screen.fill(WHITE)
        ant.draw(screen)
        manager.draw_ui(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
