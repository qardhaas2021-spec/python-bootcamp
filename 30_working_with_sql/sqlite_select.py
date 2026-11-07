import sqlite3
connection = sqlite3.connect("my_database.db")

cursor = connection.cursor()

sql = "select name, phone  from Employee"
sql = "SELECT * FROM Employee WHERE name LIKE 'A%' order by id desc"

# id = input("Enter the ID: ")


sql = "SELECT * FROM Employee"


cursor.execute(sql)

for row in cursor:
 print(row)

# row = cursor.fetchone()
# print(row)

connection.close()


# sql = "SELECT name, phone FROM Employee"
# sql = "SELECT * FROM Employee"
# sql = "SELECT * FROM Employee WHERE id = 1"
# sql = "SELECT * FROM Employee WHERE name LIKE 'A%'"
sql = "SELECT * FROM Employee WHERE name LIKE 'A%' ORDER BY id DESC"