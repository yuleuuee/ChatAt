import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'rabhav1120'
)
    

# prepare a cursor object
cursorObject = db.cursor()

# Create a database

cursorObject.execute("CREATE DATABASE IF NOT EXISTS chat_app_db")
print("Database created!")