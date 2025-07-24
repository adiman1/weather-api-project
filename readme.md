# Weather Fetching Project

1) This project fetches weather data from an external API - WeatherStack Service.
2) Had Monthly 100 free calls when project started, but as of July they only provide a 14 day free trial


**Purpose**
1) Normalize the JSON file and stores it in a csv Format.
2) Store in DB and also in a Medallion Structure. i.e. Raw, Staged, Visualization Format


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
│
├── code_testing.ipynb
│
├── main.py
├── requirements.txt
└── README.md

```

## Setup

   1. Install dependencies:
      ```bash
      pip install -r requirements.txt
      ```

   2. Set up the virtual environment:
      ```bash
      python -m venv venv 
      .\venv\Scripts\activate    
      ```

3. Add your API key in `.env` and configuration in `config_loader.py`.

## Running the Project

   To run the project and fetch weather data:
   ```bash
   python main.py
   ```
