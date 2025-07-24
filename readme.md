# Weather Fetching Project

This project fetches weather data from an external API - WeatherStack Service, 
Monthly 100 free calls,
Purpose - Normalize the JSON file and stores it in a csv Format.

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