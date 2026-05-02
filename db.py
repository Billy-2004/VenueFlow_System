import pymysql

def get_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="venueflow",
        cursorclass=pymysql.cursors.Cursor
    )
