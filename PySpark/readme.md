## PySpark Overview

PySpark is a Python API for Apache Spark. Apache Spark is an analytics engine for large-scale data processing. It is a distributed data processing engine, meaning it runs on a cluster. A Cluster consists of three or more nodes (or computers). Spark is written in Scala, but it provides APIs for other mainstream languages such as Java, Python and R - PySpark is the Python API.
It also supports other tools and languages including Spark SQL for SQL, pandas API on Spark for pandas workloads, and Structured Streaming for incremental computation and stream processing.

## Getting Started 
In this example, we demonstratee how to setup PySpark in standalone mode. 
We write our first PySpark application that reads data from CSV file. We performe DataFrame operations using Pandas API on Spark. 
In addition, we use Spark-SQL to query the dataset we imported. Finally, we persisted the DataFrame to the PostgreSQL database.