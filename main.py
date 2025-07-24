from src import fetch_weather
from src import append_data
# from src import visualize


def main():
    weather_data = fetch_weather.get_weather(city='bangalore') # change city of interest
    append_data.append_to_csv(weather_data)
    append_data.append_split_data(weather_data)
    append_data.append_final_csv(weather_data)
    append_data.append_final_db(weather_data)
 #  visualize.visualize_weather_data()

if __name__ == "__main__" :
    main()
