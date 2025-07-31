import requests
import pandas as pd
from src import config_loader

key  = config_loader.get_api_key()

def get_weather (city): # args is city of interest
    url = f"https://api.weatherstack.com/current?access_key={key}" 
    querystring = {"query":city}
    response = requests.get(url, params=querystring)

    try:
        response
        if response.status_code == 200:
            data = response.json()
            df = pd.json_normalize(data)
            return df
        else:
            return {"error": f"Failed to retrieve data. Status code: {response.status_code}"}
    except Exception as e:
    print("Error occurred:", e)

