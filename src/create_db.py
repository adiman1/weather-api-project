import sqlite3
import os

DB_PATH = os.path.abspath(os.path.join('..', 'data', 'weather.db'))
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS current_weather (
    id INTEGER PRIMARY KEY,
    temperature REAL,
    weather_descriptions TEXT,
    sunrise TEXT,
    sunset TEXT,
    moonrise TEXT,
    moonset TEXT,
    moon_phase TEXT,
    moon_illumination INTEGER,
    co REAL,
    no2 REAL,
    o3 REAL,
    so2 REAL,
    pm2_5 REAL,
    pm10 REAL,
    us_epa_index INTEGER,
    gb_defra_index INTEGER,
    wind_speed REAL,
    wind_degree INTEGER,
    wind_dir TEXT,
    pressure REAL,
    precip REAL,
    humidity INTEGER,
    cloudcover INTEGER,
    feelslike REAL,
    uv_index REAL,
    visibility REAL,
    is_day BOOLEAN,
    observation_date DATE,
    observation_time TIME
);
"""

def create_database():
    conn = sqlite3.connect(DB_PATH) # uses path if available or creates new db
    cursor = conn.cursor()
    cursor.execute(CREATE_TABLE_SQL)
    conn.commit()
    conn.close()
    print(f"Database created at: {DB_PATH}")
    print("Table 'current_weather' created.")

if __name__ == "__main__":
    create_database()
