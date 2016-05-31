import sys
from os import path


def print_help():
    print("usage: <input image> <output_image>")


def main():
    if len(sys.argv) != 3:
        print_help()
        sys.exit(1)
    if not path.exists(sys.argv[1]):
        raise FileExistsError("File %s does not exists" % sys.argv[1])


if __name__ == "__main__":
    main()
