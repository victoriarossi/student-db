import random
import csv
import objecttier
import sqlite3

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
    print("Insert 'x' to quit.")


def display_Students(display):
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
    print_more = input("Do you want to see more students?(Y/N): ")
    if(print_more.upper() == 'Y'):
        display_Students(i+1)

def display_Courses(display):
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
    print_more = input("Do you want to see more courses?(Y/N): ")
    if(print_more.upper() == 'Y'):
        display_Courses(i+1)

def display_Prerequisites():
    pass

def create_Student():
    pass

def create_Course():
    pass

def create_Prerequisites():
    pass