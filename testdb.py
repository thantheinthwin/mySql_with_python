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
#
# student = [("Rachel", 22),
#             ("Michael", 20),
#             ("Navi", 23),
#             ("Noah", 21),]
# # passing many parameters
# mycursor.executemany(sqlFormula, student)

# student1 = ("Steve", 21)
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
sql = "SELECT * FROM students WHERE name = %s"

mycursor.execute(sql, ("Mike", ))

myresult = mycursor.fetchall()

for result in myresult:
    print(result)
