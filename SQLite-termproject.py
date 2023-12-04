import sqlite3
def CreateTable(table_name, records):
    with sqlite3.connect(database_name) as con:
        cur = con.cursor()
        command = f'CREATE TABLE IF NOT EXISTS {table_name}({records})'
        cur.execute(command)
        print("done")
# ----------------------------------------------------------------  
def ReadTable(table_name):
    with sqlite3.connect(database_name) as con:
        cur = con.cursor()
        command = f"SELECT * FROM {table_name};"
        cur.execute(command)
        records = cur.fetchall()
        for i in records:
            print(i)
        print("done")
# ----------------------------------------------------------------  
def InsertTable(table_name,records):
    with sqlite3.connect(database_name) as con:
        cur = con.cursor()
        command = f"INSERT INTO {table_name} VALUES ('{records}');"
        cur.execute(command)
        print("done")
# ----------------------------------------------------------------
def DeleteTable(table_name):
    with sqlite3.connect(database_name) as con:
        cur = con.cursor()
        command = f'DROP TABLE IF EXISTS {table_name};'
        cur.execute(command)
        print("done")
# ----------------------------------------------------------------  
database_name = input("enter your database name please here: ")
print("""please select one of the following
            1.Create Table
            2.Read Table
            3.Insert Table
            4.Delete Table
            5.Exit Table ==>      """)
def start_app(start):
    while start != '5':
        if start == '1':
            CreateTable(input("enter your table name: "), input("enter your record item name: "))
        elif start == '4':
            DeleteTable(input("enter your table name to delete: "))
        elif start == '3':
            InsertTable(input("enter your table name to insert: "), input("enter your record to add: "))
        elif start == '2':
            ReadTable(input("enter your table name to show: "))
        start = input("enter Option: ")
    print("see you later bye")

start_app(input("Choose Ur option: "))
