import os
from sys import argv


def get_files(directory):
    files = []
    for entry in os.scandir(directory):
        if entry.path.endswith(".csv") and entry.is_file():
            files.append(entry.path)
    return files


# This adds the location and name of the original file a the end of each line
def finalise_line(line, filename):
    return line.strip("\n") + "," + filename + "\n"


def get_file_content(input_file, is_first_file):
    with open(input_file) as file:
        data = file.readlines()
        if is_first_file:
            return data
        else:
            del data[0]
            return data


def is_output_file_empty(output_file):
    is_empty = False
    try:
        if os.stat(output_file).st_size == 0:
            is_empty = True
    except FileNotFoundError:
        is_empty = True
    return is_empty


def add_lines(directory, output_file):
    files = get_files(directory)
    with open(output_file, "a") as file:
        for filename in files:
            is_empty = is_output_file_empty(output_file)
            for line in get_file_content(filename, is_empty):
                file.write(finalise_line(line, filename))


def main():
    add_lines(argv[1], argv[2])


if __name__ == "__main__":
    main()
