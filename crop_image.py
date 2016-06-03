import sys
from os import path
from PIL import Image


def add_metadata(output_image, metadata):
    print("something")


def crop_image(image_path):
    with Image.open(image_path) as input_image:
        width, height = input_image.size
        output_image = input_image.crop((0, 0, width/2, height))
    return output_image


def print_help():
    print("--help, -h                                               Prints this information")
    print("--add, -a <input image> <output image> <metadata file>   Adds metadata to image")
    print("--extract, -e <input image> <output metadata file>       Extracts metadata from image")


def main():
    if len(sys.argv) != 3 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print_help()
        sys.exit(1)
    if not path.exists(sys.argv[1]):
        raise FileExistsError("File %s does not exists" % sys.argv[1])
    output_image = crop_image(sys.argv[1])
    output_image.save(sys.argv[2])


if __name__ == "__main__":
    main()
