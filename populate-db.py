import sqlite3
import utils

if __name__ == "__main__":

    # Create database 
    script_file = "setup.sql"
    db_file = "students.db"

    # Create a new database file if it doesn't exist
    open(db_file, 'a').close()

    # Connect to database
    dbConn = sqlite3.connect(db_file)
    cursor = dbConn.cursor()

    # Read the SQL script
    with open(script_file, 'r') as f:
        sql_script = f.read()

    # Execute the SQL commands
    cursor.executescript(sql_script)

    # Commit the changes
    dbConn.commit()
    
    # Populate database
    utils.populateDatabase(dbConn)

    # Close the connection
    dbConn.close()