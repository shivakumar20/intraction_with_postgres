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
     
    cursor.execute("CREATE TABLE testing (Article_Code  varchar (800),"
                                                            "DC_Code varchar (800),"
                                                            "Store_Name varchar (800),"
                                                            "Article_Description varchar (800),"
                                                            "BSL_Material_Code varchar (800) ,"
                                                            "ENA_No varchar (800),"
                                                            "Available_Qty varchar (800),"
                                                            "Reoporting_Date varchar (800),"
                                                            "Serial_Number varchar (800),"
                                                            "Class_No varchar (800),"
                                                            "Class_Description varchar (800),"
                                                            "Formate_ID varchar (800),"
                                                            "Formate_Description varchar (800),"
                                                            "Return_Qty varchar (800),"
                                                            "Scaleable_Quty varchar (800),"
                                                            "Defective varchar (800),"
                                                            "Display_Qty varchar (800),"
                                                            "Transit_Quty varchar (800),"
                                                            "GT_Qty varchar (800),"
                                                            "Brand varchar (800),"
                                                            "Brand_Name varchar (800),"
                                                            "Manufacturer varchar (800),"
                                                            "Manufacturer_Desc varchar (800),"
                                                            "Warrenty_Period varchar (800),"
                                                            "EOL_Date varchar (800),"
                                                            "Product_Category varchar (800),"
                                                            "Tonnage varchar (800),"
                                                            "Star_Rating varchar (800),"
                                                            "Storage_Capicity varchar (800),"
                                                            "CADR varchar (800),"
                                                            "Area_Cover varchar (800),"
                                                            "PartnerID varchar (800));"
                                                            )

    cursor.close()
    conn.commit()
    conn.close()



create_db()