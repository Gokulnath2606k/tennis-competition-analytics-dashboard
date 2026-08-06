import json
import os
import sys
import mysql.connector

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from utils.database import get_connection

# Connect to MySQL
try:
    connection = get_connection()
    cursor = connection.cursor()
    print("✅ Connected to MySQL")
except mysql.connector.Error as err:
    print(f"Database Error: {err}")
    exit()

# Read JSON
try:
    with open("data/complexes.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    complexes = data["complexes"]

    print(f"Found {len(complexes)} complexes")

except Exception as err:
    print(err)
    connection.close()
    exit()

complex_count = 0
venue_count = 0

for complex_data in complexes:

    complex_id = complex_data["id"]
    complex_name = complex_data["name"]

    cursor.execute("""
        INSERT IGNORE INTO complexes
        (complex_id, complex_name)
        VALUES (%s,%s)
    """, (complex_id, complex_name))

    complex_count += 1

    venues = complex_data.get("venues", [])

    for venue in venues:

        cursor.execute("""
            INSERT IGNORE INTO venues
            (
                venue_id,
                venue_name,
                city_name,
                country_name,
                country_code,
                timezone,
                complex_id
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            venue.get("id"),
            venue.get("name"),
            venue.get("city_name"),
            venue.get("country_name"),
            venue.get("country_code"),
            venue.get("timezone"),
            complex_id
        ))

        venue_count += 1

connection.commit()

print("\n========== LOAD COMPLETED ==========")
print(f"Complexes Loaded : {complex_count}")
print(f"Venues Loaded    : {venue_count}")

cursor.close()
connection.close()

print("✅ MySQL Connection Closed")