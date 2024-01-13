from tasks_with_sql.sql_create_tables import engine, countries_table
from sqlalchemy import insert
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy import select

conn = engine.connect()
new_country = {'name': 'Canada', 'code': 'CAN'}
country = insert(countries_table).values(new_country)
conn.execute(country)

update_country = {'name': 'New Zealand'}
update_statement = update(countries_table).where(countries_table.c.id == 1).values(update_country)
conn.execute(update_statement)

delete_statement = delete(countries_table).where(countries_table.c.id == 2)
conn.execute(delete_statement)

