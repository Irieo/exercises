import pygame
import random
import math
from blob_cop import Blob

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 5
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


def draw_environment(blob_list):
    game_display.fill(WHITE)

    for blob_dict in blob_list:
        for blob_id in list(blob_dict.keys()):
            if blob_id in blob_dict:
                blob = blob_dict[blob_id]
                pygame.draw.circle(
                    game_display, blob.color, [blob.x, blob.y], blob.size
                )
                blob.move()
                blob.check_bounds()

                # Check for collisions with other blobs
                for other_blob_dict in blob_list:
                    for other_blob_id in list(other_blob_dict.keys()):
                        if blob_id != other_blob_id:
                            if other_blob_id in other_blob_dict:
                                other_blob = other_blob_dict[other_blob_id]
                                if blob.collides_with(other_blob):
                                    # Create new blobs of 80% size with random trajectories
                                    new_blob1 = Blob(
                                        blob.color,
                                        blob.x_boundary,
                                        blob.y_boundary,
                                        size_range=(
                                            int(blob.size * 0.8),
                                            int(blob.size * 0.8) + 1,
                                        ),
                                    )
                                    new_blob1.x = blob.x
                                    new_blob1.y = blob.y
                                    new_blob1.move_x = random.uniform(-1, 1)
                                    new_blob1.move_y = random.uniform(-1, 1)

                                    new_blob2 = Blob(
                                        blob.color,
                                        blob.x_boundary,
                                        blob.y_boundary,
                                        size_range=(
                                            int(other_blob.size * 0.8),
                                            int(other_blob.size * 0.8) + 1,
                                        ),
                                    )
                                    new_blob2.x = other_blob.x
                                    new_blob2.y = other_blob.y
                                    new_blob2.move_x = random.uniform(-1, 1)
                                    new_blob2.move_y = random.uniform(-1, 1)

                                    # Remove colliding blobs and add new blobs to the list
                                    if blob_id in blob_dict:
                                        del blob_dict[blob_id]
                                    if other_blob_id in other_blob_dict:
                                        del other_blob_dict[other_blob_id]
                                    blob_dict[new_blob1.id] = new_blob1
                                    other_blob_dict[new_blob2.id] = new_blob2

    pygame.display.update()


def main():
    blue_blobs = dict(
        enumerate([Blob(BLUE, WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)])
    )
    red_blobs = dict(
        enumerate(
            [
                Blob(RED, WIDTH, HEIGHT, size_range=(5, 15))
                for i in range(STARTING_RED_BLOBS)
            ]
        )
    )
    print(blue_blobs)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([blue_blobs, red_blobs])
        clock.tick(100)


if __name__ == "__main__":
    main()
