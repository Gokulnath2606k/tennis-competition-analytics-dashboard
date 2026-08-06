import json
import os
import sys
import mysql.connector

# ---------------------------------------
# Add project root to Python path
# ---------------------------------------
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from utils.database import get_connection

# ---------------------------------------
# Connect to MySQL
# ---------------------------------------
try:
    connection = get_connection()
    cursor = connection.cursor()
    print("✅ Connected to MySQL")
except mysql.connector.Error as err:
    print(f"❌ Database Connection Error: {err}")
    exit()

# ---------------------------------------
# Read rankings.json
# ---------------------------------------
try:
    with open("data/rankings.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    ranking_groups = data["rankings"]

    print(f"✅ {len(ranking_groups)} ranking groups found")

except Exception as err:
    print(f"❌ Error reading JSON: {err}")
    connection.close()
    exit()

competitor_count = 0
ranking_count = 0

# ---------------------------------------
# Load Data
# ---------------------------------------
for group in ranking_groups:

    print(f"\nLoading: {group['name']}")

    competitor_rankings = group.get("competitor_rankings", [])

    for row in competitor_rankings:

        competitor = row.get("competitor", {})

        # Insert Competitor
        cursor.execute("""
            INSERT IGNORE INTO competitors
            (
                competitor_id,
                competitor_name,
                country,
                country_code,
                abbreviation
            )
            VALUES (%s,%s,%s,%s,%s)
        """,
        (
            competitor.get("id"),
            competitor.get("name"),
            competitor.get("country"),
            competitor.get("country_code"),
            competitor.get("abbreviation")
        ))

        competitor_count += cursor.rowcount

        # Insert Ranking
        cursor.execute("""
            INSERT IGNORE INTO rankings
            (
                rank_position,
                movement,
                points,
                competitions_played,
                competitor_id
            )
            VALUES (%s,%s,%s,%s,%s)
        """,
        (
            row.get("rank"),
            row.get("movement"),
            row.get("points"),
            row.get("competitions_played"),
            competitor.get("id")
        ))

        ranking_count += cursor.rowcount

# ---------------------------------------
# Commit
# ---------------------------------------
connection.commit()

print("\n===================================")
print("🎉 Rankings Loaded Successfully")
print("===================================")
print(f"Competitors Inserted : {competitor_count}")
print(f"Rankings Inserted    : {ranking_count}")

cursor.close()
connection.close()

print("✅ MySQL Connection Closed")