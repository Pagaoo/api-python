import psycopg2
from decouple import config

DATABASE_HOST = config('DATABASE_HOST')
DATABASE_NAME = config('DATABASE_NAME')
DATABASE_USER = config('DATABASE_USER')
DATABASE_PASSWORD = config('DATABASE_PASSWORD')


def get_db_connection():
    connection = psycopg2.connect(
        host = DATABASE_HOST,
        database = DATABASE_NAME,
        user = DATABASE_USER,
        password = DATABASE_PASSWORD
    )
    return connection
