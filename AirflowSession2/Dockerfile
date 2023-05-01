FROM apache/airflow:2.5.3

RUN pip install dbt-postgres==1.0.5 \
	&& pip install markupsafe==2.0.1 \
	&& pip install apache-airflow-providers-odbc \
	&& pip install pyodbc \
	&& pip install apache-airflow-providers-microsoft-mssql \
	&& pip install apache-airflow-providers-microsoft-mssql[odbc] \
	&& pip install apache-airflow-providers-microsoft-azure \
	&& pip install gitpython \
	&& pip install apache-airflow-providers-airbyte[http] \
	&& pip install apache-airflow-providers-airbyte \
	&& pip install airflow-dbt \
	&& pip install plyvel \
	&& pip install --upgrade pyarrow==10.0.1

USER root
RUN apt-get update
RUN apt-get install sudo
RUN sudo apt-get install -y git

USER airflow