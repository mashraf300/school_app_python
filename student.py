from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from person import Person


class Student(Person):

	__tablename__ = 'students'

	id = Column(Integer, ForeignKey("person.id"), primary_key=True)
	grade = Column(Integer)

	__mapper_args__ = {
        "polymorphic_identity": "student",
    }

	def __init__(self, name, gender, age, grade):
		super().__init__(name, gender, age)
		self.grade = grade


	def __str__(self):
		return f"{self.name}: {self.gender}, {self.age}, {self.grade}"
  
	def get_grade(self):
		if self.grade >= 90:
			return 'A'
		elif self.grade >= 80:
			return 'B'
		elif self.grade >= 70:
			return 'C'
		elif self.grade >= 60:
			return 'D'
		else:
			return 'F'
