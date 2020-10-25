import sqlite3
import csv

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


def create_database():
    try:
        cursor.execute("""CREATE TABLE оценки
                          (предмет, студент, оценка, время получения)
                       """)
        cursor.execute("""CREATE TABLE предметы
                          (название предмета, имя преподавателя)
                       """)
        cursor.execute("""CREATE TABLE студенты
                          (имя, фамилия, страна, группа, дата рождения)
                       """)
        conn.commit()

    except sqlite3.OperationalError:
        print('Необходимые БД уже созданы')


def upload_data():
    with open('marks.csv', "r", encoding='utf-8') as file_obj:
        reader = list(csv.reader(file_obj))
        reader = [tuple(x) for x in reader]
        cursor.executemany("INSERT INTO оценки VALUES (?,?,?,?)", reader)
        conn.commit()

    with open('students.csv', "r", encoding='utf-8') as file_obj:
        reader = list(csv.reader(file_obj))
        reader = [tuple(x) for x in reader]
        cursor.executemany("INSERT INTO студенты VALUES (?,?,?,?,?)", reader)
        conn.commit()

    with open('lessons.csv', "r", encoding='utf-8') as file_obj:
        reader = list(csv.reader(file_obj))
        reader = [tuple(x) for x in reader]
        cursor.executemany("INSERT INTO предметы VALUES (?,?)", reader)
        conn.commit()


def get_lesson_info(lesson):
    cursor.execute('SELECT студент, avg(оценка) FROM оценки WHERE предмет="{0}" GROUP BY студент'.format(lesson))
    info = 'Среднее оценки учащихся по предмету: {0}'.format(lesson)
    for student in cursor.fetchall():
        info += '\n'
        for i in student:
            info += str(i) + ' '
    return info


create_database()
upload_data()
print(get_lesson_info('матан'))
