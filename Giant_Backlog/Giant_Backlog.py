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
import pandas as pd
import numpy as np


# %%
# Add paths to class libraries
from Classes.API import API_Class as api
from Classes.Converters import Converters_Class as conv
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
    api_key = sys.argv[3]
except Exception as e:
    logger.warning('Failed to read in batch file arguments')
    logger.warning(f'Exception: {e}')
else:
    logger.script_completed()


# %%
# Hard coded values for testing
server_name = 'DESKTOP-G0G762V'
db_name = 'GiantBacklog'


# %%
# Initialize logger for script
logger = log.Logger("Giant_Backlog")


# %%
# Initialize class libraries
gb_api = api.API()
convs = conv.Converters()


# %%
# Connect to SQL Server
try:
    ss_db = ssc.SQL_Server(server_name, db_name)
except Exception as e:
    logger.warning(
        f'Failed to connect to SQL server. Server: {server_name}, database: {db_name}')
    logger.warning(f'Exception: {e}')
else:
    logger.info('Connection established to SQL server')


# %%
# Get shows from database
try:
    gb_shows = ss_db.select_data_into_df('SELECT * FROM VideoShows')
except Exception as e:
    logger.warning(f'Error retrieving shows from database')
    logger.warning(f'Exception: {e}')
else:
    logger.info(f'Successfully retrieved shows from the database')
    
    
# %%
# Save video shows to file and open it
os.chdir(os.path.dirname(__file__))

gb_shows.to_csv('./video_shows.csv', header=True, index=False, sep=' ', mode='a', columns=['id', 'title'])

os.startfile('video_shows.csv')


# %%
# Create a command line parser



# %%
# Read response JSON, normalize it and place into a DataFrame
try:
    json = response.json()
    df = pd.json_normalize(json, record_path=['results'])
    print(df)
except Exception as e:
    logger.warning('Failed to parse response into JSON')
    logger.warning(f'Exception: {e}')
else:
    logger.info('Failed to normalize data and create DataFrame')


# %%



# %%
# Close database connection
ss_db.close_ss_connection()


# %%