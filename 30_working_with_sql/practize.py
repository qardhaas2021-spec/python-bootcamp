import sqlite3
connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

sql = "SELECT * FROM Employee"
cursor.execute(sql)

for row in cursor:
    print(row)

