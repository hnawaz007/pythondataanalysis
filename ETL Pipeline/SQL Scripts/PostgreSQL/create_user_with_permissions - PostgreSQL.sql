--create etl user
CREATE USER etl WITH PASSWORD 'demopass';
--grant connect
GRANT CONNECT ON DATABASE "AdventureWorks" TO etl;
--grant table permissions
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO etl;