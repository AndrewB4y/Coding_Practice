from sqlalchemy import create_engine
from sqlalchemy import MetaData


conn_param = {
    "user": 'user_name',
    "password": 'passwd123',
    "host": 'localhost',
    "port": '3306',
    "dbname": 'database_name',
}

db_uri = 'mysql://{user}:{password}@{host}:{port}/{dbname}'
engine = create_engine(db_uri.format(**conn_param))

# Create MetaData instance
# Reflection is useful when you already have a database
#  filled with data and you need to deal with it using an ORM
metadata = MetaData(engine).reflect()
print(metadata.tables)

# Get Table
ex_table = metadata.tables['Example']
print(ex_table)

# Get Table Name
print(ex_table.name)

# Get Columns
print(ex_table.columns.keys())

# Get Column
c = ex_table.c.key
print(c.name)
# Or
c = ex_table.columns.key
print(c.name)

# Get Table from Column
print(c.table)

# =============== Creation of a table and insertion on it ================
from sqlalchemy import Table
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Column


db_uri = 'sqlite:///db.sqlite'
engine = create_engine(db_uri)

# create table
meta = MetaData(engine)
table = Table('user', meta,
              Column('id', Integer, primary_key=True),
              Column('l_name', String),
              Column('f_name', String))
meta.create_all()

# insert data via insert() construct
ins = table.insert().values(
    l_name='Hello',
    f_name='World')
with engine.connect() as conn:
    conn.execute(ins)

    # insert multiple data
    conn.execute(table.insert(), [
        {'l_name': 'Hi', 'f_name': 'bob'},
        {'l_name': 'yo', 'f_name': 'alice'}
    ])
