import psycopg2
from environs import Env

env = Env()
env.read_env()


def connect():
    return psycopg2.connect(
        dbname=env("DB_NAME"),
        user=env("DB_USER"),
        password=env("DB_PASSWORD"),
        host=env("DB_HOST"),
        port=env("DB_PORT")
    )


connection = connect()