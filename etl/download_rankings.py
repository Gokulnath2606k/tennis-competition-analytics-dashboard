import json
import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# from api.api_client import fetch_data

# print("Downloading Rankings...")

# # API endpoint for doubles rankings
# data = fetch_data("rankings/doubles")

# os.makedirs("data", exist_ok=True)

# with open("data/rankings.json", "w", encoding="utf-8") as file:
#     json.dump(data, file, indent=4)

# print("✅ rankings.json created successfully")


from api.api_client import fetch_data

print("Downloading Rankings...")

data = fetch_data("double_competitors_rankings")

print(data)   # Add this line

if data:
    with open("data/rankings.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("✅ rankings.json created successfully")
else:
    print("❌ No data returned from API")