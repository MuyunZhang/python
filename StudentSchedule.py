import mysql.connector
def get_database_connection():
    connection = mysql.connector.connect(user='muyunz',
                                         password='239602782',
                                         host='10.8.37.226',
                                         database='muyunz_db')
    return connection

connection = mysql.connector.connect(user='muyunz',
                                   password='239602782',
                                   host='10.8.37.226',
                                   database='muyunz_db')




cursor = connection.cursor()


id = input("Enter your student ID:")
query = "CALL GetStudentSchedule('" + id + "');"
cursor.execute(query)




for row in cursor:
   print("Period: " + str(row[0]))
   print("Course: " + str(row[1]))
   print("Room: " + str(row[2]))
   print("Teacher: " + str(row[3]))


cursor.close()
connection.close()
