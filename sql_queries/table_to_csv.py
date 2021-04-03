import csv
import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="******",
                              host="localhost",
                              port="5432",
                              database="capital_city")

cursor = connection.cursor()
with open('../csv_files/country_list.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cursor.execute(
        "INSERT INTO country VALUES (%s, %s, %s, %s)",
        row
    )
connection.commit()
