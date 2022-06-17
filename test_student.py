import pytest
from student import Student

class TestStudent:

	def test_get_grades(self):
		student = Student('Jack', 'm', 14, 75)
		assert student.get_grade() == 'C'
