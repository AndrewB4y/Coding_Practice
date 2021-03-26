import pandas as pd
import numpy as np

params = {
    "user" : 'devs_queries',
    "passw" : 'holbie_power',
    "ip" : '207.180.244.42',
    "db" : 'multi_scrapper',
    "port" : 3306,
}
engine = 'mysql+pymysql://{user}:{passw}@{ip}:{port}/{db}?charset=utf8mb4'.format(**params)

q_params = {
    "column" : "ROW_ID, URL",
    "table" : "product_details",
}
query = "SELECT {column} FROM {table} limit 50;"
query2 = "SELECT {column} FROM {table} limit 25, 10;"

dataframe = pd.read_sql_query(query.format(**q_params), con=engine)
dataframe2 = pd.read_sql_query(query2.format(**q_params), con=engine)

# convert dataframe to numpy array
# dataframe.values

# Pandas dataframe to numpy array:
# dataframe.to_numpy()

# Pandas dataframe single column to numpy array:
# dataframe['URL'].to_numpy()

# pandas to numpy only floating-point numbers:
# dataframe['PRICE'].to_numpy(np.float64)

# Get dataframe column index
# c_idx = dataframe.columns.get_loc("URL")

# Inserting column at given index with zeros
# dataframe.insert(loc = c_idx + 1, column = "IT URL", value = [0] * 50)

# Inserting column at given index with empty strings
# dataframe.insert(loc = c_idx + 1, column = "2 IT URL", value = [""] * 50)

# Intersection of two dataframes
# P = pd.DataFrame ({"name":["Elizabeth","Darcy", "Andy"],
#         "email":["net@xyz.com","cy@acmecorpus.com", "andy@email.com"],
#         "aux":["ab", "cd", "zx"]})

# S = pd.DataFrame ({"name":["Andy", "Bingley","Elizabeth"],
#         "email": ["andy@email.com", "bingley@xyz.com","bennet@xyz.com"],
#         "aux":["zx", "ef", "ab"]})


# inter = pd.merge(P, S, left_on='name', right_on='name')
# inter = pd.merge(P, S, how='inner', on='name')

# Find all rows that contains given character in any column
# df[df.apply(lambda r: r.str.contains('=', case=False).any(), axis=1)]

# Find all columns which name ends with x string
# filter_col = [col for col in df if col.endswith('_scr')]
# newDf = df[filter_col]

# Apply conditional formatting only for pandas (not excel)
# df = pd.DataFrame([[2,3,1], [3,2,2], [2,4,4]], columns=list("ABC"))
# df.style.apply(lambda x: ["background: red" if v > x.iloc[0] else "" for v in x], axis = 1)

