class Snake:
    '''
        Esta clase contiene la información de Snake.
        Sanke tiene una lista en x e y que contiene la información del cuerpo.
    '''

    x = [0]  # Posiciones horizontales del cuerpo de Snake.
    y = [0]  # Posiciones verticales del cuerpo de Snake.
    step = 44
    direction = 0
    length = 3

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
        self.length = length
        for i in range(0, 2000):
            self.x.append(-100)
            self.y.append(-100)

        # Posiciones iniciales de Snake.
        self.x[1] = 1 * 44
        self.x[2] = 2 * 44

    def update(self):
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            # Actualizar puestos anteriores.
            for i in range(self.length - 1, 0, -1):
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1]

            # Actualizar posición de la cabeza de Snake.
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0

    def moveRight(self):
        self.direction = 0  # Movimiento de Snake a la derecha.

    def moveLeft(self):
        self.direction = 1  # Movimiento de Snake a la izquierda.

    def moveUp(self):
        self.direction = 2  # Movimiento de Snake hacia arriba.

    def moveDown(self):
        self.direction = 3  # Movimiento de Snake hacia abajo,

    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))  # Dibujar las imágenes en la superficie.