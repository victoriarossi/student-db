import random
import csv

def populateStudents(dbConn):
    cursor = dbConn.cursor()
    info = []
    with open('./resources/students.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            info.append(row)

    for i in range(50):
        # Generate random value for a person
        index = random.randint(0,99)
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