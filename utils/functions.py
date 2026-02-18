# Session needed libs
import snowflake
from snowflake.snowpark.context import get_active_session

# Planetary Computer tools for STAC API access and authentication
import pystac_client
import planetary_computer as pc

# Bands of interest on landsat data-engineering notebook
landsat_bands_of_interest = [
    'green',
    'blue',
    'red',
    'nir08',
    'swir16',
    'swir22'
]

def save_df(df, table_name, save_path):
    '''
    Saves a Pandas DataFrame locally as a CSV and uploads it to a Snowflake stage.
    The file is saved temporarily to the /tmp/ directory before 
    being uploaded via the Snowflake PUT command.
    '''
    session = get_active_session()
    df.to_csv(f'/tmp/{table_name}.csv', index = False)
    
    session.sql(f'''
        PUT file:///tmp/{table_name}.csv
        {save_path}
        AUTO_COMPRESS=FALSE
        OVERWRITE=TRUE
    ''').collect()
    
    print(f'{table_name} saved! Refresh the browser to see the files in the sidebar')

def get_catalog(collection):
    '''
    Returns the desired collection of Microsoft Planetary Computer Catalog
    '''
    catalog = pystac_client.Client.open(
        collection,
        modifier=pc.sign_inplace,
    )

    return catalog