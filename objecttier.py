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
    print(result)
    for row in result:
        prerequisites = get_prerequisites(row[0])
        one = Course.Course(row[0],row[1],row[3],prerequisites,row[2])
        c.append(one)
    return c

def get_prerequisites(code):
    sql = """
    SELECT Course_Code1
    FROM Prerequisites
    WHERE Course_Code2 = ?
    """
    dbConn = utils.getDB()
    result = datatier.select_n_rows(dbConn,sql,[code])
    p = []
    for row in result:
        p.append(row[0])
    return p
    

def create_student():
    pass

def create_course():
    pass

def create_prerequisites():
    pass