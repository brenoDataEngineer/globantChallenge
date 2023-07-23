from fastavro import schemaless_writer
from restoreBackuo import dbconnection

def backupTables(filename, table_name):
    cur, conn = dbconnection()
    select_query = f"SELECT * FROM {table_name}"

    cur.execute(select_query)
    columns = [desc[0] for desc in cur.description]  # Fetch column names
    data = cur.fetchall()  # Fetch all rows

    #If strucutre hired_employees, departments, jobs
    # Replace 'your_avro_schema' with the Avro schema definition based on
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

    avro_file_path = "/Users/brenocarlo/globant-challenge/globantChallenge/backupAvro/" + filename

    with open(avro_file_path, "wb") as avro_file:
        for row in data:
            record = dict(zip(columns, row))
            schemaless_writer(avro_file, your_avro_schema, record)

    cur.close()
    conn.close()
