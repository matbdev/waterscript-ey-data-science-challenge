import snowflake
from snowflake.snowpark.context import get_active_session

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