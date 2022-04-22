#!C:/Python/Python37/python.exe
from operator import imod


print("Content-Type:text/html")
print()
import cgi

print("<h1>Welcome to Python</h1>")

form = cgi.FieldStorage()

id = form.getvalue("id")

username = form.getvalue("username")

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"

)
cursor = con.cursor()
cursor.execute("insert into user_data values(%s,%s)",(id,username))
con.commit()

print("<h1>Record Inserted Successfully</h1>")


cursor = con.cursor()
cursor.execute("select * from user_data")
myresults = cursor.fetchall()
for x in myresults:
    print(x)
cursor.close()
con.close()
print("<h1>Record Inserted Successfully</h1>")

