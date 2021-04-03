# ----- Example Python Program to remove a PostgreSQL database table
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Start a PostgreSQL database session
connection = psycopg2.connect(user="postgres",
                              password="******",
                              host="localhost",
                              port="5432",
                              database="capital_city")

connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

# Open a database cursor

cursor = connection.cursor();

# Name of the table to be deleted

tableName = "country";

# Form the SQL statement - DROP TABLE

dropTableStmt = "DROP TABLE %s;" % tableName;

# Execute the drop table command

cursor.execute(dropTableStmt);

# Free the resources

cursor.close();

cursor.close();