from connect_db import session
from models import Discipline, Grade, Group, Student, Teacher 

from datetime import datetime
from faker import Faker
from random import randint

DISCIPLINES = [
        "Logic in computer science",
        "Sociology",
        "Data structures",
        "Analysis",
        "Algorithms",
        "History",
        "Algebra",
        "Philosophy"
    ]

GROUPS = [("PW-1",), ("PW-2",), ("PW-3",)]

GRADES_NUMBER = 20

STUDENTS_NUMBER = 50

TEACHERS_NUMBER = 5

fake = Faker()


def get_random_date():
    start = datetime(2022, 9, 1, 8, 0).timestamp()
    finish = datetime(2023, 5, 31, 14, 0).timestamp()
    date_object = datetime.fromtimestamp(randint(start, finish))
    date = date_object.strftime("%Y-%m-%d")
    return date


def fill_disciplines():
    disciplines = [Discipline(name=disciplines_name, teacher_id=randint(1, TEACHERS_NUMBER)) for disciplines_name in DISCIPLINES]
    session.add_all(disciplines)
    session.commit()


def fill_grades():
    for student in range(1, STUDENTS_NUMBER+1):
        for grade in range(GRADES_NUMBER):
            session.add(Grade(grade=randint(4, 12), date_of=get_random_date(), student_id=student, discipline_id=randint(1, 8)))
    session.commit()


def fill_groups():
    groups = [Group(name=group_name) for group_name in GROUPS]
    session.add_all(groups)
    session.commit()


def fill_students():
    students = [Student(first_name=fake.first_name(), last_name=fake.last_name(), group_id=randint(1, len(GROUPS))) for i in range(STUDENTS_NUMBER)]
    session.add_all(students)
    session.commit()


def fill_teachers():
    teachers = [Teacher(first_name=fake.first_name(), last_name=fake.last_name()) for i in range(TEACHERS_NUMBER)]
    session.add_all(teachers)
    session.commit()


if __name__ == "__main__":
    fill_groups()
    fill_teachers()
    fill_students()
    fill_disciplines()
    fill_grades()

