import urllib
import pyodbc
import sqlalchemy as sa
import pandas as pd

class SQL_Server:
    def __init__(self, server_name, db_name):
        driver_name = "ODBC+Driver+17+for+SQL+Server"
        
        engine_params = urllib.parse.quote_plus(
            f"DRIVER={driver_name};SERVER={server_name};"
            f"DATABASE={db_name};Trusted_Connection=yes;"
        )
        
        engine = sa.create_engine(
            f"mssql+pyodbc:///?odbc_connect={engine_params}",
            fast_executemany=True
        )
        
        ss_connect = engine.connect()
        self.ss_engine = engine
        self.ss_connect = ss_connect
    
    def close_ss_connection(self):
        self.ss_connect.close()
    
    def select_data_into_df(self, sql):
        df = pd.read_sql(sql, self.ss_connect, coerce_float=False)
        return df
    
    def load_data_into_sql(self, df, table_name):
        df.to_sql(table_name, self.ss_engine, index=False, if_exists='replace', schema='dbo')