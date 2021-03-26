#!/usr/bin/env python3

""" Module to match data comming from the scraper with homologued
and with not-suitable table.
"""

from numpy.core.fromnumeric import prod
import pandas as pd
from sqlalchemy import create_engine
import unicodedata
import re
import psycopg2
from os import path


def download_scraper(db="", batched=False, offset=None, batchSize=None):
    """
    download_scraper - Method that retrieves data collected by the scrapper.
                       This function can be used to return the full bulk or to
                       return a batch size with an offset.
    @db: String with the name of the table in a local DB.
    @batched: Option to enable the batched mode. True - False
    @offset: If batched is enabled, this variable is taken and should be an
             integer with the offset from which the data should be retrieved.
    @batchSize: If batched is enabled, this variable is taken and should be the
                                size or number of rows to retrieve from the DB.

    Return: A pandas dataframe with the retrieved data.
    """

    if db == "":
        print("Please provide a database-name")
        return

    if batched:
        if offset is None:
            print("Please give an <offset> value")
            return
        if batchSize is None:
            print("Please give a <batchSize> value")
            return
    # user = 'devs_queries'
    # passw = 'holbie_power'
    user = 'root'
    passw = 'root'
    ip = 'localhost'
    # db = 'scr_21012021'
    # query_dates = "SELECT DISTINCT(DATE(CREATE_TIME)) from product_details;"
    # query = "SELECT ROW_ID, URL, CREATE_TIME FROM product_details \
    # 	     WHERE DATE(CREATE_TIME)=\"2021-01-12\";"

    if batched:
        query = 'SELECT * FROM product_details' + \
            f'LIMIT {batchSize} OFFSET {offset};'

    else:
        query = "SELECT * FROM product_details;"

    # pd.set_option("display.max_rows", None, "display.max_columns", None)

    query = "SELECT * FROM product_details LIMIT 20;"
    engine = f'mysql+pymysql://{user}:{passw}@{ip}:3306/{db}?charset=utf8mb4'
    conection = create_engine(engine)
    dataframe = pd.read_sql_query(query, con=engine)

    return dataframe


def download_homologed():
    """
    download_homologed - Retrieving method for the data on the Homologados DB.

    Return: A pandas dataframe with the retrieved data.
    """

    user = 'root'
    passw = 'root'
    ip = 'localhost'
    db = 'hitch_reference'

    query = "SELECT * FROM base_homologados_inespo;"

    engine = f'mysql+pymysql://{user}:{passw}@{ip}:3306/{db}?charset=utf8mb4'
    conection = create_engine(engine)
    dataframe = pd.read_sql_query(query, con=engine)

    return dataframe


def download_Products():
    """
    download_inProduction - Retrieving method for the data on the Production DB.

    Return: A pandas dataframe with the retrieved data.
    """
    # column_names = [
    #     "id",
    #     "url",
    #     "name",
    #     "current_price",
    #     "enable",
    #     "issue_report",
    #     "description",
    #     "created",
    #     "updated",
    #     "category_id",
    #     "country_id",
    #     "hitch_model_id",
    #     "retailer_id",
    #     "sub_category_id",
    # ]
    conn_param = {
        "user": 'postgres',
        "password": 'andy',
        "host": 'localhost',
        "dbname": 'hitchdeployed',
    }

    query = "SELECT id, url, current_price FROM app_product;"

    conn = psycopg2.connect(**conn_param)
    cur = conn.cursor()
    try:
        cur.execute(query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cur.close()
        return 1

    tupples = cur.fetchall()
    cur.close()

    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=['id', 'url', 'current_price'])

    return df


def mergeScrapperHomologados(scrapData=None,
                             homologados=None,):

    if scrapData is None:
        print("Please provide a scrapData")
        return
    if homologados is None:
        print("Please provide a homologados data")
        return

    print("Scrapper on Homologados")
    scrapData_in_homologados = pd.merge(scrapData, homologados,
                                        how='inner', on='URL',
                                        suffixes=('_scrapper', '_homologados'))
    scrapData_in_homologados = scrapData_in_homologados.sort_index(axis=1)

    return scrapData_in_homologados


def filterProducts(scrInHomologados, products):

    # Matching rows upon their URL
    filtered = pd.merge(scrInHomologados, products,
                        how='inner', left_on='URL', right_on='url',
                        suffixes=('_scrapper', '_products'))

    # Filtering to get a dataframe with only the rows where Price has changed
    filtered = filtered.loc[filtered['PRICE'] != filtered['current_price']]

    return filtered


def normalizeColNames(text):

    # Stripping Accents
    try:
        text = unicode(text, 'utf-8')
    except NameError:  # unicode is a default on python 3
        pass

    text = unicodedata.normalize('NFD', text)\
        .encode('ascii', 'ignore')\
        .decode("utf-8")

    # Adding spaces to numbers preceded by a letter
    text = re.sub('([A-Za-z])(\d+(\.\d+)?)', r'\1 \2', text)

    # Replacing spaces to underscores
    text = text.replace(" ", "_")

    return str(text)


def getPricesToUpdate(scrInHomologados=None, products=None):

    if scrInHomologados is None:
        print("dataframe scrInHomologados not defined")
        return
    if scrInHomologados.get('PRICE') is None:
        print("Dataframe doesn't have the PRICE column")
        return

    # compare if price should be updated, return a filtered list
    productsToUpdate = filterProducts(
        scrInHomologados[['URL', 'PRICE']], products)

    return productsToUpdate


def updatePricesOnDB(productsToUpdate=None, products=None):

    fullFilePath = ''
    sql = '''
    COPY copy_test
    FROM 'PATH_TO_FILE.csv'
    DELIMITER ',' CSV;
    '''

    table_create_sql = '''
    CREATE TABLE IF NOT EXISTS copy_test (id                bigint,
                                        quantity          int,
                                        cost              double precision,
                                        total_revenue     double precision)
    '''
    conn_param = {
        "user": 'postgres',
        "password": 'andy',
        "host": 'localhost',
        "dbname": 'hitchdeployed',
    }

    conn = psycopg2.connect(conn_param)
    cur = conn.cursor()
    cur.execute(table_create_sql)
    # Truncate the table in case you've already run the script before
    cur.execute('TRUNCATE TABLE copy_test')

    
    df.to_csv('upload_test_data_from_copy.csv', index=False, header=False)
    cur.execute(sql)
    conn.commit()
    cur.close()
    print("COPY duration: {} seconds".format(time.time() - start_time))

    # close connection
    conn.close()


if __name__ == '__main__':
    scrapper = download_scraper(db='scr_21012021')
    homologados = download_homologed()
    scrInHomologados = mergeScrapperHomologados(scrapData=scrapper,
                                                homologados=homologados)

    # Retrieve production data to compare if price should be updated
    # Handles only the products' url and current_price
    products = download_Products()

    productsToUpdate = getPricesToUpdate(scrInHomologados, products)

    # update prices only to the list to be updated
    try:
        updatePricesOnDB(productsToUpdate, products)
    except Exception as e:
        # raise Exception('ZeroDivisionError')
        print("Update unsuccessfull: \n{}".format(e))

    # update historical

    # create trigger if price change and up to promotions
