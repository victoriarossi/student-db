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
    pass

def get_prerequisites():
    pass

def create_student():
    pass

def create_course():
    pass

def create_prerequisites():
    pass