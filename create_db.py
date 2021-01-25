import sqlite3

def sql_con():
    try:
        con = sqlite3.connect('eventdb.db')
        return con
    except:
        print("Error creating database")

def create_table(con):
    cursor = con.cursor()
    cursor.execute("CREATE TABLE events(id integer PRIMARY KEY, name text, time text)")
    con.commit()



con = sql_con()
create_table(con)
