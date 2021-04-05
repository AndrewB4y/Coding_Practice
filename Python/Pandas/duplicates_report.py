import pandas as pd


# Reading the excel into pandas dataframe
df = pd.read_excel(
    'scr_en_homologados_08032021.xlsx',
    sheet_name=0,
    engine='openpyxl'
)

url_dups = df[df.duplicated(keep=False, subset=['URL'])]

del df

filename = "dupsURL.xlsx"

writer = pd.ExcelWriter(
    filename, engine='xlsxwriter',
    options={
        'strings_to_urls': False,
        'strings_to_formulas': False
    }
)

url_dups.to_excel(writer)
writer.save()
writer.close()
