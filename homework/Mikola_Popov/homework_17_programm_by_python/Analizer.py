import os
import argparse

DIR_PATH = os.path.dirname(__file__)
HOME_PATH = os.path.dirname(os.path.dirname(DIR_PATH))

parser = argparse.ArgumentParser(prog="Analizer")
parser.add_argument("--file_path", help="Enter full path: ", type=str)
parser.add_argument("-ts", "--text_search", help="text for search", type=str)
args = parser.parse_args()
lines = args.file_path.split("/")
search_text = args.text_search


# eugene_okulik/data/logs/rpe-api-error.2022-02-03.0.log


def full_file_path_logs(path):
    path_file_logs = os.path.join(path, "/".join(lines))
    lst = []
    for root, dirs, files in os.walk(path_file_logs):
        for file in files:
            file = os.path.join(root, file)
            lst.append(file)
    return lst


def search_logs_text(text):
    for file in full_file_path_logs(HOME_PATH):
        try:
            with open(file, "r") as file_log:
                new_file_log = file_log.readline()
                for num, line in enumerate(new_file_log.split(), start=1):
                    if text in line:
                        words = line.split()
                        for i, word in enumerate(words):
                            if text in word:
                                start_i = max(0, i - 5)
                                end_i = min(len(words), i + 6)
                                new_text = words[start_i:end_i]
                                print(
                                    f"Найден текст: {text},"
                                    f" в файле {file},"
                                    f" строка {num}: {new_text}"
                                )
        except FileNotFoundError:
            print(f"Файл {text} ненайден")


search_logs_text(search_text)
