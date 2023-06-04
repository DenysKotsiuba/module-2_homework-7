from connect_db import session
from models import Discipline, Grade, Group, Student, Teacher
from sqlalchemy import and_, desc, func, select


def select_1():
    query = select(Student.first_name, Student.last_name, func.round(func.avg(Grade.grade), 2).label("avg_grade")).\
            select_from(Student).\
            join(Grade).\
            group_by(Student.id).\
            order_by(desc("avg_grade")).\
            limit(5)
    result = session.execute(query).all()
    return result


def select_2(discipline_id):
    query = select(Discipline.name, Student.first_name, Student.last_name, func.round(func.avg(Grade.grade), 2).label("avg_grade")).\
            select_from(Grade).\
            join(Discipline).\
            join(Student).\
            where(Discipline.id == discipline_id).\
            group_by(Student.id, Discipline.id).\
            order_by(desc("avg_grade")).\
            limit(1)
    result = session.execute(query).all()
    return result


def select_3(discipline_id):
    query = select(Group.name, Discipline.name, func.round(func.avg(Grade.grade), 2).label("avg_grade")).\
            select_from(Grade).\
            join(Student).\
            join(Group).\
            join(Discipline).\
            where(Discipline.id == discipline_id).\
            group_by(Group.id, Discipline.id).\
            order_by(desc("avg_grade"))
    result = session.execute(query).all()
    return result


def select_4():
    query = select(func.round(func.avg(Grade.grade), 5).label("avg_grade")).\
            select_from(Grade)
    result = session.execute(query).all()
    return result


def select_5(teacher_id):
    query = select(Teacher.first_name, Teacher.last_name, Discipline.name).\
            select_from(Discipline).\
            join(Teacher).\
            where(Teacher.id == teacher_id)
    result = session.execute(query).all()
    return result


def select_6(group_id):
    query = select(Student.first_name, Student.last_name, Group.name).\
            select_from(Student).\
            join(Group).\
            where(Group.id == group_id).\
            order_by(Student.first_name, Student.last_name)
    result = session.execute(query).all()
    return result


def select_7(group_id, discipline_id):
    query = select(Student.first_name, Student.last_name, Group.name, Discipline.name, Grade.grade).\
            select_from(Grade).\
            join(Discipline).\
            join(Student).\
            join(Group).\
            where(and_(Group.id == group_id, Discipline.id == discipline_id)).\
            order_by(Student.first_name, Student.last_name, Grade.grade.desc())
    result = session.execute(query).all()
    return result


def select_8(teacher_id):
    query = select(Teacher.first_name, Teacher.last_name, func.round(func.avg(Grade.grade), 2).label("avg_grade")).\
            select_from(Grade).\
            join(Discipline).\
            join(Teacher).\
            group_by(Teacher.id)
    result = session.execute(query).all()
    return result


def select_9(student_id):
    query = select(Student.first_name, Student.last_name, Discipline.name).\
            select_from(Grade).\
            join(Student).\
            join(Discipline).\
            where(Student.id == student_id).\
            group_by(Student.first_name, Student.last_name, Discipline.name)
    result = session.execute(query).all()
    return result


def select_10(student_id, teacher_id):
    query = select(Student.first_name, Student.last_name, Teacher.first_name, Teacher.last_name, Discipline.name).\
            select_from(Grade).\
            join(Student).\
            join(Discipline).\
            join(Teacher).\
            where(and_(Student.id == student_id, Teacher.id == teacher_id)).\
            group_by(Student.first_name, Student.last_name, Teacher.first_name, Teacher.last_name, Discipline.name)
    result = session. execute(query).all()
    return result


def select_11(teacher_id, student_id):
    query = select(Teacher.first_name, Teacher.last_name, Student.first_name, Student.last_name, func.round(func.avg(Grade.grade), 2).label("avg_grade")).\
            select_from(Grade).\
            join(Student).\
            join(Discipline).\
            join(Teacher).\
            where(and_(Teacher.id == teacher_id, Student.id == student_id)).\
            group_by(Teacher.first_name, Teacher.last_name, Student.first_name, Student.last_name)
    result = session.execute(query).all()
    return result


def select_12(group_id, discipline_id):
    subquery = (
        select(Grade.date_of).
        select_from(Grade).
        join(Discipline).
        join(Student).
        join(Group).
        where(Group.id == group_id, Discipline.id == discipline_id).
        order_by(Grade.date_of.desc()).limit(1).
        scalar_subquery()
    )
    query = select(Student.first_name, Student.last_name, Group.name, Discipline.name, Grade.grade).\
            select_from(Grade).\
            join(Discipline).\
            join(Student).\
            join(Group).\
            where(and_(Group.id == group_id, Discipline.id == discipline_id, Grade.date_of == subquery))
    result = session.execute(query).all()
    return result


print(session.get(Student, 2).first_name)