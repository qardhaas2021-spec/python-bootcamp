# we will use four sql statment
# 1. Insert
# 2. Select
# 3. Update
# 4. Delate
#  Lets start by inserting the employees taple

import sqlite3
connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()
sql = """
    INSERT INTO Employee(id, name, department, phone, email)
    VALUES(1, "Ahmed", "IT", "+851909583", "qardhaas2021@gmail.com");
    INSERT INTO Employee VALUES(
        2, "Ali", "HR", "+552589", "mohamed@gmail.com"
    );
    INSERT INTO Employee VALUES(
        3, "Sara", "Marketing", "+552589", "sara@gmail.com"
    );


"""
cursor.executescript(sql)

connection.commit()

connection.close()