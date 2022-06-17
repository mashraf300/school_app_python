from sqlalchemy import Column, String, Date, Integer, Numeric
from database_manager import Base

class Person(Base):

	__tablename__ = 'person'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	gender = Column(Integer, default=0)
	age = Column(Integer)

	type = Column(String(50))

	__mapper_args__ = {"polymorphic_identity": "person", "polymorphic_on": type}

	def __init__(self, name, gender, age):
		self.name = name
		self.gender = gender
		self.age = age


	def __str__(self):
		return f"{self.name}: {self.gender}, {self.age}"