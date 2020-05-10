import pygame
from random import randint
from apple import Apple
from snake import Snake

import time


class Game:
    '''
    Esta clase contiene la lógica general del juego.
    '''
    windowWidth = 800
    windowHeight = 600
    snake = 0
    apple = 0

    def __init__(self):
        self.running = True
        self.display_surf = None
        self.image_surf = None
        self.apple_surf = None
        self.snake = Snake(3)
        self.apple = Apple(5, 5)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('Snake Game')  # Establecer el título de la pantalla
        self._running = True
        self._image_surf = pygame.image.load("snake.png").convert()  # Carga de la superficie de imagen snake
        self._apple_surf = pygame.image.load("apple.png").convert()  # Carga de la superficie de imagen apple

    def isCollision(self, x1, y1, x2, y2, size):
        if x1 >= x2 and x1 <= x2 + size:  # Prueba si ocurre colisión en posiciones horizontales.
            if y1 >= y2 and y1 <= y2 + size:  # Prueba si ocurre colisión en posiciones verticales.
                return True
        return False

    def on_event(self, event):
        if pygame.event.type == QUIT:
            self._running = False  # Termina el juego

    def on_loop(self):
        self.snake.update()

        # Snake choca con  los bordes
        if self.snake.x[0] < 0 or self.snake.x[0] > self.windowWidth or self.snake.y[0] < 0 or self.snake.y[
            0] > self.windowHeight:
            print("GAME OVER!")
            exit(0)

        # Snake come Apple?
        for i in range(0, self.snake.length):
            if self.isCollision(self.apple.x, self.apple.y, self.snake.x[i], self.snake.y[i], 20):
                self.apple.x = randint(2, 9) * 44
                self.apple.y = randint(2, 9) * 44
                self.snake.length = self.snake.length + 1

        # Snake se come a ella?
        for i in range(2, self.snake.length):
            if self.isCollision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i], 20):
                print("GAME OVER!")
                exit(0)

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self.snake.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()  # Presionando las teclas

            if (keys[pygame.K_RIGHT]) and not self.snake.direction == 1:
                self.snake.moveRight()

            elif (keys[pygame.K_LEFT]) and not self.snake.direction == 0:
                self.snake.moveLeft()

            elif (keys[pygame.K_UP]) and not self.snake.direction == 3:
                self.snake.moveUp()

            elif (keys[pygame.K_DOWN]) and not self.snake.direction == 2:
                self.snake.moveDown()

            elif (keys[pygame.K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()

            time.sleep(50.0 / 1000.0);

        self.on_cleanup()
