import os
import datetime
import re


DIR_PATH = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(DIR_PATH))
eugene_file_path = os.path.join(
    homework_path, "eugene_okulik", "hw_13", "data.txt"
)
print(eugene_file_path)

with open(eugene_file_path) as Eugene_file:
    new_file = Eugene_file.readlines()
    count = 1
    for date_line in new_file:
        if int(date_line[:1]) == 1:
            date = re.findall(
                r'\d{4}-\d{2}-\d{2} \d{2}:\d+:\d+.\d+', date_line)[0]
            date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
            print(f"{1}. {date + datetime.timedelta(weeks=1)} - {date}")
        elif int(date_line[:1]) == 2:
            date1 = re.findall(
                r"\d{4}-\d{2}-\d{2} \d{2}:\d+:\d+.\d+", date_line)[0]
            date1 = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S.%f")
            print(f'{2}. {date1} - {date1.strftime("%B")}')
        elif int(date_line[:1]) == 3:
            date2 = re.findall(
                r"\d{4}-\d{2}-\d{2} \d{2}:\d+:\d+.\d+", date_line)[0]
            date2 = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S.%f")
            date_now = datetime.datetime.now()
            print(f"{3}. {date2} - {date_now - date2}")
