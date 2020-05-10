class Apple:
    x = 0  # Posición Horizontal apple.
    y = 0  # Posición Vertical apple
    step = 44

    def __init__(self, x, y):
        self.x = x * self.step
        self.y = y * self.step

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))  # Dibujando la imagen de apple en la superficie.