import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="******",
                                  host="localhost",
                                  port="5432",
                                  database="capital_city")

    cursor = connection.cursor()
    # SQL query to create a new table

    create_table_query = '''CREATE TABLE country
          (country_code TEXT PRIMARY KEY NOT NULL,
           country_name TEXT NOT NULL,
           capital_city TEXT NOT NULL); '''

    # Execute a command: this creates a new table
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")




