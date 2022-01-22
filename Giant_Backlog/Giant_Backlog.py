###################################################################################
#                                                                                 #
#                                   Giant Backlog                                 #
#                                                                                 #
###################################################################################
#       Purpose: This script will access the Giant Bomb API and download all the  #
#                videos of a show specified in the batch file arguments.          #
#                                                                                 #
#       Created by: Kyle Bales                                                    #
#       Creation Date: 01/21/22                                                   #
#                                                                                 #
###################################################################################

# %%
# Imports
import sys
import os


# %%
# Add paths to class libraries
from Classes.API import API_Class as api
from Classes.Logger import Logger_Class as log
from Classes.SQL_Server import SQL_Server_Class as ssc


# %%
# Initialize logger
logger = log.Logger("Batch_File_Read")


# %%
# Set batch file arguments
try:
    server_name = sys.argv[1]
    db_name = sys.argv[2]
except Exception as e:
    logger.warning('Failed to read in batch file arguments')
    logger.warning(f'Exception: {e}')
else:
    logger.script_completed()
    
    
# %%
# Initialize logger for script
logger = log.Logger("Giant_Backlog")


# %%
# Connect to SQL Server
try:
    ss_db = ssc.SQL_Server(server_name, db_name)
except Exception as e:
    logger.warning(f'Failed to connect to SQL server. Server: {server_name}, database: {db_name}')
    logger.warning(f'Exception: {e}')
else:
    logger.info('Connection established to SQL server')


# %%
# Close database connection
ss_db.close_ss_connection()


# %%