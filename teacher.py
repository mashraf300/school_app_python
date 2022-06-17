from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from person import Person

class Teacher(Person):

	__tablename__ = 'teachers'

	id = Column(Integer, ForeignKey("person.id"), primary_key=True)
	course = Column(String)

	__mapper_args__ = {
        "polymorphic_identity": "teacher",
    }

	def __init__(self, name, gender, age, course):
		super().__init__(name, gender, age)
		self.course = course



	def __str__(self):
		return f"{self.name}: {self.gender}, {self.age}, {self.course}"