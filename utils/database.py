import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="k.gokulnath2606",
        database="tennis_analytics"
    )