from blob import Blob


# access attributes of the Blob class
def main():
    # create a blob
    blob = Blob("red", 100, 100)
    print(blob.size)
    print(blob.color)
    print(blob.x_boundary)
    print(blob.y_boundary)
    print(blob.x)
    print(blob.y)
    print(blob.move_x)
    print(blob.move_y)
    print(blob.check_bounds())
    print(blob.move())


if __name__ == "__main__":
    main()
