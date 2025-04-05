INSERT INTO students (name, second_name, group_id) VALUES ('Mikalau', 'Papov', 4905);

INSERT INTO books (title, taken_by_student_id) VALUES ('The plan to defeat Thanos', 20076);

INSERT INTO books (title, taken_by_student_id)  VALUES ('How to shave a wolverine and stay alive', 20076);

INSERT INTO `groups` (title, start_date, end_date) VALUES ('Charles Xovier Group', 'Marth 25', 'Jul 25');

INSERT INTO subjets (title) VALUES ('psychology');

INSERT INTO subjets (title) VALUES ('philosophy');

INSERT INTO lessons (title, subject_id) VALUES ('reflection', 10049);

INSERT INTO lessons (title, subject_id) VALUES ('basic psychology', 10049);

INSERT INTO lessons (title, subject_id) VALUES ('the teachings of Socrates', 10050);

INSERT INTO lessons (title, subject_id) VALUES ('paradigms of philosophy', 10050);

INSERT INTO marks (value, lesson_id, student_id) VALUES (8, 9400, 20076);

INSERT INTO marks (value, lesson_id, student_id) VALUES (8, 9401, 20076);

INSERT INTO marks (value, lesson_id, student_id) VALUES (7, 9403, 20076);

INSERT INTO marks (value, lesson_id, student_id) VALUES (9, 9404, 20076);

SELECT value FROM marks WHERE student_id=20076;

SELECT title FROM books WHERE taken_by_student_id=20076;

SELECT * 
FROM `groups` g 
JOIN students s
ON g.id = s.group_id
JOIN marks m
ON s.id=m.student_id
JOIN lessons l
ON m.lesson_id =l.id
JOIN books b
ON m.student_id=b.taken_by_student_id
JOIN subjets sub
ON l.subject_id = sub.id
WHERE s.id=20076;

