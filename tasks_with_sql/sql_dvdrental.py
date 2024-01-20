import psycopg2 as pg2

conn = pg2.connect(database='dvdrental',user='p',password=3)
cur = conn.cursor()
cur.execute('SELECT * FROM payment')
print(cur.fetchone())
data = cur.fetchmany(10)
print(data[9])
conn.close()
