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
    print("1. Display information.")
    print("2. Update database.")
    print("Insert 'x' to quit or 'h' to print the commands.")

def print_Display_Commands():
    print("1. Display Students.")
    print("2. Display Courses.")
    print("3. Display Prerequisites.")
    print("4. Display one student information.")
    print("5. Display one course information.")
    print("6. Display one course prerequisites.")
    print("7. Display one student registration.")
    print("Insert 'b' to go to the main menu or 'h' to print the commands.")

def print_Update_Commands():
    print("1. Create an new student.")
    print("2. Create an new course.")
    print("3. Add a new prerequisites.")
    print("4. Add a new registration.")
    print("5. Update a student.")
    print("6. Update a course.")
    print("7. Update a registration")
    print("Insert 'b' to go to the main menu or 'h' to print the commands.")

def checkCommand(command):
    if(command.isdigit() and int(command) > 0 and int(command) < 3):
        return True
    elif(command.isalpha() and command.upper() == 'H'):
        return True
    elif(command.isalpha() and command.upper() == 'x'):
        return False

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
        print(f"""ID: {students[i].id}
Name: {students[i].name}
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
        print(courses[i])
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
    print(f"""ID: {student.id}
Name: {student.name}
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
        get_student_helper(id)

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
        get_course_helper(code)

def get_prerequisites():
    code = input("Input the courses code: ")
    get_prerequisites_by_code(code)

def get_prerequisites_by_code(code):
    prerequisites = objecttier.get_prerequisites_by_code(code)
    if(prerequisites == []):
        print(f"{code} has no prerequisites")
    else:
        print(f"{code} prerequisites are: ")
        i = 1
        for course in prerequisites:
            print(f"  {i}. {course}")
            i += 1

def create_Prerequisites():
    print("Please enter the information of the courses")
    code2 = input("Input the course's prerequisite: ")
    code1 = input("Input the course's code: ")
    objecttier.create_prerequisites(code1, code2)
    i = input("Want to see the new prerequisite? (Y/N): ").upper()
    if(i == 'Y'):
        objecttier.get_prerequisites_by_code(code1)

def get_registrations():
    id = input("Input the student's ID: ")
    get_registration_by_id(id)

def get_registration_by_id(id):
    registrations = objecttier.get_student_registration(id)
    if(registrations.registration == []):
        print(f"The student with id '{id}' has no registrations")
    else:
        print(f"The student's with id '{id}' registratios are:")
        i = 1
        for registration in registrations.registration:
            print(f"  {i}. {registration[0]} passed with grade: {registration[1]}")

def create_Registration():
    print("Please enter the information of the student registration")
    id = input("Input the student ID: ")
    code = input("Input the course code: ")
    grade = input("Input the grade: ")
    objecttier.create_Registration(id,code,grade)
    i = input("Want to see the student's registration? (Y/N): ").upper()
    if(i == 'Y'):
        get_registration_by_id(id)

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
        print(get_student_helper(id))
    

def update_course(code = None):
    if(code == None):
        code = input("Please insert the course code: ")
    print()
    get_course_helper(code)
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
        print(get_course_helper(code))
    

def update_registration(id = None):
    if(id == None):
        id = input("Please insert the student id: ")
    get_registration_by_id(id)
    code = input("Please insert the course code you want to update: ")
    grade = input("Insert the new grade: ")
    objecttier.update_registration(id, code, grade)
    i = input("Want to see the course information? (Y/N): ").upper()
    if(i == 'Y'):
        get_registration_by_id(id)
    