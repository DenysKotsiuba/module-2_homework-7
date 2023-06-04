from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass
    

class Discipline(Base):
    __tablename__ = "disciplines"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete="CASCADE"), nullable=False)
    teacher = relationship("Teacher", backref="disciplines")


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    date_of = Column(Date, nullable=False)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"), nullable=False)
    discipline_id = Column(Integer, ForeignKey("disciplines.id", ondelete="CASCADE"), nullable=False)
    student = relationship("Student", backref="grades")
    discipline = relationship("Discipline", backref="grades")


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id", ondelete="CASCADE"), nullable=False)
    group = relationship("Group", backref="students")

    @hybrid_property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    @hybrid_property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


