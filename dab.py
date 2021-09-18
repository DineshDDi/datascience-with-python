import mysql.connector

mydb = mysql.connector.connect(host="localhost", port=4401, user="root", password="Divi@0410", database="dini")

# print(mydb)

mycursor = mydb.cursor()

mycursor.execute("insert into export_data_new values(4, 'avengers', 92.2, 'adventure')")

mydb.commit()

database = mycursor.fetchall()

for x in database:
    print(x)




