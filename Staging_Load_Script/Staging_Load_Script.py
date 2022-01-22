import sys
import urllib
import pandas as pd
import sqlalchemy as sa

# %%
# Set batch file arguments
server_name = sys.argv[1]
database = sys.argv[2]
source_load_filename = sys.argv[3]
target_insert_table_name = sys.argv[4]


# %%
# Connect to database
engine_params = urllib.parse.quote_plus(
    "DRIVER=ODBC+Driver+17+for+SQL+Server;SERVER={0};DATABASE={1};Trusted_Connection=yes;".format(server_name, database))
engine = sa.create_engine(
    f"mssql+pyodbc:///?odbc_connect={engine_params}",
    fast_executemany=True
)
conn = engine.raw_connection()


# %%
# Load data from passed in source table into DataFrame
source_load_path = f"C:/Projects/Python_Projects/Staging_Load_Script/SQL_Scripts/{source_load_filename}"

with open(source_load_path, 'r') as f:
    source_load_sql = f.read()

df = pd.read_sql(source_load_sql, conn)


# %%
# Bulk insert DataFrame into new SQL table
df.to_sql(f"{target_insert_table_name}", engine,
          index=False, if_exists="replace", schema="dbo")


# %%
conn.close()


# %%
