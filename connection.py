from getpass import getpass
from mysql.connector import connect, Error


try:
    with connect(host="localhost", user="root", password="Lodestone#123") as connection:
        print(connection)

except Exception as e:
    print(e)
