from sqlalchemy import create_engine
from sqlalchemy import MetaData

conn_param = {
    "user": 'postgres',
    "password": 'andy',
    "host": 'localhost',
    "dbname": 'hitchdeployed',
}

db_uri = 'postgresql://{user}:{password}@{host}/{dbname}'
engine = create_engine(db_uri.format(**conn_param))

metadata = MetaData(engine)
# print(metadata)
metadata.reflect()
# print(metadata)
print(metadata.tables['app_hitchmodel'])

updated_json = {"USA": {"url": "https://www.pcrichard.com/Pioneer/Pioneer-In-Dash-Detachable-Face-AM-FM-CD-MP3-Car-Stereo/DEH-S1200UB.pcrp", "price": "$69.99", "prod_id": "88d53dbe193ce74e06d0e7efa1c64a7a37cbc0ba", "int_price": 69.99, "percent_change": 69.99, "updated": 69.99, "is_old": 0}}
hitchmodel_id = 5
update_sql = 'UPDATE app_hitchmodel SET lower_price_product=\'{}\' WHERE id={}'.format(str(updated_json), hitchmodel_id)