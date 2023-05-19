import psycopg2
from settings import (DB_HOST,
                      DB_NAME,
                      DB_PASS,
                      DB_PORT,
                      DB_USER)


def connection():
    connect = psycopg2.connect(host=DB_HOST,
                               name=DB_NAME,
                               password=DB_PASS,
                               port=DB_PORT,
                               user=DB_USER)
    return connect
