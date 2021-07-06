
from sqlalchemy import create_engine

conn_param = {
        "user": 'user_name',
        "password": 'passwd123',
        "host": 'localhost',
  		  "port": '3306',
        "dbname": 'database_name',
    }

db_uri = 'mysql://{user}:{password}@{host}:{port}/{dbname}'
engine = create_engine(db_uri.format(**conn_param))

# Create connection
with engine.connect() as conn:
  # Begin transaction
  trans = conn.begin()
  conn.execute('INSERT INTO "EX1" (name) '
               'VALUES ("Hello")')
  trans.commit()
  # Close connection
# Here is an implicit
# conn.close()

# Optional to clean connection pool
engine.dispose()

print("Algo 1")