## 🔄 Data Flow in `src/` Directory

The `src/` folder contains the key logic for the weather data pipeline, organized into modular Python scripts that follow a clear flow from fetching to final storage.

### 📂 Module Breakdown

- **`config_loader.py`**  
  Loads configuration values like API keys and database paths from a `.env` file or environment variables.

- **`fetch_weather.py`**  
  Handles API calls to Weatherstack. It prepares request parameters, sends the request, and returns the raw JSON response.

- **`helpers.py`**  
  Contains reusable utility functions used across the pipeline. This includes timestamp generators, data validation logic, and formatting helpers that support data transformation and logging.

- **`append_data.py`**  
  Manages data transformation and storage:
  - Appends full raw JSON to `data/raw_data/weather_data.csv`
  - Extracts and stores structured components (request, location, current) in `data/staged_data/`
  - Creates and stores a flattened, final version of the weather data in `data/final_data/current_weather_final.csv`
  - Optionally writes the final data into a SQLite database (`current_weather` table)

- **`main.py`**  
  Acts as the entry point of the pipeline. It orchestrates the steps by calling:
  1. Configuration loader
  2. Weather fetcher
  3. Data appender

### Flow Summary

1. Load configuration using `config_loader.py`
2. Fetch weather data using `fetch_weather.py`
3. Use utilities from `helpers.py` during transformation and formatting
4. Normalize and persist data through `append_data.py`
5. Trigger the full flow from `main.py`

This modular architecture ensures clean separation of concerns and makes each step reusable and testable.
