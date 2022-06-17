from database_manager import session_factory
from student import Student
from teacher import Teacher

def add_student(student):
	ses = session_factory()
	ses.add(student)
	ses.commit()

def get_students():
	ses = session_factory()
	res = ses.query(Student).all()

	return res

def add_teacher(teacher):
	ses = session_factory()
	ses.add(teacher)
	ses.commit()

def get_teachers():
	ses = session_factory()
	res = ses.query(Teacher).all()

	return res