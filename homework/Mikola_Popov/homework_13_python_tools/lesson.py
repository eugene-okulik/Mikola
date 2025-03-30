import os


print(os.path.dirname(__file__))
DIR_PATH = os.path.dirname(__file__)
DIR_FILE = os.path.join(DIR_PATH, "data.txt")


def read_files():
    with open(DIR_FILE, "r") as file:
        for line in file.readlines():
            yield line


for data_line in read_files():
    with open(os.path.join(DIR_PATH, "data_2.txt"), "a") as file_2:
        data_line = data_line.replace(",", "").replace(".", "")
        file_2.write(data_line)
