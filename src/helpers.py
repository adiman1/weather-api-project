import os
import pandas as pd

def append_data_func(df, filepath):
    if os.path.exists(filepath):
            df.to_csv(filepath, mode='a', header=False, index=False)
            print(f"Appended to {filepath}")
    else:
        print(f"Unable to append to {filepath}")

def split_localtime(df):
    if 'localtime' in df.columns:
        df[['observation_date', 'observation_time']] = df['localtime'].str.split(' ', expand=True)
        df.drop(columns=['localtime'], inplace=True)
    return df

def transform_and_append(df):

    # Cleaning json normalized df - keeping select cols, splitting cols and cleaning col names
    df = df.loc[:, [col for col in df.columns if 
                    (col.startswith('current.') and col not in ['current.weather_code', 'current.weather_icons', 'current.observation_time']) 
                    or col == 'location.localtime']] 
    
    df.columns = [col.replace('current.', '').replace('location.', '').replace('astro.', '').replace('air_quality.','') for col in df.columns]

    # Via Helper function
    df = split_localtime(df)
 
    # Conversion for Storing in DB
    df.columns = df.columns.str.replace('-', '_')
    df["weather_descriptions"] = df["weather_descriptions"][0]
    df["is_day"] = df["is_day"].apply(lambda x: 1 if str(x).strip().lower() == 'yes' else 0)
    df["moon_illumination"] = df["moon_illumination"].astype(int)
    df["temperature"] = df["temperature"].astype(float)
    df["observation_date"] = pd.to_datetime(df["observation_date"]).dt.date
    df["observation_time"] = pd.to_datetime(df["observation_time"].astype(str) + ":00", format="%H:%M:%S").dt.time
    
    return df
