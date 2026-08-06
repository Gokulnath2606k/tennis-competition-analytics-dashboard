import json
import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from api.api_client import fetch_data

print("Downloading Complexes...")

data = fetch_data("complexes")

os.makedirs("data", exist_ok=True)

with open("data/complexes.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("✅ complexes.json created successfully")