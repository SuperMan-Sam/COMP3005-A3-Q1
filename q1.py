import sys
import psycopg2
from psycopg2 import Error

# Database connection parameters
DB_NAME = "a3"
DB_USER = "postgres"
DB_PASSWORD = "admin"
DB_HOST = "localhost"
DB_PORT = "5432"

def connect():
    try:
        connection = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )
        return connection
    except Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

def getAllStudents():
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        for student in students:
            print(student)
        cursor.close()
        connection.close()
    except Error as e:
        print(f"Error fetching students: {e}")

def addStudent(first_name, last_name, email, enrollment_date):#Add student to table
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                       (first_name, last_name, email, enrollment_date))
        connection.commit()
        print("Student added successfully")
        cursor.close()
        connection.close()
    except Error as e:
        print(f"Error adding student: {e}")

def updateStudentEmail(student_id, new_email):#update student email
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET email = %s WHERE student_id = %s",
                       (new_email, student_id))
        connection.commit()
        print("Email updated successfully")
        cursor.close()
        connection.close()
    except Error as e:
        print(f"Error updating email: {e}")

def deleteStudent(student_id):#delete student by id
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        connection.commit()
        print("Student deleted successfully")
        cursor.close()
        connection.close()
    except Error as e:
        print(f"Error deleting student: {e}")


def run_command(command):
    if command == "getAllStudents":#print all students
        getAllStudents()
    elif command == "addStudent":#add student info to table
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
        addStudent(first_name, last_name, email, enrollment_date)
    elif command == "updateStudentEmail":#update student email by id
        student_id = int(input("Enter student ID: "))
        new_email = input("Enter new email: ")
        updateStudentEmail(student_id, new_email)
    elif command == "deleteStudent":#delete student by id
        student_id = int(input("Enter student ID: "))
        deleteStudent(student_id)
    elif command == "help":#get help menu
        print("'getAllStudents' = get all students in table")
        print("'addStudent' = add students to table")
        print("'updateStudentEmail' = update students email by id")
        print("'deleteStudent' = remove students by id")
    else:
        print("Usage: 'python a3.py help' to get help")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: 'python a3.py help' to get help")
        sys.exit(1)
    command = sys.argv[1]
    run_command(command)
