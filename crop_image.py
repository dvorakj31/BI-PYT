import sys
from os import path
from PIL import Image


def crop_image(image_path):
    input_image = Image.open(image_path)
    coordinates = (10, 20, 10 + 60, 20 + 50)
    output_image = input_image.crop(coordinates)
    return output_image

def print_help():
    print("usage: <input image> <output_image>")


def main():
    if len(sys.argv) != 3:
        print_help()
        sys.exit(1)
    if not path.exists(sys.argv[1]):
        raise FileExistsError("File %s does not exists" % sys.argv[1])
    output_image = crop_image(sys.argv[1])
    output_image.save(sys.argv[2])


if __name__ == "__main__":
    main()
