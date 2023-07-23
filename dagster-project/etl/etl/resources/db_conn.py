import os
import urllib
import pyodbc
from sqlalchemy import create_engine
from dagster import resource
#

def get_sql_conn():
    """return db connection."""
    #get password from environmnet var
    pwd = os.environ['devrep']
    uid = os.environ['devrep123']
    #
    conn = pyodbc.connect(
              'DRIVER=' + 'DRIVER={Devart ODBC Driver for PostgreSQL' +
              ';server=' + 'cube-dev-pg2.cupdg7spipxv.eu-north-1.rds.amazonaws.com' +
              ';database=' + 'devrep' +
              ';UID=' + uid +
              ';PWD=' + pwd
              )
    try:
        return conn
    except Exception:
        print("Error connecting to PostgreSQL")