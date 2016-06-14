#!/usr/bin/env python3

import sys
from os import path
from PIL import Image


def extract_metadata(input_image, output_file):
    with open(input_image, 'rb') as input_file:
        arr = 0
        for line in input_file:
            position = line.find(b"\xff\xd9\x00")
            if position != -1:
                tmp = line.split(b"\xff\xd9\x00")
                arr = tmp[1:]
                break
        with open(output_file, 'wb') as ofile:
            for x in arr:
                ofile.write(x)
            for line in input_file:
                ofile.write(line)


def add_metadata(output_image, metadata):
    with open(output_image, 'ab') as output:
        with open(metadata, 'rb') as input_metadata:
            output.write(b"\x00")
            for line in input_metadata:
                output.write(line)
            output.write(b"\x00")


def crop_image(image_path):
    with Image.open(image_path) as input_image:
        width, height = input_image.size
        output_image = input_image.crop((0, 0, width//2, height))
    return output_image


def print_help():
    print("usage: %s [option] [files]" % sys.argv[0])
    print("--help, -h                                                     Print this information")
    print("--add, -a <input image> <output image> <input metadata file>   Add metadata to image")
    print("--extract, -e <input image> <output metadata file>             Extract metadata from image")


def main():
    if len(sys.argv) <= 3 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print_help()
        sys.exit(1)
    if not path.exists(sys.argv[2]):
        raise FileNotFoundError("File %s does not exists" % sys.argv[2])
    if sys.argv[1] == "--add" or sys.argv[1] == "-a":
        if len(sys.argv) != 5:
            print_help()
            sys.exit(2)
        if not path.exists(sys.argv[4]):
            raise FileNotFoundError("File %s does not exists" % sys.argv[4])
        output_image = crop_image(sys.argv[2])
        output_image.save(sys.argv[3])
        add_metadata(sys.argv[3], sys.argv[4])
    elif sys.argv[1] == "--extract" or sys.argv[1] == "-e":
        if len(sys.argv) != 4:
            print_help()
            sys.exit(2)
        extract_metadata(sys.argv[2], sys.argv[3])
    else:
        print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
