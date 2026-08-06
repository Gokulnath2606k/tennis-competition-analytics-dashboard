import json
import os
import sys

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from api.api_client import fetch_data

print("Downloading Competition Data...")

data = fetch_data("competitions")

if data:

    os.makedirs("data", exist_ok=True)

    with open("data/competitions.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("✅ Competition data saved successfully.")

else:
    print("❌ Failed to download data.")