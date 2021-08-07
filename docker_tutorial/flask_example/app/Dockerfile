FROM python:3.8-slim  

COPY . /app  

WORKDIR /app  

RUN pip install flask psycopg2

COPY ./db_entrypoint/sql_entry.sql /docker-entrypoint-initdb.d/sql_entry.sql

ENV FLASK_APP=flask_app.py  

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]  