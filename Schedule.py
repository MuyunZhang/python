import mysql.connector
def get_database_connection():
    connection = mysql.connector.connect(user='muyunz',
                                         password='239602782',
                                         host='10.8.37.226',
                                         database='muyunz_db')
    return connection

def execute_statement(connection, statement):
    cursor = connection.cursor()
    cursor.execute(statement)
    results = []

    for row in cursor:
        results.append(row)

    cursor.close()
    connection.close()

    return results

def get_student_schedule(student_id):
    statement = "CALL GetStudentSchedule('" + student_id + "');"
    return execute_statement(get_database_connection(), statement)


def get_teacher_schedule(teacher_id):
    statement = "CALL GetTeacherSchedule('" + teacher_id + "');"
    return execute_statement(get_database_connection(), statement)


type = input("Teacher or Student:")
type = type.lower()
id = input("Enter your ID:")
if type == 'teacher':
    results = get_teacher_schedule(id)
if type == 'student':
    results = get_student_schedule(id)



for result in results:
    period = result[0]
    course = result[1]
    room = result[2]
    teacher = result[3]
    print("Period: ",  period)
    print("Course: ",  course)
    print("Room: ", room)
    print("Teacher: ", teacher)
    print()



