import random
import math
import uuid


class Blob:
    def __init__(self, color, x_boundary, y_boundary, size_range=(20, 21)):
        self.size = random.randrange(size_range[0], size_range[1])
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)
        self.move_x = random.uniform(-1, 1)
        self.move_y = random.uniform(-1, 1)
        self.collisions = 0
        self.id = uuid.uuid4()

    def move(self):
        self.x += self.move_x
        self.y += self.move_y
        self.check_bounds()

    def collides_with(self, other_blob):
        distance = math.sqrt(
            (self.x - other_blob.x) ** 2 + (self.y - other_blob.y) ** 2
        )
        return distance < (self.size + other_blob.size) * 0.9

    def check_bounds(self):
        if self.x < 0:
            self.x = 0
            self.move_x *= -1
        elif self.x > self.x_boundary:
            self.x = self.x_boundary
            self.move_x *= -1
        if self.y < 0:
            self.y = 0
            self.move_y *= -1
        elif self.y > self.y_boundary:
            self.y = self.y_boundary
            self.move_y *= -1
