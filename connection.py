from getpass import getpass
from os import close
from mysql.connector import connect, Error

try:
    with connect(host="localhost", user="root", password="Lodestone#123") as connection:
        create_db_query = "CREATE DATABASE online_movie_rating"
        connection.reconnect()
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)
        
except Error as e:
    print(e)
    print(connection)
finally:
    connection.close()
