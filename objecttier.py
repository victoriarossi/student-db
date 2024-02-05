import datatier
import utils
import sqlite3
import Student
import Course

def get_students():
    sql = """
    SELECT *
    FROM Students
    """
    dbConn = utils.getDB()
    result = datatier.select_n_rows(dbConn,sql)
    s = []
    for row in result:
        name = row[1] + " " + row[2]
        one = Student.Student(name,row[3],row[4],row[5],row[6])
        s.append(one)
    return s

def get_courses():
    sql = """
    SELECT *
    FROM Courses
    """
    dbConn = utils.getDB()
    result = datatier.select_n_rows(dbConn,sql)
    c = []
    for row in result:
        prerequisites = get_prerequisites_by_code(row[0])
        one = Course.Course(row[0],row[1],row[3],prerequisites,row[2])
        c.append(one)
    return c

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

def get_student(id):
    dbConn = utils.getDB()

    sql = """
    SELECT *
    FROM Students
    WHERE Students_ID = ?
    """
    result = datatier.select_one_row(dbConn,sql,[id])
    return Student.Student(result[1] + " " + result[2], result[3], result[4], result[5], result[6])

def create_student(id, first_name, last_name, email, birthdate, address, identifier):
    dbConn = utils.getDB()

    sql = """
    INSERT INTO Students VALUES (?,?,?,?,?,?,?)
    """
    datatier.create_entry(dbConn,sql,[id, first_name, last_name, email, birthdate, address, identifier])

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

def create_course(code, name, description, credits, prerequisites):
    dbConn = utils.getDB()
    sql = """
    INSERT INTO Courses VALUES (?,?,?,?)
    """
    datatier.create_entry(dbConn, sql, [code, name, description, credits])
    for course in prerequisites:
        sql = """
        INSERT INTO Prerequisites VALUES (?,?)
        """
        datatier.create_entry(dbConn, sql, [code,course])

def create_prerequisites():
    pass