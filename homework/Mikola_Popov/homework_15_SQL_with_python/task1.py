import mysql.connector as mysql

db = mysql.connect(
    username="st-onl",
    password="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st-onl",
)

cursor = db.cursor(dictionary=True)

name = input("Enter student name - ")  # Alexandar
second_name = input("Enter student second_name - ")  # Orlov
cursor.execute(
    """
    INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, NULL);
    """,
    (name, second_name),
)
db.commit()

pk_student = cursor.lastrowid

#  one book: Lions of Eldorado, two book: Far Galaxy
one_book, two_book = input("one book: "), input("two book: ")
cursor.executemany(
    """
    INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s);
    """,
    [(one_book, pk_student), (two_book, pk_student)],
)
db.commit()

#  created groups
title = input("title group: ")
start_date = input("start date: ")
end_date = input("end date: ")
cursor.execute(
    """
    INSERT INTO`groups`(title, start_date, end_date) VALUES (%s, %s, %s)""",
    (title, start_date, end_date),
)
db.commit()

group_id = cursor.lastrowid
print(group_id)

#  add student to group
cursor.execute(
    """
    UPDATE students SET group_id=%s WHERE id=%s
""",
    (group_id, pk_student),
)
db.commit()

#  add a couple of subjets
title_one = input("title subjet one: ")  # Mathematics
title_two = input("title subjet two: ")  # English
cursor.execute(
    """
    INSERT INTO subjets (title) VALUES (%s)
""",
    (title_one,),
)
db.commit()
subjet_one_math = cursor.lastrowid

cursor.execute(
    """
    INSERT INTO subjets (title) VALUES (%s)
""",
    (title_two,),
)
db.commit()
subjet_two_eng = cursor.lastrowid

#  we create classes by subject
cursor.execute(
    """
    INSERT INTO lessons (title, subject_id) VALUES (%s, %s);
""",
    ("algebra", subjet_one_math),
)
db.commit()
lesson_algebra_id = cursor.lastrowid

cursor.execute(
    """
    INSERT INTO lessons (title, subject_id) VALUES (%s, %s);
""",
    ("geometry", subjet_one_math),
)
db.commit()
lesson_geometry_id = cursor.lastrowid

cursor.execute(
    """
    INSERT INTO lessons (title, subject_id) VALUES (%s, %s);
""",
    ("grammar", subjet_two_eng),
)
db.commit()
lesson_grammar_id = cursor.lastrowid

cursor.execute(
    """
    INSERT INTO lessons (title, subject_id) VALUES (%s, %s);
""",
    ("learning words by heart", subjet_two_eng),
)
db.commit()
lesson_words_id = cursor.lastrowid

#  Rating

cursor.executemany(
    """
    INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)
""",
    [
        (6, lesson_algebra_id, pk_student),
        (9, lesson_geometry_id, pk_student),
        (5, lesson_grammar_id, pk_student),
        (8, lesson_words_id, pk_student),
    ],
)
db.commit()

# Этот поиск я сделал просто для проверки запросов,
# необращайте на него внимания.
cursor.execute(
    """
    SELECT id FROM students WHERE name='Alexandar' and second_name='Orlov'
"""
)
student = cursor.fetchone()
pk_student = student["id"]
print(pk_student)

cursor.execute(
    """
    SELECT * FROM students WHERE id=%s
""",
    (pk_student,),
)
print(cursor.fetchall())

cursor.execute(
    """
    SELECT title FROM books WHERE taken_by_student_id=%s
""",
    (pk_student,),
)
print(cursor.fetchall())

cursor.execute(
    """
    SELECT * FROM `groups` g JOIN students s
    ON g.id = s.group_id
    JOIN marks m
    ON s.id=m.student_id
    JOIN lessons l
    ON m.lesson_id =l.id
    JOIN books b
    ON m.student_id=b.taken_by_student_id
    JOIN subjets sub
    ON l.subject_id = sub.id
    WHERE s.id=%s
""",
    (pk_student,),
)
print(cursor.fetchall())

db.close()
