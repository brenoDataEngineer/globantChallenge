import fastavro
import pandas as pd
from historicalData import loadPostgres
import psycopg2
import os

user_path = os.path.expanduser("~")

user_path = user_path + "/globantBreno/"

def restoreBackup(filenameAvro, table_name):

    avro_file_path = user_path + "/globantChallenge/backupAvro/" + filenameAvro
    
    df = avro_to_dataframe(avro_file_path)

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
        user="postgres",
        password="pass#GLOBANT",
        port=5432,
    )

    # Create a cursor
    cur = conn.cursor()
    return cur, conn

def avro_to_dataframe(avro_file):
    # Step 1: Read Avro data from the file
    with open(avro_file, 'rb') as f:
        avro_reader = fastavro.reader(f)
        records = [record for record in avro_reader]

    # Step 2: Convert Avro records to a pandas DataFrame
    df = pd.DataFrame.from_records(records)
    return df
