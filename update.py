import csv
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="compegence",
    user="postgres",
    password="1234")

cursor = conn.cursor()

with open('update_table.csv', 'r') as f:
    reader = csv.reader(f)
    print(reader)
    next(reader) # Skip the header row.
    new_list = []
    for row in reader:
        print(row)
        new_list.append(row)
    print(len(new_list))

    cursor.execute('UPDATE croma_stk_18_sep SET ean_no= %s;',row
    )

conn.commit()