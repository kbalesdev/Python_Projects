import sys
import pandas as pd
import pyodbc

#%%
# Set batch file arguments
server_name = sys.argv[1]
database = sys.argv[2]
table_name = sys.argv[3]
new_table_name = sys.argv[4]


#%%
# Connect to database and read table columns
conn_str = f"Driver=SQL Server;Server={server_name};Database={database};Trusted_Connection=yes;"
conn = pyodbc.connect(conn_str)


#%%
# Read table columns and data types of incoming table name argument
sql_query = "SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, CHARACTER_MAXIMUM_LENGTH, NUMERIC_PRECISION, NUMERIC_SCALE\n"
sql_query = sql_query + f"FROM {database}.INFORMATION_SCHEMA.COLUMNS\n"
sql_query = sql_query + f"WHERE TABLE_NAME=\'{table_name}\';"

df = pd.read_sql(sql_query, conn)


#%%
# Write Create Table SQL statement from DataFrame
create_statement = f"CREATE TABLE {new_table_name}\n(\n\t"

for row in df.itertuples(index=False):
    if(row.DATA_TYPE == 'varchar'):
        create_statement = create_statement + f"{row.COLUMN_NAME} VARCHAR({int(row.CHARACTER_MAXIMUM_LENGTH)})"
    elif(row.DATA_TYPE == 'int'):
        create_statement = create_statement + f"{row.COLUMN_NAME} INT"
    elif(row.DATA_TYPE == 'datetime'):
        create_statement = create_statement + f"{row.COLUMN_NAME} DATETIME"
    elif(row.DATA_TYPE == 'bit'):
        create_statement = create_statement + f"{row.COLUMN_NAME} BIT"
    
    if(row.IS_NULLABLE == 'NO'):
        create_statement = create_statement + " NOT NULL"
    create_statement = create_statement + ",\n\t"

create_statement = create_statement.rstrip(',\n\t')
create_statement = create_statement + "\n);"

#%%
# Write create statement to a text file
with open('C:/Projects/Python_Projects/Create_Table_Script/Output/output.txt', 'w+') as f:
    f.writelines(create_statement)
    
    
#%%
# Close database connection
conn.close()

#%%