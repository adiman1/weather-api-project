# Weather Fetching Project

1) This project fetches weather data from an external API - WeatherStack Service.
2) Had Monthly 100 free calls when project started, but as of July 2025 they only provide a 14 day free trial


**Purpose**
1) Normalize the JSON file and stores it as csv.
2) Store it in a Medallion Structure. i.e. Raw, Staged, Final Visualization Layers.
3) Also store the final layer in a SQLite DB.
4) Visualise the results


## 🗂️ Project Structure

```
weather-api-project/
│
├── src/
│ ├── init.py
│ ├── append_data.py
│ ├── config_loader.py
│ ├── fetch_weather.py
│ ├── helpers.py
│ └── visualize.py # (not yet used)
│
├── data/
│ ├── raw_data/
│ ├── staged_data/
│ └── final_data/
│ └── weather.db/
│
├── testing/
│ ├── code_testing.ipynb
│
├── main.py
│
├── .gitignore
├── .env
├── requirements.txt
└── readme.md

```

## ⚙️ Setup

   1. Set up a virtual environment:
      ```bash
      python -m venv venv 
      .\venv\Scripts\activate    
      ```

   2. Install dependencies:
      ```bash
      pip install -r requirements.txt
      ```

3. Add your API key in `.env` and configuration in `config_loader.py`.

## 🚀 Running the Project

   To run the project and fetch weather data:
   ```bash
   python main.py
   ```

This script:
- Loads configuration (API key, paths)
- Calls the Weatherstack API
- Appends the response to:
  - `data/raw_data/weather_data.csv`
  - `data/staged_data/*.csv` (separated into request, location, and current)
  - `data/final_data/current_weather_final.csv`
- Inserts the data into the connected database

## 🧱 Architecture: Medallion Pattern

- **Raw Layer:** Full JSON API responses Normalized as csv
- **Staged Layer:** Split Normalized CSVs (e.g. `request_from.csv`, `location_data.csv`)  
- **Final Layer:** Stripped Necessary weather data for analytics  

## 🛢️ Database Integration

1) `append_data.py` supports writing final weather data into a database (e.g. SQLite).
2) Make sure DB paths are configured properly in your config file.

## 📒 Notebooks

Use `notebooks/code_testing.ipynb` to test, visualize, or prototype changes interactively.

## 🔒 API Key

1) Store your Weatherstack API key securely. It is loaded via `config_loader.py`.
2) You can use a `.env` for local setup (not included in repo).

## 📊 Visual of a sample run

A manual run was done at some points on 2025-05-07 and plotted

![Sample Output](https://github.com/adiman1/weather-api-project/blob/4ddf6b89871a885df8104a7b13284ed25d1f292b/images/sample_trial_output.png)

## 📌 Future Improvements

- Use `visualize.py` for charts and plots  
- Add logic for storage of logs and retries  
- Support multiple cities or batch mode. Project was made to store only single location data
- Include more tests

## Important note

**Don't forget to add your API key and DB Path in .env**

