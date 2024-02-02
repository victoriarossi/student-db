DROP TABLE IF EXISTS Students;
CREATE TABLE Students (
    Students_ID INT NOT NULL,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Email TEXT NOT NULL CHECK (Email LIKE '%@gmail.com' OR Email LIKE '%@outlook.com' OR Email LIKE '%@yahoo.com'),
    Birthdate DATE NOT NULL,
    Address TEXT NOT NULL,
    Identifies CHAR,
    PRIMARY KEY (Students_ID ASC)
);

DROP TABLE IF EXISTS Courses;
CREATE TABLE Courses (
    Course_Code INT NOT NULL,
    Name TEXT NOT NULL,
    Credits INT NOT NULL,
    Description TEXT,
    PRIMARY KEY (Course_Code ASC)
);

DROP TABLE IF EXISTS Prerequisites;
CREATE TABLE Prerequisites (
    Course_Code1 INT NOT NULL,
    Course_Code2 INT NOT NULL,
    FOREIGN KEY (Course_Code1) REFERENCES Course(Course_Code),
    FOREIGN KEY (Course_Code2) REFERENCES Course(Course_Code),
    PRIMARY KEY (Course_Code1, Course_Code2)
);

DROP TABLE IF EXISTS Registration;
CREATE TABLE Registration (
    Students_ID INT NOT NULL,
    Course_Code INT NOT NULL, 
    Grade CHAR CHECK(Grade IN ('A', 'B', 'C', 'D', 'F')),
    FOREIGN KEY (Students_ID) REFERENCES Students(Students_ID),
    FOREIGN KEY (Course_Code) REFERENCES Course(Course_Code),
    PRIMARY KEY (Students_ID, Course_Code)
);