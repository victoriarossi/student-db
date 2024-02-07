import datatier
import utils
import classes.Student as Student
import classes.Course as Course
import classes.Registration as Registration

###########################################################################
#
# get_students:
#   Returns a list of [LIMIT] students in the database.
#
###########################################################################
def get_students(limit):
    sql = """
    SELECT *
    FROM Students
    LIMIT ?
    """
    dbConn = utils.getDB()
    result = datatier.select_n_rows(dbConn,sql,[limit])
    s = []
    for row in result:
        name = row[1] + " " + row[2]
        one = Student.Student(row[0],name,row[3],row[4],row[5],row[6])
        s.append(one)
    return s

###########################################################################
#
# get_courses:
#   Returns a list of [LIMIT] courses in the database.
#
###########################################################################
def get_courses(limit):
    sql = """
    SELECT *
    FROM Courses
    LIMIT ?
    """
    dbConn = utils.getDB()
    result = datatier.select_n_rows(dbConn,sql,[limit])
    c = []
    for row in result:
        print(row)
        prerequisites = get_prerequisites_by_code(row[0])
        one = Course.Course(row[0],row[1],row[2],prerequisites,row[3])
        c.append(one)
    return c

###########################################################################
#
# get_prerequisites:
#   Returns a list of all prerequisites of a class with course code [code]
#   in the database.
#
###########################################################################
def get_prerequisites_by_code(code):
    sql = """
    SELECT Course_Code2
    FROM Prerequisites
    WHERE Course_Code1 = ?
    """
    dbConn = utils.getDB()
    result = datatier.select_n_rows(dbConn,sql,[code])
    p = []
    for row in result:
        p.append(row[0])
    return p

###########################################################################
#
# get_prerequisites:
#   Returns a list of all prerequisites in the database.
#
###########################################################################
def get_prerequisites():
    sql = """
    SELECT *
    FROM Prerequisites
    """
    dbConn = utils.getDB()
    result = datatier.select_n_rows(dbConn,sql)
    p = []
    for row in result:
        sql = """
        SELECT *
        FROM Courses
        WHERE Course_Code = ?
        """
        course_info1 = datatier.select_one_row(dbConn, sql, [row[0]])
        one = [course_info1[1],row[0]]
        course_info2 = datatier.select_one_row(dbConn, sql, [row[1]])
        one.extend([course_info2[1],row[1]])
        p.append(one)
    return p

###########################################################################
#
# get_student:
#   Returns a student with student id [id] in the database.
#
###########################################################################
def get_student(id):
    dbConn = utils.getDB()

    sql = """
    SELECT *
    FROM Students
    WHERE Students_ID = ?
    """
    result = datatier.select_one_row(dbConn,sql,[id])
    return Student.Student(result[0],result[1] + " " + result[2], result[3], result[4], result[5], result[6])

###########################################################################
#
# create_student:
#   Creates a student with student id [id, first_name, last_name, birthdate, address, identifier] in the database.
#
###########################################################################
def create_student(id, first_name, last_name, email, birthdate, address, identifier):
    dbConn = utils.getDB()

    sql = """
    INSERT INTO Students VALUES (?,?,?,?,?,?,?)
    """
    datatier.perform_action(dbConn,sql,[id, first_name, last_name, email, birthdate, address, identifier])

###########################################################################
#
# get_course:
#   Returns a course with course code [code] in the database.
#
###########################################################################
def get_course(code):
    dbConn = utils.getDB()

    sql = """
    SELECT *
    FROM Courses
    WHERE Course_Code = ?
    """
    result = datatier.select_one_row(dbConn,sql,[code])
    prerequisites = get_prerequisites_by_code(code)
    return Course.Course(result[0], result[1], result[2], prerequisites, result[3])

###########################################################################
#
# create_course:
#   Creates a course with course code, name, description, credits, and prerequisites in the database.
#
###########################################################################
def create_course(code, name, description, credits, prerequisites):
    dbConn = utils.getDB()
    sql = """
    INSERT INTO Courses VALUES (?,?,?,?)
    """
    datatier.perform_action(dbConn, sql, [code, name, description, credits])
    for course in prerequisites:
        sql = """
        INSERT INTO Prerequisites VALUES (?,?)
        """
        datatier.perform_action(dbConn, sql, [code,course])

