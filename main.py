import re
from student import Student
from teacher import Teacher
from sqlalchemy import create_engine, inspect, MetaData, Table
from database_manager import setup_database
from database_helper import add_student, get_students, add_teacher, get_teachers
import tkinter as tk
from gui import SchoolApp

setup_database()

students = get_students()

if len(students) == 0:
    with open('school.txt') as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        person_line = re.findall("\:(.*)", line)[0]
        person_props = person_line.split(",")

        if line.startswith('S'):
            student = Student(person_props[0], person_props[1], person_props[2], person_props[3])
            add_student(student)
        else:
            teacher = Teacher(person_props[0], person_props[1], person_props[2], person_props[3])
            add_teacher(teacher)

        count += 1

students = get_students()
teachers = get_teachers()

print(len(teachers))

## GIVEN, Run GUI
root = tk.Tk()
obj = SchoolApp(root, students, teachers)
root.mainloop()
