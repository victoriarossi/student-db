import random
import csv
import objecttier
import sqlite3
import datetime

###########################################################################
#
# populateStudents:
#   Populates the Students table with random values from the csv file 
#    'students.csv under the resources folder.
#
###########################################################################
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

###########################################################################
#
# populateCourses:
#   Populates the Courses table with values from the csv file
#    'courses.csv' under the resources folder.
#
###########################################################################
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
            values = (course_code, name, credits, description)
            cursor.execute(sql, values)

    # Commit the changes
    dbConn.commit()

###########################################################################
#
# populatePrerequisites:
#   Populates the Prerequisites table with values from the csv file
#    'prerequisites.csv' under the resources folder.
#
###########################################################################    
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

###########################################################################
#
# populateDatabase:
#   Populates the students, courses and prerequisites tables.
#
def populateDatabase(dbConn):
    populateStudents(dbConn)
    populateCourses(dbConn)
    populatePrerequisites(dbConn)

###########################################################################
#
# getDB:
#   Returns a connection to the database.
#
###########################################################################
def getDB():
    return sqlite3.connect("students.db")


###########################################################################
#
# Main Commands
#
###########################################################################
    

    
###########################################################################
#
# printCommands:
#   Prints the main commands of the program.
#
###########################################################################
def printCommands():
    print("Please enter one of the following commands:")
    print("1. Display information.")
    print("2. Update database.")
    print("Insert 'x' to quit or 'h' to print the commands.")


###########################################################################
#
# print_Display_Commands:
#   Prints the display commands of the program.
#
###########################################################################
def print_Display_Commands():
    print("1. Display Students.")
    print("2. Display Courses.")
    print("3. Display Prerequisites.")
    print("4. Display one student information.")
    print("5. Display one course information.")
    print("6. Display one course prerequisites.")
    print("7. Display one student registration.")
    print("Insert 'b' to go to the main menu or 'h' to print the commands.")

###########################################################################
#
# print_Update_Commands:
#   Prints the update commands of the program.
#
###########################################################################
def print_Update_Commands():
    print("1. Create an new student.")
    print("2. Create an new course.")
    print("3. Add a new prerequisites.")
    print("4. Add a new registration.")
    print("5. Update a student.")
    print("6. Update a course.")
    print("7. Update a registration")
    print("Insert 'b' to go to the main menu or 'h' to print the commands.")

###########################################################################
#
# checkCommand:
#   Checks if the command is valid. If the command is valid, it returns True.
#   If the command is not valid, it returns False.
#   The command is valid if it is a number between 1 and 2 or if it is 'h' or 'x'.
#
###########################################################################
def checkCommand(command):
    if(command.isdigit() and int(command) > 0 and int(command) < 3):
        return True
    elif(command.isalpha() and command.upper() == 'H'):
        return True
    elif(command.isalpha() and command.upper() == 'X'):
        return False

###########################################################################
#
# display_Students:
#   Gets the students from the database and displays them.
#   Command: 1.1
#
###########################################################################
def display_Students(display = 0):
    students = objecttier.get_students(display+10)
    j = 0
    identifier = " "
    if(display == len(students)):
        print("There are no more students")
        return
    for i in range(display,len(students)):
        get_student(students[i].id)
    print_more = input("Do you want to see more students? (Y/N): ").upper()
    if(print_more == 'Y'):
        display_Students(i+1)

###########################################################################
#
# display_Courses:
#   Gets the courses from the database and displays them.
#   Command: 1.2
#
###########################################################################
def display_Courses(display = 0):
    courses = objecttier.get_courses(display+10)
    if(display == len(courses)):
        print("There are no more courses")
        return
    for i in range(display,len(courses)):
        get_course(courses[i].code)

    print_more = input("Do you want to see more courses? (Y/N): ").upper()
    if(print_more == 'Y'):
        display_Courses(i+1)

###########################################################################
#
# display_Prerequisites:
#   Gets the prerequisites from the database and displays them.
#   Command: 1.3
#
###########################################################################
def display_Prerequisites():
    prerequisites = objecttier.get_prerequisites()
    if(len(prerequisites) == 0):
        print("There are no prerequisites")
        return
    for prereq in range(len(prerequisites)):
        print(f"{prereq[0]} ({prereq[1]}) is a prerequisite of {prereq[2]} ({prereq[3]})")

###########################################################################
#
# valid_date_format:
#   Checks if the date string is in the correct format.
#   The correct format is 'YYYY-MM-DD'.
#   If the date string is in the correct format, it returns True. Else, returns False.
#
###########################################################################
def valid_date_format(date):
    try:
        # Attempt to parse the date string using strptime with the expected format
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True  # Return True if the date string is in the correct format
    except ValueError:
        return False  # Return False if the date string is not in the correct format

###########################################################################
#
# get_student:
#   With an id, gets that student from the database and displays it.
#   Command: 1.4
#
###########################################################################
def get_student(id = None):
    if(id == None):
        id = input("Input the student's ID: ")
    student = objecttier.get_student(id)
    if(student.identifier == ''):
        identifier = "No identifier"
    else:
        identifier = student.identifier
    print(f"""ID: {student.id}
Name: {student.name}
Email: {student.email}
Birthdate: {student.birthdate}
Address: {student.address}
Identifier: {identifier}
""")

###########################################################################
#
# create_Student:
#   Creates a new student and adds it to the database.
#   Command: 2.1
#
###########################################################################
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
    info = input("Want to see the students information? (Y/N): ").upper()
    if(info == 'Y'):
        get_student(id)

