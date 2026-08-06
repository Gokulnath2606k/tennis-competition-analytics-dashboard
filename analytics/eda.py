import pandas as pd
from db_connection import engine
import matplotlib.pyplot as plt

# Load Data
competitions = pd.read_sql("SELECT * FROM competitions", engine)
categories = pd.read_sql("SELECT * FROM categories", engine)
competitors = pd.read_sql("SELECT * FROM competitors", engine)
rankings = pd.read_sql("SELECT * FROM rankings", engine)
venues = pd.read_sql("SELECT * FROM venues", engine)
complexes = pd.read_sql("SELECT * FROM complexes", engine)

print("✅ Data Loaded Successfully")


competition_category = (
    competitions
    .merge(categories, on="category_id")
    .groupby("category_name")
    .size()
    .reset_index(name="Total Competitions")
    .sort_values("Total Competitions", ascending=False)
)

print("\nCompetition by Category")
print(competition_category)


# player analysis

country_players = (
    competitors
    .groupby("country")
    .size()
    .reset_index(name="Players")
    .sort_values("Players", ascending=False)
)

print("\nTop Countries")
print(country_players.head(10))

# ranking analysis
top_players = (
    rankings
    .merge(competitors, on="competitor_id")
    .sort_values("rank_position")
)

print("\nTop 20 Players")
print(
    top_players[
        ["rank_position", "competitor_name", "country", "points"]
    ].head(20)
)


# venue analysis 
venue_country = (
    venues
    .groupby("country_name")
    .size()
    .reset_index(name="Venues")
    .sort_values("Venues", ascending=False)
)

print("\nTop Countries by Venues")
print(venue_country.head(10))

# summary statistics
print("\n========== SUMMARY ==========")

print("Total Competitions :", len(competitions))
print("Total Players      :", len(competitors))
print("Total Venues       :", len(venues))
print("Total Categories   :", len(categories))
print("Total Complexes    :", len(complexes))

print("=============================")

# first visualization
competition_category.plot(
    x="category_name",
    y="Total Competitions",
    kind="bar",
    figsize=(10, 5),
    legend=False
)

plt.title("Competitions by Category")
plt.xlabel("Category")
plt.ylabel("Number of Competitions")

plt.tight_layout()

plt.savefig("assets/competition_category.png")

plt.show()