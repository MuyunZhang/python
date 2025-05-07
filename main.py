import mysql.connector

connection = mysql.connector.connect(user='muyunz',
                                     password='239602782',
                                     host='10.8.37.226',
                                     database='muyunz_db')
cursor = connection.cursor()

department_list = []
count = 0;
query = "SELECT Department_Name FROM Departments"
cursor.execute(query)

for row in cursor:
    print(str(count) + ". " + row[0])
    count = count + 1
    department_list.append(row[0])


answer = input('Enter your department choice (type the number): ')
print(department_list[int(answer)])

query = "SELECT Teachers.Teacher_Name FROM Departments INNER JOIN Teachers ON Teachers.Department_ID = Departments.Department_ID WHERE Departments.Department_Name = '" + department_list[int(answer)] + "'";
cursor.execute(query)

for row in cursor:
    print(row[0])

cursor.close()
connection.close()

