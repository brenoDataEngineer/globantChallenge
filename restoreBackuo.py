import fastavro
import pandas as pd
from historicalData import loadPostgres
import psycopg2


def restoreBackup(filename, table_name):

    avro_file_path = "/Users/brenocarlo/globant-challenge/globantChallenge/backupAvro/" + filename

    if table_name == 'departments':
        ###### AQUI ######
        your_avro_schema = {
            "type": "record",
            "name": "departments",
            "fields": [
                {"name": "id", "type": "int"},
                {"name": "department", "type": "string"},
                # Add other fields based on your table columns and data types.
            ],
        }
    elif table_name == 'hired_employees':
        your_avro_schema = {
            "type": "record",
            "name": "hired_employees",
            "fields": [
                {"name": "id", "type": "int"},
                {"name": "name", "type": "string"},
                {"name": "datetime", "type": "string"},
                {"name": "department_id", "type": "integer"},
                {"name": "job_id", "type": "integer"},
                # Add other fields based on your table columns and data types.
            ],
        }
    else:
        your_avro_schema = {
            "type": "record",
            "name": "jobs",
            "fields": [
                {"name": "id", "type": "int"},
                {"name": "job", "type": "string"},
                # Add other fields based on your table columns and data types.
            ],
        }
    
    with open(avro_file_path, "rb") as avro_file:
        records = list(fastavro.reader(avro_file, schema=your_avro_schema))

    df = pd.DataFrame.from_records(records)

    deletePostgres(table_name)
    loadPostgres(df, table_name)

def deletePostgres(table_name):
    curr, conn = dbconnection()
    sql_query = "DELETE FROM " + table_name + " WHERE 1 = 1"
    curr.execute(sql_query)
    conn.commit()
    print("Data Cleaned")

def dbconnection():
    conn = psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="newuser",
        password="@Breno123",
        port=5432,
    )

    # Create a cursor
    cur = conn.cursor()
    return cur, conn
