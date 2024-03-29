import random


class Blob:
    def __init__(self, color, x_boundary, y_boundary, size_range=(4, 10)):
        self.size = random.randrange(size_range[0], size_range[1])
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)

    def move(self):
        self.move_x = random.randrange(-2, 3)
        self.move_y = random.randrange(-2, 3)
        self.x += self.move_x
        self.y += self.move_y

    def check_bounds(self):
        if self.x < 0:
            self.x = 0
        elif self.x > self.x_boundary:
            self.x = self.x_boundary

        if self.y < 0:
            self.y = 0
        elif self.y > self.x_boundary:
            self.y = self.x_boundary
