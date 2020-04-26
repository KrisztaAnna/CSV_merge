import os
from sys import argv


def get_files(directory):
    for entry in os.scandir(directory):
        if entry.path.endswith(".csv") and entry.is_file():
            print(entry.path)


def get_file_content(filename):
    with open(filename) as file:
        data = file.readlines()
        del data[0]
        return data


def main():
    get_files(argv[1])


if __name__ == "__main__":
    main()
