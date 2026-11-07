# connect = open the .db file
# CREATE TABLE = make empty table
# INSERT = add rows
# SELECT = read rows (WHERE = filter)

import sqlite3
connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

sql = """
CREATE TABLE IF NOT EXISTS Student (
    name VARCHAR(64),
    age INTEGER,
    gender VARCHAR(64)
)
"""
cursor.execute(sql)

sql = """
INSERT INTO Student (name, age, gender) VALUES (
"Abdishakuur", 28, "male"),
("Barkhad", 35, "male"),
("Farhan", 28, "male"),
("Hassan", 22, "male"),
("Aisha", 25, "female")

"""
cursor.execute(sql)
connection.commit()
connection.close()