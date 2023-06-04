from connect_db import session
from models import Discipline, Grade, Group, Student, Teacher

import argparse

from sqlalchemy import select, update


parser = argparse.ArgumentParser()

parser.add_argument("-a", "--action", choices=["create", "list", "update", "remove"])
parser.add_argument("-m", "--model", choices=["Discipline", "Grade", "Group", "Student", "Teacher"])
parser.add_argument("--id", help="Enter ID", type=int)
parser.add_argument("-fn", "--first_name", help="Enter first name")
parser.add_argument("-ln", "--last_name", help="Enter last name")
parser.add_argument("-n", "--name", help="Enter name")
parser.add_argument("-g", "--grade", help="Enter grade")
parser.add_argument("-d", "--date_of", help="Enter date")
parser.add_argument("-did", "--discipline_id", help="Enter discipline id", type=int)
parser.add_argument("-grid", "--group_id", help="Enter group id", type=int)
parser.add_argument("-sid", "--student_id", help="Enter student id", type=int)
parser.add_argument("-tit", "--teacher_id", help="Enter teacher id", type=int)

arguments = parser.parse_args()


def create():
    match arguments.model:
        case "Discipline":
            row = Discipline(name=arguments.name, teacher_id=arguments.teacher_id)
        case "Grade":
            row = Grade(grade=arguments.grade, date_of=arguments.date_of, student_id=arguments.student_id, discipline_id=arguments.discipline_id)
        case "Group":
            row = Group(name=arguments.name)
        case "Student":
            row = Student(first_name=arguments.first_name, last_name=arguments.last_name, group_id=arguments.group_id)
        case "Teacher":
            row = Teacher(first_name=arguments.first_name, last_name=arguments.last_name)
        case _:
            print("Enter model name")
            return None    
    session.add(row)
    session.commit()


def list():
    match arguments.model:
        case "Discipline":
            query = select(Discipline.name)
        case "Grade":
            query = select(Grade.grade, Grade.date_of)
        case "Group":
            query = select(Group.name)
        case "Student":
            query = select(Student.first_name, Student.last_name)
        case "Teacher":
            query = select(Teacher.first_name, Student.last_name)
        case _:
            print("Enter model name")
            return None   
    result = session.execute(query).all()
    print(result)


def update():
    match arguments.model:
        case "Discipline":
            row = session.get(Discipline, arguments.id)
            row.name = arguments.name
        case "Grade":
            row = session.get(Grade, arguments.id)
            row.grade = arguments.grade
        case "Group":
            row = session.get(Group, arguments.id)
            row.name = arguments.name
        case "Student":
            row = session.get(Student, arguments.id)
            row.first_name = arguments.first_name
            row.last_name = arguments.last_name
        case "Teacher":
            row = session.get(Teacher, arguments.id)
            row.first_name = arguments.first_name
            row.last_name = arguments.last_name
        case _:
            print("Enter model name")
            return None    
    session.add(row)
    session.commit()


def remove():
    match arguments.model:
        case "Discipline":
            row = session.get(Discipline, arguments.id)
        case "Grade":
            row = session.get(Grade, arguments.id)
        case "Group":
            row = session.get(Group, arguments.id)
        case "Student":
            row = session.get(Student, arguments.id)
        case "Teacher":
            row = session.get(Teacher, arguments.id)
        case _:
            print("Enter model name")
            return None    
    session.delete(row)
    session.commit()


def main():
    match arguments.action:
        case "create":
            create()
        case "list":
            list()
        case "update":
            update()
        case "remove":
            remove()
        case _:
            print("No action")


if __name__ == "__main__":
    main()