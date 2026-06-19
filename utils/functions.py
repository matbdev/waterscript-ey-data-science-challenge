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
    # Padronize keys
    merged_df = padronize_keys(main_df)
    
    for i, df_feat in enumerate(feature_dfs_list):
        join_cols = ['Latitude', 'Longitude']
    
        df_feat_padronized = padronize_keys(df_feat)

        # Uses 'Sample Date' if it exists on both dfs
        if 'Sample Date' in merged_df.columns and 'Sample Date' in df_feat_padronized.columns:
            join_cols.append('Sample Date')
        
        # Only unique cols
        cols_to_use = list(
            df_feat_padronized.columns.difference(merged_df.columns)
        ) + join_cols

        # Merge left on base df
        merged_df = pd.merge(
            merged_df,
            df_feat_padronized[cols_to_use],
            on=join_cols,
            how='left'
        )
        
    return merged_df

def padronize_keys(df):
    df_copy = df.copy()

    if 'Sample Date' in df.columns:
        df_copy['Sample Date'] = pd.to_datetime(df_copy['Sample Date'], dayfirst=True, errors='coerce')
        
    df_copy['Latitude'] = df_copy['Latitude'].round(6)
    df_copy['Longitude'] = df_copy['Longitude'].round(6)

    return df_copy
