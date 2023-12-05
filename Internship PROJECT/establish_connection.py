'''import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Dvg@5321",
        database="car",
        autocommit=True
    )
    print("Connected to MySQL!")
except mysql.connector.Error as err:
    print(f"Error: {err}")'''
import mysql.connector

# Connection parameters
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Dvg@5321",
    "database": "car",
    "autocommit": True,
}

# Establish a connection
mydb = mysql.connector.connect(**db_config)

