
import pandas as pd




# Reading the excel into pandas dataframe
df = pd.read_excel(
    'scrapper_08032021.xlsx',
    sheet_name=0,
    engine='openpyxl'
)

