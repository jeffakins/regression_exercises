## Wrangle File for cleaning data before performing regression analysis ##

#---------------------------Imports---------------------------------------------------

import env
import pandas as pd
import numpy as np
import os

#---------------------------Connection Info Function-----------------------------------

# Connection information from the env file for the mySQL Server

def get_connection(db, user=env.username, host=env.hostname, password=env.password):
    connection_info = f'mysql+pymysql://{user}:{password}@{host}/{db}'
    return connection_info

#---------------------------Data Base Functions----------------------------------------

# Function to retrieve the 2017 Zillow Property Data Set from CODEUP's mySQL Server 
def get_zillow_data():
    '''
    Function to retrieve the 2017 Zillow Property Data Set from CODEUP's mySQL Server
    '''
    if os.path.isfile('2017_zillow_properties.csv'):
        df = pd.read_csv('2017_zillow_properties.csv', index_col=0)  # If csv file exists read in data from csv file.
    else:
        sql = '''
                SELECT bedroomcnt, bathroomcnt, 
	            calculatedfinishedsquarefeet, 
	            taxvaluedollarcnt, yearbuilt, 
	            taxamount, fips 
                FROM properties_2017
                WHERE propertylandusetypeid = 261;'''   # SQL query
                                                    
        db = 'zillow'                                   # Database name
        df = pd.read_sql(sql, get_connection(db))       # Pandas DataFrame
        df.to_csv('2017_zillow_properties.csv')         # Cache Data
    return df