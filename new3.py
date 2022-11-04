import psycopg2
def create_db():
    conn = psycopg2.connect(
        host="localhost",
        database="compegence",
        user="postgres",
        password="1234")

    # Open a cursor to perform database operations
    cursor = conn.cursor()

    # Execute a command: this creates a new table
     
    cursor.execute("CREATE TABLE testing_dup (Article_code  varchar (800),"
                                                            "Material_number varchar (800),"
                                                            
                                                            "EAN_NO varchar (800));"
                                                            )

    cursor.close()
    conn.commit()
    conn.close()



create_db()