import os

output_folder = os.path.join(os.pardir, 'outputs')


def write_file(filename, binary=False):
    file_path = os.path.join(output_folder, filename)
    if binary:
        return open(file_path, "wb")
    return open(file_path, "w")


def append_file(filename, binary=False):
    file_path = os.path.join(output_folder, filename)
    if binary:
        return open(file_path, "ab")
    return open(file_path, "a")


def read_file(filename, binary=False):
    file_path = os.path.join(output_folder, filename)
    if binary:
        return open(file_path, "rb")
    return open(file_path, "r")
