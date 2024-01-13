from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.types import Integer, Unicode, UnicodeText
from sqlalchemy.schema import ForeignKey


engine = create_engine("postgresql+psycopg2://postgres:333333@localhost/mydatabase")
metadata = MetaData()

countries_table = Table("countries",
metadata,
Column('id', Integer, primary_key=True),
Column('name', Unicode(255)),
Column('code', Unicode(255)))

indicators_table = Table("indicators",
metadata,
Column('id', Unicode(255), primary_key=True),
Column('name', Unicode(255)))

data_table = Table("data",
metadata,
Column('country_id', ForeignKey("countries.id")),
Column('indicator', ForeignKey("indicators.id")),
Column('data', UnicodeText))
metadata.create_all(engine)
