import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from src import config_loader

def fetch_data_from_db(table_name="current_weather"):
    db_path = config_loader.get_db_url()
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df

def prepare_data(df):
    latest_date = df['observation_date'].max()
    df = df[df['observation_date'] == latest_date]
    df['datetime'] = pd.to_datetime(df['observation_date'].astype(str) + ' ' + df['observation_time'].astype(str))
    df['hour'] = df['datetime'].dt.hour
    return df, latest_date
    
def plot_temperature(df, latest_date):
    # Horizontal bands/gradients for showing temp increase
    fig, ax = plt.subplots(figsize=(12, 6))
    min_temp = 0
    max_temp = 40
    cmap = plt.cm.Reds

    for t in range(min_temp, max_temp, 5):
        norm_val = (t - min_temp) / (max_temp - min_temp)
        color = cmap(norm_val)
        ax.axhspan(t, t + 5, color=color, alpha=0.3)

    if df['temperature'].max() > 40:
        ax.axhspan(40, df['temperature'].max() + 2, color=cmap(1.0), alpha=0.7) 
    
    # Chart plotting
    ax.plot(df['hour'], df['temperature'], marker='o', linestyle='-', color='black', label='Temperature')

    for x, y in zip(df['hour'], df['temperature']):
        ax.text(x, y + 0.3, f"{y:.1f}", ha='center', va='bottom', fontsize=10)

    ax.set_xlabel('Hour of the Day')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title(f'Temperature on {pd.to_datetime(latest_date).date()}')
    ax.set_xticks(range(24))
    ax.set_xticklabels([str(i + 1) for i in range(24)])  # Display 1–24
    ax.legend()
    plt.tight_layout()
    plt.show()

def visualize_weather_data():
    df = fetch_data_from_db()
    df, latest_date = prepare_data(df)
    plot_temperature(df, latest_date)