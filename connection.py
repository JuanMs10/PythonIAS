import psycopg2 as pg

conn = pg.connect(
    dbname="pythontest",
    user="postgres",
    password="1",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE movies
               (id SERIAL PRIMARY KEY,
               titulo VARCHAR(100),
               descripcion TEXT(200),
               duracion TIME,
               puntuacion INTEGER,
               category_id INTEGER FOREIGN KEY);""")

cursor.execute("""CREATE TABLE categories
               (category_id SERIAL PRIMARY KEY,
               nombre VARCHAR(20));""")

conn.commit()
cursor.close()
conn.close()
