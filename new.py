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
     
    cursor.execute("CREATE TABLE croma_stk_18_sep (Article_code  varchar (800),"
                                                            "DC_Code varchar (800),"
                                                            "Store_Name varchar (800),"
                                                            "Article_Description varchar (800),"
                                                            "BSL_Metrial_code varchar (800),"
                                                            "EAN_No varchar (800),"
                                                            "Available_Qty varchar (800),"
                                                            "Reporting_date varchar (800),"
                                                            "Region varchar (800),"
                                                            "City varchar (800),"
                                                            "Product_Category varchar (800),"
                                                            "Sub_Category varchar (800),"
                                                            "Tonnage varchar (800),"
                                                            "Star_Rating varchar (800),"
                                                            "Storage_Capacity varchar (800),"
                                                            "CADR varchar (800),"
                                                            "Area_Cover varchar (800),"
                                                            "Partner_Id varchar (800));"
                                                            )

    cursor.close()
    conn.commit()
    conn.close()



create_db()