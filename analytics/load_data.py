import pandas as pd
from db_connection import engine

print("Loading data from MySQL...\n")

# Load all tables
competitions = pd.read_sql("SELECT * FROM competitions", engine)
categories = pd.read_sql("SELECT * FROM categories", engine)
competitors = pd.read_sql("SELECT * FROM competitors", engine)
rankings = pd.read_sql("SELECT * FROM rankings", engine)
complexes = pd.read_sql("SELECT * FROM complexes", engine)
venues = pd.read_sql("SELECT * FROM venues", engine)

print("=" * 50)
print("DATA LOADED SUCCESSFULLY")
print("=" * 50)

print(f"Competitions : {competitions.shape}")
print(f"Categories   : {categories.shape}")
print(f"Competitors  : {competitors.shape}")
print(f"Rankings     : {rankings.shape}")
print(f"Complexes    : {complexes.shape}")
print(f"Venues       : {venues.shape}")

print("\nFirst 5 Competition Records")
print(competitions.head())

print("\nFirst 5 Competitor Records")
print(competitors.head())

print("\nFirst 5 Ranking Records")
print(rankings.head())