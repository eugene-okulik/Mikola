import os
import argparse


parser = argparse.ArgumentParser(prog="Analizer")
parser.add_argument("--file_path", help="Enter full path: ", type=str)
parser.add_argument("-ts", "--text_search", help="text for search", type=str)
args = parser.parse_args()
lines = args.file_path
search_text = args.text_search


def full_file_path_logs():
    lst = []
    for root, dirs, files in os.walk(lines):
        for file in files:
            file = os.path.join(root, file)
            lst.append(file)
    return lst


def search_logs_text(text):
    for file in full_file_path_logs():
        try:
            with open(file, "r") as file_log:
                new_file_log = [file.split() for file in file_log.readlines()]
                for num, word in enumerate(new_file_log):
                    if text in word:
                        index_w = word.index(text)
                        new_text = word[0:index_w] + word[index_w:index_w + 6]
                        print(
                            f"Найден текст: {text},"
                            f" в файле {file},"
                            f" строка {num}: {new_text}"
                        )
        except FileNotFoundError:
            print(f"Файл {text} ненайден")


search_logs_text(search_text)
