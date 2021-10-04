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

mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)
