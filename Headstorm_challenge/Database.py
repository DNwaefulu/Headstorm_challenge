import mysql.connector
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123password",
  database="newdatabase"
)

mycursor = mydb.cursor()

# Create original Startup Database
mycursor.execute("CREATE DATABASE startup(Record_ID smallint, Name VARCHAR(50), Cell_Phone VARCHAR(14), Work_Phone VARCHAR(14), Email VARCHAR(127), Address VARCHAR(255), Basic_Widget_Order smallint, Advanced_Widget_Order smallint, Protection_Plan BOOL)")

# Starts loading information into new file path
file_path = input("Enter file path: ")

parse_file = json.loads(file_path)

for i in parse_file:
    NoSQL = "INSERT INTO startup_order(Record_ID, Name, Cell_Phone, Work_Phone, Email, Address, Basic_Widget_Order, Advanced_Widget_Order, Protection_Plan) VALUES(%d, %s, %s, %s, %s, %s, %d, %d, %r)"
    mycursor.execute(NoSQL, parse_file[i])
    mydb.commit()