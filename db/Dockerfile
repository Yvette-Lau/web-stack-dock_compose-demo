FROM postgres:latest
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=postgres
COPY ./create_tables.sql /docker-entrypoint-initdb.d/create_tables.sql
COPY ./fill_tables.sql /docker-entrypoint-initdb.d/fill_tables.sql