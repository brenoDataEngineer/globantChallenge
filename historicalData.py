import pandas as pd
from sqlalchemy import create_engine
import os

user_path = os.path.expanduser("~")

user_path = user_path + "/globantBreno"


def extractAndLoad(filename, table_name):
    #extract
    df = pd.read_csv(user_path + "/globantChallenge/dataSample/files/" + filename)
    loadPostgres(df, table_name)

def loadPostgres(df, table_name):
    #load
    engine = create_engine('postgresql://postgres:pass#GLOBANT@localhost:5432/postgres')
    df.to_sql(table_name, engine, if_exists='append', index=False)
