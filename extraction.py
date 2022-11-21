import csv
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="compegence",
    user="postgres",
    password="1234")

cursor = conn.cursor()

with open('extraction_croma.csv', 'r') as f:
    reader = csv.reader(f)
    print(reader)
    next(reader) # Skip the header row.
    new_list = []
    a = 0
    for row in reader:
        for x in row:
            for i in range(0,len(x)):
                if x[i] == "S":
                    if x[i-1] >= "0" and x[i-1] <="9" and x[i-1] != " ":
                        a = a + 1
                        print(x)
                        try:
                            y = int(x[i-1])
                        except TypeError:
                            print(f"Type Error In the line {i} and it is {x[i]}")
                        print(f"{y}  DataType : {type(y)}")
    print(a)

            
            
    
            
        
        

    #for z in new_list:
       # for i in z:
         #   print(len(i))
          #  break
           # for x in i:
           #     x = 0

