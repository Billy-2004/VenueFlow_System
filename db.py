import pymysql

def get_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="billzeitt1979%",
        database="venueflow",
        cursorclass=pymysql.cursors.Cursor
    )