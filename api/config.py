import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SPORTRADAR_API_KEY")

if API_KEY is None:
    raise ValueError("API key not found. Please check your .env file.") 