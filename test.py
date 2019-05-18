import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        global db
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Manipulator56789",
            database="anto")
        global cursor
        cursor = db.cursor()
        cursor.execute("select database();")
        global record
        record = cursor.fetchone()
    except Error as e:
        print("Error while connecting to MySQL", e)

def create_db(db_name):
    connect_db()
    cursor.execute("CREATE DATABASE" " "+ db_name)
    print("Your database allready insert")
    cursor.close()

def delete_db(db_name):
    connect_db()
    cursor.execute("DROP DATABASE " + db_name)
    print("succes delete database",db_name)
    cursor.close()

def show_db():
    connect_db()
    cursor.execute("SHOW DATABASES")
    for x in cursor:
      print(x)
    cursor.close()

def create_table(table_name):
    connect_db()
    cursor.execute("""CREATE TABLE IF NOT EXISTS """ + table_name + """(
    	StudentID INT PRIMARY KEY,
    	StudentName TEXT,
    	StudentStatus TEXT,
    	StudentAnswer INT)""")
    print("table created by name",table_name)
    db.close()
    cursor.close()

def insert_file(table_name, sid,nme,stts,answer):
    connect_db()
    add= """INSERT INTO  """ + table_name +"""(
          StudentID,
          StudentName,
          StudentStatus,
          StudentAnswer ) 
          VALUES (%s,%s,%s,%s)"""
    data=(sid,nme,stts,answer)
    cursor.execute(add,data)
    db.commit()
    print("Record inserted successfully to table ", table_name)
    db.close()
    cursor.close()

def show_table():
    connect_db()
    print("Your connected to database - ", record)
    cursor.execute("SHOW TABLES")
    for x in cursor:
        print(x)
    db.close()
    cursor.close()

def select_data_student(table,id):
    connect_db()
    cursor.execute("SELECT" " "+ id +" StudentAnswer FROM " + table)
    myresult = cursor.fetchone()
    for x in myresult:
      print(x)
    db.close()
    cursor.close()

def show_all_data(table_name):
    connect_db()
    # table=input("which quiz=")
    cursor.execute("SELECT * FROM " + table_name + " ORDER BY StudentID")
    myresult = cursor.fetchall()
    for x in myresult:
      print(x)
    db.close()
    cursor.close()

def delete_table(table_name):
    connect_db()
    cursor.execute("DROP TABLE IF EXISTS " + table_name)
    print ("you delete the table"" >>",table_name)
    db.close()
    cursor.close()

def update_data():
    connect_db()
    table=input("which quiz want to update:")
    id=input("which student:")
    status=input("new status :")
    answer=input("asnwer:")
    cursor.execute("UPDATE "+table+" SET StudentStatus = "+status+ ", StudentAnswer = "+answer +" WHERE StudentID = " +id)
    db.commit()
    print("succesed update for table >> ", table)
    db.close()
    cursor.close()
