import os
import pyodbc
from sqlalchemy import create_engine

#

def get_sql_conn():
    """return db connection."""
    #get password from environmnet var
    pwd = os.environ['PGPASS']
    uid = os.environ['PGUID']
    #
    conn = pyodbc.connect(
              'DRIVER=' + 'ODBC Driver 17 for SQL Server' +
              ';server=' + 'localhost' +
              ';database=' + 'AdventureWorksDW2019' +
              ';UID=' + uid +
              ';PWD=' + pwd
              )
    try:
        return conn
    except:
        print("Error loading the config file.")


def get_postgres_creds():
    #get password from environmnet var
    pwd = os.environ['PGPASS']
    uid = os.environ['PGUID']
    #
    server = 'localhost'
    db =  'AdventureWorks'
    uid = uid
    pwd = pwd
    port = 5432
    cs = create_engine(f'postgresql://{uid}:{pwd}@{server}:{port}/{db}')
    try:
        return cs
    except:
        print("Error loading the config file.")