import pandas as pd
import plotly.express as px
from db_connection import engine

# Load tables
competitions = pd.read_sql("SELECT * FROM competitions", engine)
categories = pd.read_sql("SELECT * FROM categories", engine)
competitors = pd.read_sql("SELECT * FROM competitors", engine)
rankings = pd.read_sql("SELECT * FROM rankings", engine)
venues = pd.read_sql("SELECT * FROM venues", engine)
complexes = pd.read_sql("SELECT * FROM complexes", engine)

print("✅ Data Loaded")


# competition category bar chart 

competition_category = (
    competitions
    .merge(categories, on="category_id")
    .groupby("category_name")
    .size()
    .reset_index(name="Competitions")
    .sort_values("Competitions", ascending=False)
)

fig = px.bar(
    competition_category,
    x="category_name",
    y="Competitions",
    title="Competitions by Category",
    text="Competitions"
)

fig.show()

# top 1p countries by players bar chart

country_players = (
    competitors
    .groupby("country")
    .size()
    .reset_index(name="Players")
    .sort_values("Players", ascending=False)
    .head(10)
)

fig = px.bar(
    country_players,
    x="country",
    y="Players",
    title="Top 10 Countries by Players",
    text="Players"
)

fig.show()

#  top 20 rank player 
top_players = (
    rankings
    .merge(competitors, on="competitor_id")
    .sort_values("rank_position")
    .head(20)
)

fig = px.bar(
    top_players,
    x="competitor_name",
    y="points",
    title="Top 20 Ranked Players",
    text="points"
)

fig.show()

# top 10 countries by venues
venue_country = (
    venues
    .groupby("country_name")
    .size()
    .reset_index(name="Venues")
    .sort_values("Venues", ascending=False)
    .head(10)
)

fig = px.bar(
    venue_country,
    x="country_name",
    y="Venues",
    title="Top 10 Countries by Venues",
    text="Venues"
)

fig.show()

# ranking distribution 

fig = px.histogram(
    rankings,
    x="points",
    nbins=30,
    title="Ranking Points Distribution"
)

fig.show()

# player ranking scatter plot
player_rank = rankings.merge(
    competitors,
    on="competitor_id"
)

fig = px.scatter(
    player_rank,
    x="rank_position",
    y="points",
    hover_name="competitor_name",
    title="Player Rankings vs Points"
)

fig.show()