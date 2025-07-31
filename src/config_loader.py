from dotenv import load_dotenv 
import os

def get_api_key():
    load_dotenv() # to get the file with extension .env with the API Keys 
    return os.getenv("API_KEY") # to get the specific value of the secret named - API_KEY from the environment

def get_db_url():
    load_dotenv()
    return os.getenv("DB_PATH")
