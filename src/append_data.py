import pandas as pd
import os
import sqlite3
from src.config_loader import get_db_url
from .helpers import append_data_func
from .helpers import split_localtime
from .helpers import transform_and_append

# Filepaths to store Medallion Structure
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw_data")
STAGED_DIR = os.path.join(DATA_DIR, "staged_data")
FINAL_DIR = os.path.join(DATA_DIR, "final_data")


# To Raw Data (Bronze)
def append_to_csv(df, filename=os.path.join(RAW_DIR, "weather_data.csv")):
    append_data_func(df, filename)

# To Intermediate Data (Silver)
def append_split_data(df):
    request_colnames = [x for x in df.columns if x.startswith('request')]
    location_colnames = [x for x in df.columns if x.startswith('location')]
    current_colnames = [x for x in df.columns if x.startswith('current')]

    request_df = df[request_colnames]
    location_df = df[location_colnames]
    current_df = df[current_colnames]

    append_data_func(request_df, os.path.join(STAGED_DIR, 'request_from.csv'))
    append_data_func(location_df, os.path.join(STAGED_DIR, 'location_data.csv'))
    append_data_func(current_df, os.path.join(STAGED_DIR, 'current_weather.csv'))

# To Final Data (Gold)
def append_final_csv(df, filename=os.path.join(FINAL_DIR, "current_weather_final.csv")):
    
    '''
    1) Using loc for creating a view with purpose of explicit modification,
    2) Here view is not like sql and action on view directly impacts the actual data
    3) Direct application of list comprehension over df creates another df and also may cause unexpected behavior
    '''
    df = df.loc[:, [col for col in df.columns if 
                    (col.startswith('current.') and col not in ['current.weather_code', 'current.weather_icons', 'current.observation_time']) 
                    or col == 'location.localtime']] 
      
    df.columns = [col.replace('current.', '').replace('location.', '') for col in df.columns]
    
    df = split_localtime(df)  # Helper function - To split localtime column into time and date
    append_data_func(df, filename)


# To append final data to SQLite DB (Also Gold)
def append_final_db(df):
    df = transform_and_append(df)
    db_path = get_db_url()  # Dynamically fetch the DB path from .env
    conn = sqlite3.connect(db_path)

    try:
        df.to_sql("current_weather", conn, if_exists="append", index=False)
        print("Data successfully inserted into the database!")

    # exceptions handled via logging the failures into console, ideally we should save it in files for auditing runs
    except Exception as e:
        logging.exception("Failed to insert data into the database.")

    conn.commit()
    conn.close()
