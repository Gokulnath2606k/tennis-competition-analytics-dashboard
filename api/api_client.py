import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SPORTRADAR_API_KEY")

BASE_URL = "https://api.sportradar.com/tennis/trial/v3/en"


def fetch_data(endpoint):
    url = f"{BASE_URL}/{endpoint}.json"

    params = {
        "api_key": API_KEY
    }

    print("Request URL:", url)

    response = requests.get(url, params=params)

    print("Status Code:", response.status_code)
    print("Response:")
    print(response.text)

    if response.status_code == 200:
        return response.json()

    return None