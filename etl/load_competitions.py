import json
import os
import sys
import mysql.connector

# -----------------------------
# Add project root to Python path
# -----------------------------
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# -----------------------------
# Import database connection
# -----------------------------
from utils.database import get_connection

# -----------------------------
# Connect to MySQL
# -----------------------------
try:
    connection = get_connection()
    cursor = connection.cursor()

    print("✅ Connected to MySQL")

except mysql.connector.Error as err:
    print(f"❌ Database Connection Error: {err}")
    exit()

# -----------------------------
# Read JSON File
# -----------------------------
try:
    with open("data/competitions.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    competitions = data["competitions"]

    print(f"✅ {len(competitions)} competitions found")

except Exception as err:
    print(f"❌ Error reading JSON: {err}")
    connection.close()
    exit()

# -----------------------------
# Insert Categories
# -----------------------------
inserted_categories = set()
category_count = 0

for competition in competitions:

    category = competition.get("category")

    if category is None:
        continue

    if category["id"] not in inserted_categories:

        cursor.execute("""
            INSERT IGNORE INTO categories
            (category_id, category_name)
            VALUES (%s,%s)
        """,
        (
            category["id"],
            category["name"]
        ))

        inserted_categories.add(category["id"])
        category_count += 1

# -----------------------------
# Insert Competitions
# -----------------------------
competition_count = 0

for competition in competitions:

    parent = competition.get("parent")

    parent_id = None

    if parent:
        parent_id = parent.get("id")

    cursor.execute("""
        INSERT IGNORE INTO competitions
        (
            competition_id,
            competition_name,
            parent_id,
            type,
            gender,
            category_id
        )
        VALUES
        (%s,%s,%s,%s,%s,%s)
    """,
    (
        competition.get("id"),
        competition.get("name"),
        parent_id,
        competition.get("type"),
        competition.get("gender"),
        competition["category"]["id"]
    ))

    competition_count += 1

# -----------------------------
# Commit Changes
# -----------------------------
connection.commit()

print("\n==============================")
print("Data Loaded Successfully")
print("==============================")
print(f"Categories Inserted   : {category_count}")
print(f"Competitions Inserted : {competition_count}")

# -----------------------------
# Close Connection
# -----------------------------
cursor.close()
connection.close()

print("✅ MySQL Connection Closed")