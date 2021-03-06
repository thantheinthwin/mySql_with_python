import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="I4+CYLwEB,]r",
    database="testdb"   #declaring which database we'll be using
)

mycursor = mydb.cursor()

# Running sql command to create a database
# mycursor.execute("CREATE DATABASE testdb")

# mycursor.execute("SHOW DATABASES")

# Creating a table in database
# mycursor.execute("CREATE TABLE Students (name VARCHAR(255), age INTEGER(10))")

# mycursor.execute("SHOW TABLES")

# Displaying the database or table in terminal
# for tb in mycursor:
#     print(tb)

# sqlFormula = "INSERT INTO Students (name, age) VALUES (%s, %s)"

# student = [("Rachel", 22),
#             ("Michael", 20),
#             ("Navi", 23),
#             ("Noah", 21),]
# # passing many parameters
# mycursor.executemany(sqlFormula, student)

# student1 = ("Mike", 15)
# passing only one parameter
# mycursor.execute(sqlFormula, student1)

# commiting the current transaction
# mydb.commit()

# mycursor.execute("SELECT age FROM students")

# get all the data from the table
# myresult = mycursor.fetchall()

# get only one entry
# myresult = mycursor.fetchone()
#
# for row in myresult:
#     print(row)

# selecting a variable with name starting with Mi
# sql = "SELECT * FROM students WHERE name LIKE 'Mi%'"

# selecting a variable with name which has ac in it
# sql = "SELECT * FROM students WHERE name LIKE '%ac%'"

# to prevent sql injection
# sql = "SELECT * FROM students WHERE name = %s"

# mycursor.execute(sql, ("Mike", ))
#
# myresult = mycursor.fetchall()
#
# for result in myresult:
#     print(result)

# Changing the age of the entry named Rachel
# sql = "UPDATE students SET age = 13 WHERE name = 'Rachel'"
# mycursor.execute(sql)
# mydb.commit()

# Limiting the quaries up to first 5 elements
# sql = "SELECT * FROM students LIMIT 5"

# Limiting the quaries up to first 5 elements skipping first two
# sql = "SELECT * FROM students LIMIT 5 OFFSET 2"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for result in myresult:
#     print(result)

# Order by name
# sql = "SELECT * FROM students ORDER BY name"

# Order by age decending
# sql = "SELECT * FROM students ORDER BY age DESC"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for result in myresult:
#     print(result)

# Delete a quary with name 'Rachel'
# sql = "DELETE FROM students WHERE name = 'Rachel'"

# Delete a quary with 2 conditions
# sql = "DELETE FROM students WHERE name = 'Mike' AND age = 15"

# Deleting a table
sql = "DROP TABLE IF EXISTS students"

mycursor.execute(sql)

mydb.commit()
