CREATE SCHEMA IF NOT EXISTS minio.sales
WITH (location = 's3a://sales/');

--------------------Kafka Schema
CREATE SCHEMA minio.kafka with (LOCATION = 's3a://kafka-bucket/');