###########################################################################
#
# get_course:
#   With a code, gets that course from the database and displays it.
#   Command: 1.5
#
###########################################################################
def get_course(code = None):
    if(code == None):
        code = input("Input the courses's code: ")
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

###########################################################################
#
# create_Course:
#   Creates a new course and adds it to the database.
#   Command: 2.2
#
###########################################################################
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
        get_course(code)

###########################################################################
#
# get_prerequisites:
#   With a code, gets that course from the database and displays its prerequisites.
#   Command: 1.6
#
###########################################################################
def get_prerequisites(code = None):
    if(code == None):
        code = input("Input the course's code: ")
    prerequisites = objecttier.get_prerequisites_by_code(code)
    if(prerequisites == []):
        print(f"{code} has no prerequisites")
    else:
        print(f"{code} prerequisites are: ")
        i = 1
        for course in prerequisites:
            print(f"  {i}. {course}")
            i += 1

###########################################################################
#
# create_Prerequisites:
#   Creates a new prerequisite and adds it to the database.
#   Command: 2.3
#
###########################################################################
def create_Prerequisites():
    print("Please enter the information of the courses")
    code2 = input("Input the course's prerequisite: ")
    code1 = input("Input the course's code: ")
    objecttier.create_prerequisites(code1, code2)
    i = input("Want to see the new prerequisite? (Y/N): ").upper()
    if(i == 'Y'):
        objecttier.get_prerequisites_by_code(code1)

###########################################################################
#
# get_registrations:
#   With an id, gets that student's registrations from the database and displays them.
#   Command: 1.7
#
###########################################################################
def get_registrations(id = None):
    if(id == None):
        id = input("Input the student's ID: ")
    registrations = objecttier.get_student_registration(id)
    if(registrations.registration == []):
        print(f"The student with id '{id}' has no registrations")
        return -1
    else:
        print(f"The student's with id '{id}' registratios are:")
        i = 1
        for registration in registrations.registration:
            print(f"  {i}. {registration[0]} passed with grade: {registration[1]}")

###########################################################################
#
# create_Registration:
#   Creates a new registration and adds it to the database.
#   Command: 2.4
#
###########################################################################
def create_Registration():
    print("Please enter the information of the student registration")
    id = input("Input the student ID: ")
    code = input("Input the course code: ")
    grade = input("Input the grade: ")
    objecttier.create_Registration(id,code,grade)
    i = input("Want to see the student's registration? (Y/N): ").upper()
    if(i == 'Y'):
        get_registrations(id)

###########################################################################
#
# update_student:
#   Updates a student's information in the database.
#   Command: 2.5
#
###########################################################################
def update_student(id = None):
    if(id == None):
        id = input("Please insert the student ID: ")
    print("""What information do you want to change?
    1. Name and family name
    2. Email
    3. Birthdate
    4. Address
    5. Identification
          """)
    command = input("Input: ")
    while(command.isalpha()):
        print("Please enter a valid option.")
        command = input("Input: ")
    command = int(command)
    if(command == 1):
        name = input("First name: ")
        last_name = input("Family name: ")
        objecttier.update_student_name(id, name,last_name)
    elif(command == 2):
        email = input("Email: ")
        objecttier.update_student_email(id, email)
    elif(command == 3):
        birthdate = input("Birthdate (YYYY-MM-DD): ")
        objecttier.update_student_birthdate(id, birthdate)
    elif(command == 4):
        address = input("Address: ")
        objecttier.update_student_address(id, address)
    elif(command == 5):
        identification = input("Identification (F/M):")
        objecttier.update_student_identification(id, identification)
    i = input("Do you want to change something else? (Y/N): ").upper()
    if(i == 'Y'):
        update_student()
    i = input("Want to see the students information? (Y/N): ").upper()
    if(i == 'Y'):
        get_student(id)
    
###########################################################################
#
# update_course:
#   Updates a course's information in the database.
#   Command: 2.6
#
###########################################################################
def update_course(code = None):
    if(code == None):
        code = input("Please insert the course code: ")
    print()
    get_course(code)
    print("""What information do you want to change?
    1. Name
    2. Description
    3. Credits
        """)
    command = input("Input: ")
    while(command.isalpha()):
        print("Please enter a valid option.")
        command = input("Input: ")
    command = int(command)
    if(command == 1):
        name = input("Name: ")
        objecttier.update_course_name(code, name)
    elif(command == 2):
        description = input("Description: ")
        objecttier.update_course_description(code, description)
    elif(command == 3):
        credits = input("Credits: ")
        objecttier.update_course_credits(code, credits)
    i = input("Do you want to change something else? (Y/N): ").upper()
    if(i == 'Y'):
        update_course(code)
    i = input("Want to see the course information? (Y/N): ").upper()
    if(i == 'Y'):
        print(get_course(code))
    
###########################################################################
#
# update_registration:
#   Updates a registration's information in the database.
#   Command: 2.7
#
###########################################################################
def update_registration(id = None):
    if(id == None):
        id = input("Please insert the student id: ")
    registrations = get_registrations(id)
    if(registrations == -1):
        return
    code = input("Please insert the course code you want to update: ")
    grade = input("Insert the new grade: ")
    objecttier.update_registration(id, code, grade)
    i = input("Want to see the course information? (Y/N): ").upper()
    if(i == 'Y'):
        get_registrations(id)
    