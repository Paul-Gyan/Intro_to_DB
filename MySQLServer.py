import mysql.connector
from mysql.connector import Error

def create_database(host_name, database_name, user_name, user_password):
    """Create a database in the MySQL server."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host= "localhost",
            user= "root",
            password= "Iloveowus@5280"
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store ")
        print(f"Database alx_book_store created successfully!")
    except mysql.connector.Error as e:
        print(f"Error while creating database: {e}")
    finally:
        if connection is not None:
            connection.close()

if _name_ == "_main_":
    host_name = "localhost"
    database_name = "alx_book_store"
    user_name = "root"
    user_password = "Iloveowus@5280"

    create_database(host_name, database_name, user_name, user_password)