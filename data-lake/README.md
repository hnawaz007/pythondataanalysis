# trino-minio-docker

Minimal example to run Trino with Minio and the Hive standalone metastore on Docker. The data used in this tutorial is from Microsoft AdventureWorks database.  

## Installation and Setup

Install [s3cmd](https://s3tools.org/s3cmd) with:

```bash
sudo apt update
sudo apt install -y \
    s3cmd \
    openjdk-11-jre-headless  # Needed for trino-cli
```

Pull and run all services with:

```bash
docker-compose up
```

Configure `s3cmd` with (or use the `minio.s3cfg` configuration):

```bash
s3cmd --config minio.s3cfg --configure
```

Use the following configuration for the `s3cmd` configuration when prompted:

```
Access Key: minio_access_key
Secret Key: minio_secret_key
Default Region [US]:
S3 Endpoint [s3.amazonaws.com]: localhost:9000
DNS-style bucket+hostname:port template for accessing a bucket [%(bucket)s.s3.amazonaws.com]: localhost:9000
Encryption password:
Path to GPG program [/usr/bin/gpg]:
Use HTTPS protocol [Yes]: no
```

To create a bucket and upload data to minio, type:

```bash
s3cmd --config minio.s3cfg mb s3://iris
s3cmd --config minio.s3cfg put data/iris.parq s3://iris
```
To list all object in all buckets, type:

```bash
s3cmd --config minio.s3cfg la
```

## Access Trino with CLI and Prepare Table

Download trino cli with:

```bash
wget https://repo1.maven.org/maven2/io/trino/trino-cli/352/trino-cli-351-executable.jar \
  -O trino
chmod +x trino  # Make it executable
```

Create schema and create table with:

```bash
./trino --execute "
CREATE SCHEMA IF NOT EXISTS minio.sales
WITH (location = 's3a://sales/');

CREATE TABLE IF NOT EXISTS minio.sales.sales_parquet (
  productcategoryname VARCHAR,
  productsubcategoryname VARCHAR,
  productname VARCHAR,
  country VARCHAR,
  salesamount DOUBLE,
  orderdate timestamp
)
WITH (
  external_location = 's3a://sales/',
  format = 'PARQUET'
);
"
```

Query the newly created table with:

```bash
./trino --execute "
SHOW TABLES IN minio.sales;
SELECT * FROM minio.sales.sales_parquet LIMIT 5;"
```

# License

This project is licensed under the MIT license. See the [LICENSE](LICENSE) for details.
