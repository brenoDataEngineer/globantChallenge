import pandas as pd
import psycopg2
import fastavro
import os

user_path = os.path.expanduser("~")

user_path = user_path + "/globantBreno/"

def backupTables(filename, filenameavro ,table_name):
    
    postgresql_connection_params = {
        "host": "localhost",
        "database": "postgres",
        "user": "postgres",
        "password": "pass#GLOBANT"
    }

    if table_name == 'globant_departments':
        avro_schema = {
            "type": "record",
            "name": "departments",
            "fields": [
                {"name": "id", "type": "int"},
                {"name": "department", "type": "string"},
            ]
        }
    elif table_name == 'globant_hired_employees':
        avro_schema = {
            "type": "record",
            "name": "hired_employees",
            "fields": [
                {"name": "id", "type": "int"},
                {"name": "name", "type": "string"},
                {"name": "datetime", "type": "string"},
                {"name": "department_id", "type": "int"},
                {"name": "job_id", "type": "int"},
            ]
        }
    else:
        avro_schema = {
            "type": "record",
            "name": "jobs",
            "fields": [
                {"name": "id", "type": "int"},
                {"name": "job", "type": "string"},
            ]
        }
    
    # Extract data from PostgreSQL to DataFrame
    df = extract_table_to_dataframe(table_name, postgresql_connection_params)
  
    #Convert the datafarme to csv
    df.to_csv(user_path + 'globantChallenge/backupCsv/'+ filename, index=False)

    #Set variables with the files address to use
    csv_file = user_path + 'globantChallenge/backupCsv/'+ filename
    avro_file = user_path + '/globantChallenge/backupAvro/'+ filenameavro

    #Convert the csv to Avro and save
    csv_to_avro(csv_file, avro_file, avro_schema)

def extract_table_to_dataframe(table_name, connection_params):
    with psycopg2.connect(**connection_params) as conn:
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, conn)
    return df
  
def csv_to_avro(csv_file, avro_file, avro_schema):
    # Step 1: Read CSV data into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Step 2: Convert DataFrame to Avro records
    records = df.to_dict(orient='records')

    # Step 3: Write Avro data to the output file
    with open(avro_file, 'wb') as f:
        fastavro.writer(f, avro_schema, records)
