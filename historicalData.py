import pandas as pd
from sqlalchemy import create_engine

def extractAndLoad(filename, table_name):
    #extract
    df = pd.read_csv("/Users/brenocarlo/globant-challenge/globantChallenge/files/" + filename)
    loadPostgres(df, table_name)

def loadPostgres(df, table_name):
    #load
    engine = create_engine('postgresql://breno:breno123@localhost:5432/postgres')
    df.to_sql(table_name, engine, if_exists='append', index=False)
