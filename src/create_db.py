import sqlite3
from config import DB_PATH

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
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(CREATE_TABLE_SQL)
    conn.commit()
    conn.close()
    print(f"Database created at: {DB_PATH}")

if __name__ == "__main__":
    create_database()
