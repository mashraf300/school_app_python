First Project Draft


Your brother, who is the principal of a small school, asked you to help him develop a system to manage the school. You are given a .txt file named school.txt that contains the information of some students and teachers. In this file, each row represents the data of a student or a teacher, as shown in the following example:

S:Steven Nelson,m,12,89

The fields are type (student (S) or teacher (T)), name, gender (male (m) or female (f)), age (numeric), average grade (for students) or course (for teachers) respectively.

Task 1 (20 points)

Convert the file of students and teachers to a sqlite database with custom classes for students and teachers.

Note: Make sure to only add the information from the file to your database once upon creation. 

Task 2 (10 points)

Create a function named get_grade in your Student class that converts the numeric grade into a letter grade using the following table:


Numeric Grade
Letter Grade
90 to 100
A
80 to 89
B
70 to 79
C
60 to 69
D
0 to 59
F




Task 3 (20 points)

Get all students and teachers from your database and show them using the gui.py file that you’re given. This file uses the Tkinter library that we will dive into later this microdegree to create a simple GUI, but don’t worry about that for now. Once you have the data you retrieved from the database, you can just call the following lines to pass it to the GUI: 

import tkinter as tk
from gui import SchoolApp

root = tk.Tk()
obj = SchoolApp(root, students, teachers)
root.mainloop()

Note: This class uses the fields inside your custom classes Student and Teacher to show the data. These fields are assumed to have the names: 

Student: name, gender, age, get_grade (the function that you created in task 2)
Teacher: name, gender, age, course

If you have different field names, don’t panic. You can change the following lines in gui.py with your field names.

Line 35:
set.insert(parent='',index='end',iid=student.id,text='',values=(student.id,student.name,student.age, student.gender, student.get_grade()))

Line 60: 
teachers_set.insert(parent='',index='end',iid=teacher.id,text='',values=(teacher.id,teacher.name,teacher.age, teacher.gender, teacher.course))

Task 4 (10 points)

Finally, you are required to create a test function using pytest to make sure your function get_grades works well. Once you are done with your test function, feel free to try it with different values for grades to make sure the function get_grades works as intended. 
