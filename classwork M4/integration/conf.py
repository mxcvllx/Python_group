import psycopg2
from psycopg2.extras import RealDictCursor

connection = psycopg2.connect(
    dbname='taxidb',
    user='postgres',
    password='Odiljon350',
    host='localhost',
    port=5432
)

cur = connection.cursor(cursor_factory=RealDictCursor)

sql = "insert into cars(name, color) values (%s, %s)"
cur.execute(sql, ("test1", "white"))
connection.commit()

cur.execute("select * from cars where id=%s", (4,))
cars = cur.fetchall()
# cars2 = cur.fetchone()
# cars2 = cur.fetchmany(2)

with connection.cursor(cursor_factory=RealDictCursor) as cur:
    cur.execute("select * from cars where id=%s", (4,))
    cars = cur.fetchall()
    print("with context manager", cars)
