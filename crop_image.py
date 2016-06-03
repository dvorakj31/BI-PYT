#!/usr/bin/env python3

import sys
from os import path
from PIL import Image


def add_metadata(output_image, metadata):
    meta = []
    with open(metadata, 'rb') as input_metadata:
        for byte in input_metadata:
            meta.append(byte)
    with open(output_image, 'ab') as output:
        output.write(b'\0')
        for byte in meta:
            output.write(byte)


def crop_image(image_path):
    with Image.open(image_path) as input_image:
        width, height = input_image.size
        output_image = input_image.crop((0, 0, width//2, height))
    return output_image


def print_help():
    print("--help, -h                                                     Prints this information")
    print("--add, -a <input image> <output image> <input metadata file>   Adds metadata to image")
    print("--extract, -e <input image> <output metadata file>             Extracts metadata from image")


def main():
    if len(sys.argv) <= 3 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print_help()
        sys.exit(1)
    if not path.exists(sys.argv[2]):
        raise FileExistsError("File %s does not exists" % sys.argv[2])
    if sys.argv[1] == "--add" or sys.argv[1] == "-a":
        if len(sys.argv) != 5:
            print_help()
        if not path.exists(sys.argv[4]):
            raise FileExistsError("File %s does not exists" % sys.argv[4])
        output_image = crop_image(sys.argv[2])
        output_image.save(sys.argv[3])
        add_metadata(sys.argv[3], sys.argv[4])


if __name__ == "__main__":
    main()