###########################################################################
#
# create_prerequisites:
#   Creates the course code2 prerequisite for course code1 in the database.
#
###########################################################################
def create_prerequisites(code1, code2):
    dbConn = utils.getDB()
    sql = """
    INSERT INTO Prerequisites VALUES (?,?)
    """
    datatier.perform_action(dbConn, sql, [code1, code2])

###########################################################################
#
# create_Registration:
#   Creates a registration with student id, course code, and grade in the database.
#
###########################################################################
def create_Registration(id, code, grade):
    dbConn = utils.getDB()
    sql = """
    INSERT INTO Registration VALUES (?,?,?)
    """
    datatier.perform_action(dbConn, sql, [id, code, grade])

###########################################################################
#
# get_student_registration:
#   Returns a student's registrations with student id [id] in the database.
#
###########################################################################
def get_student_registration(id):
    dbConn = utils.getDB()
    sql = """
    SELECT *
    FROM Registration
    WHERE Students_ID = ?
    """
    result = datatier.select_n_rows(dbConn,sql,[id])
    r = []
    for row in result:
        r.append([row[1],row[2]])
    return Registration.Registration(id, r)

###########################################################################
#
# update_student_name:
#   Updates a student's first and last name with student id [id] in the database.
#
###########################################################################
def update_student_name(id, name,last_name):
    dbConn = utils.getDB()
    sql = """
    UPDATE Students
    SET FirstName = ?, LastName = ?
    WHERE Students_ID = ?
    """
    datatier.perform_action(dbConn,sql,[name, last_name, id])

###########################################################################
#
# update_student_email:
#   Updates a student's email with student id [id] in the database.
#
###########################################################################
def update_student_email(id, email):
    dbConn = utils.getDB()
    sql = """
    UPDATE Students
    SET Email = ?
    WHERE Students_ID = ?
    """
    datatier.perform_action(dbConn,sql,[email, id])

###########################################################################
#
# update_student_birthdate:
#   Updates a student's birthdate with student id [id] in the database.
#
###########################################################################
def update_student_birthdate(id, birthdate):
    dbConn = utils.getDB()
    sql = """
    UPDATE Students
    SET Birthdate = ?
    WHERE Students_ID = ?
    """
    datatier.perform_action(dbConn,sql,[birthdate, id])

###########################################################################
#
# update_student_address:
#   Updates a student's address with student id [id] in the database.
#
###########################################################################
def update_student_address(id, address):
    dbConn = utils.getDB()
    sql = """
    UPDATE Students
    SET Address = ?
    WHERE Students_ID = ?
    """
    datatier.perform_action(dbConn,sql,[address, id])

###########################################################################
#
# update_student_identification:
#   Updates a student's identifier with student id [id] in the database.
#
###########################################################################
def update_student_identification(id, identification):
    dbConn = utils.getDB()
    sql = """
    UPDATE Students
    SET Identifies = ?
    WHERE Students_ID = ?
    """
    datatier.perform_action(dbConn,sql,[identification, id])

###########################################################################
#
# update_course_name:
#   Updates a course's name with course code [code] in the database.
#
###########################################################################
def update_course_name(code, name):
    dbConn = utils.getDB()
    sql = """
    UPDATE Courses
    SET Name = ?
    WHERE Course_Code = ?
    """
    datatier.perform_action(dbConn,sql,[name, code])

###########################################################################
#
# update_course_description:
#   Updates a course's description with course code [code] in the database.
#
###########################################################################
def update_course_description(code, description):
    dbConn = utils.getDB()
    sql = """
    UPDATE Courses SET Description = "Introduction to programming: control structures; variables and data types; problem decomposition and procedural programming; input and output; aggregate data structures including arrays; programming exercises." WHERE Course_Code = 'CS 141';
    """
    datatier.perform_action(dbConn,sql,[description, code])

###########################################################################
#
# update_course_credits:
#   Updates a course's credits with course code [code] in the database.
#
###########################################################################
def update_course_credits(code, credits):
    dbConn = utils.getDB()
    sql = """
    UPDATE Courses
    SET Credits = ?
    WHERE Course_Code = ?
    """
    datatier.perform_action(dbConn,sql,[credits, code])

###########################################################################
#
# update_registration:
#   Updates a registration's grade with student id [id] and course code [code] in the database.
#
###########################################################################
def update_registration(id, code, grade):
    dbConn = utils.getDB()
    sql = """
    UPDATE Registration
    SET Grade = ?
    WHERE Students_ID = ? and Course_Code = ?
    """
    datatier.perform_action(dbConn,sql,[grade, id, code])
