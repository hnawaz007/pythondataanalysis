FROM python:3.7-slim

WORKDIR /usr/src/app
ENV DAGSTER_HOME=/usr/src/app


RUN pip install dagster dagster-webserver dagit dagster-postgres SQLAlchemy==1.4.49 pandas pyarrow

# Copy our code and workspace to /usr/src/app
COPY dagster.yaml workspace.yaml .
COPY etl ./etl
COPY pyproject.toml .
COPY setup.cfg .
COPY setup.py .


EXPOSE 3000

CMD ["dagster-webserver", "-w", "workspace.yaml", "-h", "0.0.0.0", "-p", "3000"]