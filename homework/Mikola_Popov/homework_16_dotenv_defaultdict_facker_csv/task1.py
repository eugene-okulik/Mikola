import mysql.connector as mysql
import os
import dotenv
import csv


DIR_PATH = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(DIR_PATH))
path_eugene_hw_data = os.path.join(
    homework_path, "eugene_okulik", "Lesson_16", "hw_data", "data.csv"
)


dotenv.load_dotenv(override=True)

db = mysql.connect(
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
)

list_undiscovered = []


def func_for_in(lst, enter):
    for i in lst:
        if i["count(*)"] == 0:
            list_undiscovered.append(enter)


#  Checking by name
def func_check_by_db_name(variable, enter):
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        f"""
        SELECT count(*) FROM students WHERE {variable}=%s
    """,
        (enter,),
    )
    name_check = cursor.fetchall()
    func_for_in(name_check, enter)


with open(path_eugene_hw_data, newline="") as eugene_file:
    data = {}
    row_one = next(eugene_file)
    data_eugene_csv = csv.reader(eugene_file)
    for num, row_1 in enumerate(row_one.split(",")):
        for row_2 in data_eugene_csv:
            (
                name,
                second_name,
                group_title,
                book_title,
                subject_title,
                lesson_title,
                mark_value,
            ) = row_2
            func_check_by_db_name(row_1, name)
            func_check_by_db_name(row_1, second_name)
            func_check_by_db_name(row_1, group_title)
            func_check_by_db_name(row_1, book_title)
            func_check_by_db_name(row_1, subject_title)
            func_check_by_db_name(row_1, lesson_title)
            func_check_by_db_name(row_1, mark_value)
    print(list_undiscovered)
