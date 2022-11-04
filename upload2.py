import csv
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="compegence",
    user="postgres",
    password="1234")

cursor = conn.cursor()

with open('test_dup.csv', 'r') as f:
    reader = csv.reader(f)
    print(reader)
    next(reader) # Skip the header row.
    new_list = []
    for row in reader:
        for i in row:
            i = str(i)
        new_list.append(tuple(row))
    print(len(new_list))
    for row in new_list:
        cursor.execute(
        "INSERT INTO testing_dup VALUES (%s, %s, %s)",
        row
    )
conn.commit()