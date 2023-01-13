import pandas as pd
import numpy as np
import pytest
from numpy import nan
from product_pipeline import extract, load


# get data
@pytest.fixture(scope='session', autouse=True)
def df():
    # Will be executed before the first test
    df, tbl = extract()
    yield df
    # Will be executed after the last test
    load(df, tbl)
#

# check if column exists
def test_col_exists(df):
    name="ProductKey"
    assert name in df.columns

# check for nulls
def test_null_check(df):
    assert df['ProductKey'].notnull().all()

# check values are unique
def test_unique_check(df):
    assert pd.Series(df['ProductKey']).is_unique

# check data type
def test_productkey_dtype_int(df):
    assert (df['ProductKey'].dtype == int or df['ProductKey'].dtype == np.int64)

# check data type
def test_productname_dtype_srt(df):
    assert (df['EnglishProductName'].dtype == str or  df['EnglishProductName'].dtype == 'O')

# check values in range
def test_range_val(df):
    assert df['SafetyStockLevel'].between(0,1000).any()

# check values in a list
def test_range_val_str(df):
    assert set(df.Color.unique()) == {'NA', 'Black', 'Silver', 'Red', 'White', 'Blue', 'Multi', 'Yellow','Grey', 'Silver/Black'}

