import dlt
from dlt.sources.helpers import requests
import requests
import pandas as pd
import json
from datetime import date
from datetime import datetime
from uuid import uuid4



# get data from S3
df = pd.read_parquet(
    "s3://sales/data/sales_summary_updated.parquet",
    storage_options={
        "key": "minio_access_key",
        "secret": "minio_secret_key",
        "client_kwargs": {"endpoint_url": "http://localhost:9000/"}
    }
)

# convert api data for dlt format
records = df.to_dict(orient="records")

pipeline = dlt.pipeline(
    pipeline_name="s3_pipeline",
    destination="postgres",
    dataset_name="staging"
)
# Run the pipeline 
load_info = pipeline.run(
        records, 
        write_disposition="replace",
        table_name="sales")

print(load_info)

