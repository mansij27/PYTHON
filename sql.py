import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="Mansi Jain", passwd="2704", database="ime")

mycursor = mydb.cursor()

mycursor.execute("select * from student")

result= mycursor.fetchall()

for i in result:
    print(i)