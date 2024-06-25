import dlt
from dlt.sources.helpers import requests
import requests
import pandas as pd
import json
from datetime import date
from datetime import datetime
from uuid import uuid4


key = 'Your-API-Key'

# api call
url = f'https://v6.exchangerate-api.com/v6/{key}/latest/USD'
# Make a request
response = requests.get(url)
data = response.json()
#
df = pd.json_normalize(data['conversion_rates'])
df = df.melt().reset_index()
df["index"] += 1 
df['date'] = date.today()
df = df.rename(columns={ 'index':'id','variable': 'currencycode', 'value': 'fxrate'})
# convert api data for dlt format
records = df.to_dict(orient="records")

pipeline = dlt.pipeline(
    pipeline_name="fxrate_pipeline",
    destination="postgres",
    dataset_name="incremental"
)
# Run the pipeline 
load_info = pipeline.run(
        records, 
        write_disposition="merge",
        primary_key=("currencycode", "date"),
        table_name="fxrates")

print(load_info)

