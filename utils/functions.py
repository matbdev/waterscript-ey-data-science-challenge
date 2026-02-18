# Session needed libs
import snowflake
from snowflake.snowpark.context import get_active_session

# Planetary Computer tools for STAC API access and authentication
import pystac_client
import planetary_computer as pc

# Data processing
import pandas as pd

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

def combine_datasets(main_df, feature_dfs_list):
    '''
    Returns a  vertically concatenated dataset.
    You can pass as many datasets you want, inside a list.
    Verifys lenght to avoid errors.
    '''
    join_cols = ['Latitude', 'Longitude', 'Sample Date']
    merged_df = main_df.copy()

    # Padronize the keys
    merged_df_padronized = padronize_keys(merged_df)
    
    for i, df_feat in enumerate(feature_dfs_list):
        df_feat_copy = df_feat.copy()

        # Padronize the keys
        df_feat_copy_padronized = padronize_keys(df_feat_copy)
        
        # Only unique cols
        cols_to_use = list(
            df_feat_copy_padronized.columns.difference(merged_df.columns)
        ) + join_cols

        # Merge left on base df
        merged_df = pd.merge(
            merged_df,
            df_feat_copy_padronized[cols_to_use],
            on=join_cols,
            how='left'
        )
        
    return combined

def padronize_keys(df):
    df_copy = df.copy()

    if 'Sample Date' in df.columns:
        df_copy['Sample Date'] = pd.to_datetime(df_copy['Sample Date'], dayfirst=True, errors='coerce')
        
    df_copy['Latitude'] = df_copy['Latitude'].round(6)
    df_copy['Longitude'] = df_copy['Longitude'].round(6)

    return df_copy
