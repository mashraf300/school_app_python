import tkinter as tk
from tkinter import ttk

class SchoolApp:
	def __init__(self, root, students, teachers):
		self.root = root
		self.root.geometry("1350x700+0+0")
		self.root.title("School App")
		bg_color = "#badc57"
		title = tk.Label(self.root, text="School App", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg="#badc57", fg="Black", relief=tk.GROOVE)
		title.pack(fill=tk.X)

		#Students
		set = ttk.Treeview(root)
		set.pack(pady=20)

		set['columns']= ('id', 'name','age', 'gender', 'grade')
		set.column("#0", width=0,  stretch=tk.NO)
		set.column("id",anchor=tk.CENTER, width=80)
		set.column("name",anchor=tk.CENTER, width=150)
		set.column("age",anchor=tk.CENTER, width=80)
		set.column("gender",anchor=tk.CENTER, width=80)
		set.column("grade",anchor=tk.CENTER, width=80)


		set.heading("#0",text="",anchor=tk.CENTER)
		set.heading("id",text="ID",anchor=tk.CENTER)
		set.heading("name",text="Name",anchor=tk.CENTER)
		set.heading("age",text="Age",anchor=tk.CENTER)
		set.heading("gender",text="Gender",anchor=tk.CENTER)
		set.heading("grade",text="Grade",anchor=tk.CENTER)


		for student in students:
			set.insert(parent='',index='end',iid=student.id,text='',values=(student.id,student.name,student.age, student.gender, student.get_grade()))


		#Teachers
		teachers_set = ttk.Treeview(root)
		teachers_set.pack(pady=20)

		teachers_set['columns']= ('id', 'name','age', 'gender', 'course')
		teachers_set.column("#0", width=0,  stretch=tk.NO)
		teachers_set.column("id",anchor=tk.CENTER, width=80)
		teachers_set.column("name",anchor=tk.CENTER, width=150)
		teachers_set.column("age",anchor=tk.CENTER, width=80)
		teachers_set.column("gender",anchor=tk.CENTER, width=80)
		teachers_set.column("course",anchor=tk.CENTER, width=80)


		teachers_set.heading("#0",text="",anchor=tk.CENTER)
		teachers_set.heading("id",text="ID",anchor=tk.CENTER)
		teachers_set.heading("name",text="Name",anchor=tk.CENTER)
		teachers_set.heading("age",text="Age",anchor=tk.CENTER)
		teachers_set.heading("gender",text="Gender",anchor=tk.CENTER)
		teachers_set.heading("course",text="Course",anchor=tk.CENTER)


		for teacher in teachers:
			teachers_set.insert(parent='',index='end',iid=teacher.id,text='',values=(teacher.id,teacher.name,teacher.age, teacher.gender, teacher.course))




