import sqlite3
connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

phone = input("Enter the phone: ")
employee_id = input("Enter the employee ID: ")
department = input("Enter the department: ")

sql = "UPDATE Employee SET department=?,phone=? WHERE id=?"
cursor.execute(sql, (department, phone, employee_id))

connection.commit()

connection.close()