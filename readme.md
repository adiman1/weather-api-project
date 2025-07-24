# Weather Fetching Project

1) This project fetches weather data from an external API - WeatherStack Service.
2) Had Monthly 100 free calls when project started, but as of July they only provide a 14 day free trial


**Purpose**
1) Normalize the JSON file and stores it in a csv Format.
2) Store in DB and also in a Medallion Structure. i.e. Raw, Staged, Visualization Format

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
