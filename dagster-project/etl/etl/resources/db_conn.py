import os
import urllib
import pyodbc
from sqlalchemy import create_engine
from dagster import resource
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
        print("Error connecting to SQL Server")