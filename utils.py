import random
import csv
import objecttier
import sqlite3
import datetime

def populateStudents(dbConn):
    cursor = dbConn.cursor()
    info = []
    with open('./resources/students.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            info.append(row)

    for i in range(50):
        # Generate random value for a person
        index = random.randint(0,98)
        person_data = info[index]
        student_id = i 
        first_name = person_data[0].split()[0]
        last_name = person_data[0].split()[1]
        email = person_data[1]
        birthdate = person_data[2]
        address = person_data[3]
        if(len(person_data) < 5):
            identifies = ' '
        else:
            identifies = person_data[4]

        # Insert the random values into the Students table
        sql = f"INSERT INTO Students VALUES (?, ?, ?, ?, ?, ?, ?)"
        values = (student_id, first_name, last_name, email, birthdate, address, identifies)
        cursor.execute(sql, values)

    # Commit the changes
    dbConn.commit()

def populateCourses(dbConn):
    cursor = dbConn.cursor()
    with open('./resources/courses.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
            course_code = row[0]
            name = row[1]
            description = row[2]
            credits = row[3]

            # Insert the random values into the Students table
            sql = f"INSERT INTO Courses VALUES (?, ?, ?, ?)"
            values = (course_code, name, description, credits)
            cursor.execute(sql, values)

    # Commit the changes
    dbConn.commit()

def populatePrerequisites(dbConn):
    cursor = dbConn.cursor()
    with open('./resources/prerequisites.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            course_code1 = row[0]
            course_code2 = row[1]

            # Insert the random values into the Students table
            sql = f"INSERT INTO Prerequisites VALUES (?, ?)"
            values = (course_code1, course_code2)
            cursor.execute(sql, values)

    # Commit the changes
    dbConn.commit()

def populateDatabase(dbConn):
    populateStudents(dbConn)
    populateCourses(dbConn)
    populatePrerequisites(dbConn)

def getDB():
    return sqlite3.connect("students.db")


#####################################################
#
# Main Commands
#
#####################################################
    

def printCommands():
    print("Please enter one of the following commands:")
    print("1. Display Students.")
    print("2. Display Courses.")
    print("3. Display Prerequisites.")
    print("4. Create an new student.")
    print("5. Create an new course.")
    print("6. Create an new prerequisites.")
    print("7. Create a new registration.")
    print("8. Display one student information.")
    print("9. Display one course information.")
    print("Insert 'x' to quit.")

def display_Students():
    display_Students_helper(0)

def display_Students_helper(display):
    students = objecttier.get_students()
    j = 0
    identifier = " "
    if(display == len(students)):
        print("There are no more students")
        return
    for i in range(display,len(students)):
        if(students[i].identifier == ' '):
            identifier = "No identifier"
        else:
            identifier = students[i].identifier
        print(f"""Name: {students[i].name}
Email: {students[i].email}
Birthdate: {students[i].birthdate}
Address: {students[i].address}
Identifier: {identifier}
""")
        j += 1
        if(j == 10):
            break
    print_more = input("Do you want to see more students? (Y/N): ")
    if(print_more.upper() == 'Y'):
        display_Students_helper(i+1)

def display_Courses():
    display_Courses_helper(0)

def display_Courses_helper(display):
    courses = objecttier.get_courses()
    j = 0
    description = " "
    prerequisites = " "
    if(display == len(courses)):
        print("There are no more courses")
        return
    for i in range(display,len(courses)):
        if(len(courses[i].description) == 0):
            description = "No description"
        else:
            description = courses[i].description

        if(len(courses[i].prerequisites) == 0):
            prerequisites = "No prerequisites"
        else:
            prerequisites = courses[i].prerequisites
        print(f"""Course code: {courses[i].code}
Course name: {courses[i].name}
Course credits: {courses[i].credits}
Course decription: {description}
Course prerequisites: {prerequisites}
""")
        j += 1
        if(j == 10):
            break
    print_more = input("Do you want to see more courses? (Y/N): ")
    if(print_more.upper() == 'Y'):
        display_Courses_helper(i+1)

def display_Prerequisites():
    display_Prerequisites_helper(0)

def display_Prerequisites_helper(display):
    prerequisites = objecttier.get_prerequisites()
    j = 0
    if(display == len(prerequisites)):
        print("There are no more students")
        return
    for i in range(display,len(prerequisites)):
        print(f"{prerequisites[i][0]} ({prerequisites[i][1]}) is a prerequisite of {prerequisites[i][2]} ({prerequisites[i][3]})")
        j += 1
        if(j == 10):
            break
    print_more = input("Do you want to see more prerequisites? (Y/N): ")
    if(print_more.upper() == 'Y'):
        display_Prerequisites_helper(i+1)

def valid_date_format(date):
    try:
        # Attempt to parse the date string using strptime with the expected format
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True  # Return True if the date string is in the correct format
    except ValueError:
        return False  # Return False if the date string is not in the correct format

def get_student():
    id = input("Input the student's ID: ")
    get_student_helper(id)

def get_student_helper(id):
    student = objecttier.get_student(id)
    if(student.identifier == ''):
        identifier = "No identifier"
    else:
        identifier = student.identifier
    print(f"""Name: {student.name}
Email: {student.email}
Birthdate: {student.birthdate}
Address: {student.address}
Identifier: {identifier}
""")


def create_Student():
    print("Please enter the information of the student you want to create")
    id = input("Input the student's ID number: ")
    first_name = input("Input the student's first name: ")
    last_name = input("Input the student's last name: ")
    email = input("Input the student's email: ")
    birthdate = input("Input the student's birthdate(YYYY-MM-DD): ")
    while(not valid_date_format(birthdate)):
        birthdate = input("Input the student's birthdate(YYYY-MM-DD): ")
    address = input("Input the student's address: ")
    i = input("Do you want to add an identifier? (Y/N): ")
    if(i.upper() == 'Y'):
        identifier = input("Input the student's identifier: ")
    else:
        identifier = ""
    objecttier.create_student(id, first_name,last_name,email,birthdate, address,identifier)
    i = input("Want to see the students information? (Y/N): ").upper()
    if(i == 'Y'):
        print(get_student_helper(id))

def get_course():
    code = input("Input the courses's code: ")
    get_course_helper(code)

def get_course_helper(code):
    course = objecttier.get_course(code)
    if(course.prerequisites == []):
        prerequisites = "No prerequisites"
    else:
        prerequisites = course.prerequisites
    print(f"""Code: {course.code}
Name: {course.name}
Description: {course.description}
Credits: {course.credits}
Prerequisites: {prerequisites}
""")


def create_Course():
    print("Please enter the information of the course you want to create")
    code = input("Input the course's code: ")
    name = input("Input the course's name: ")
    description = input("Input the course's description: ")
    credits = input("Input the course's number of credits: ")
    i = input("Does the course have prerequisites? (Y/N): ").upper()
    if(i == 'Y'):
        prerequisites = input("Input the course's prerequisites separated by commas: ").split(',')
    else:
        prerequisites = []
    objecttier.create_course(code, name, description, credits, prerequisites)
    i = input("Want to see the course information? (Y/N): ").upper()
    if(i == 'Y'):
        print(get_course_helper(code))



def create_Prerequisites():
    pass