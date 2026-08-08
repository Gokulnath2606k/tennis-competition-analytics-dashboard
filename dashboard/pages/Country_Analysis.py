import streamlit as st
from db import run_query
from charts.country_charts import (
    players_country_chart,
    venues_country_chart,
    points_country_chart,
    average_points_chart,
    top_players_chart,
    player_distribution_chart,
    top_country_points_chart
)

st.set_page_config(
    page_title="Country Analysis",
    page_icon="🌍",
    layout="wide"
)

st.markdown(
"""
<h1 style='text-align:center;font-weight:bold;'>
🌍 Country Analysis Dashboard
</h1>
""",
unsafe_allow_html=True
)

st.markdown("---")

# ==========================================================
# SIDEBAR FILTERS
# ==========================================================

st.sidebar.header("🌍 Country Filters")

# Country Filter
countries = run_query("""
SELECT DISTINCT country
FROM competitors
WHERE country IS NOT NULL
ORDER BY country;
""")

selected_country = st.sidebar.selectbox(
    "Country",
    ["All"] + countries["country"].tolist()
)

# Minimum Ranking Points
min_points = st.sidebar.slider(
    "Minimum Ranking Points",
    0,
    12000,
    0,
    100
)

# Top N Countries
top_n = st.sidebar.slider(
    "Top Countries",
    5,
    30,
    10
)

# ==========================================================
# WHERE CLAUSE
# ==========================================================

filters = [
    f"r.points >= {min_points}"
]

if selected_country != "All":
    filters.append(f"c.country='{selected_country}'")

where_clause = "WHERE " + " AND ".join(filters)

# ==========================================================
# CHART 1
# Players by Country
# ==========================================================

players = run_query(f"""
SELECT
    c.country,
    COUNT(*) AS total_players
FROM competitors c
JOIN rankings r
ON c.competitor_id=r.competitor_id

{where_clause}

GROUP BY c.country
ORDER BY total_players DESC
LIMIT {top_n};
""")

st.plotly_chart(
    players_country_chart(players),
    use_container_width=True
)

st.markdown("---")

# ==========================================================
# CHART 2
# Venues by Country
# ==========================================================

venues = run_query(f"""
SELECT
    country_name,
    COUNT(*) AS total_venues
FROM venues

{"WHERE country_name='"+selected_country+"'" if selected_country!="All" else ""}

GROUP BY country_name
ORDER BY total_venues DESC
LIMIT {top_n};
""")

# ==========================================================
# CHART 3
# Ranking Points
# ==========================================================

points = run_query(f"""
SELECT
    c.country,
    SUM(r.points) AS total_points
FROM competitors c
JOIN rankings r
ON c.competitor_id=r.competitor_id

{where_clause}

GROUP BY c.country
ORDER BY total_points DESC
LIMIT {top_n};
""")

col1,col2=st.columns(2)

with col1:
    st.plotly_chart(
        venues_country_chart(venues),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        points_country_chart(points),
        use_container_width=True
    )

st.markdown("---")

# ==========================================================
# CHART 4
# Average Points
# ==========================================================

average = run_query(f"""
SELECT
    c.country,
    AVG(r.points) AS avg_points
FROM competitors c
JOIN rankings r
ON c.competitor_id=r.competitor_id

{where_clause}

GROUP BY c.country
ORDER BY avg_points DESC
LIMIT {top_n};
""")

st.plotly_chart(
    average_points_chart(average),
    use_container_width=True
)

st.markdown("---")

# ==========================================================
# CHART 5
# Top Players
# ==========================================================

top = run_query(f"""
SELECT
    c.country,
    COUNT(*) AS top_players
FROM competitors c
JOIN rankings r
ON c.competitor_id=r.competitor_id

{where_clause}

GROUP BY c.country
ORDER BY top_players DESC
LIMIT {top_n};
""")

# ==========================================================
# CHART 6
# Player Distribution
# ==========================================================

distribution = run_query(f"""
SELECT
    c.country,
    COUNT(*) AS players
FROM competitors c
JOIN rankings r
ON c.competitor_id=r.competitor_id

{where_clause}

GROUP BY c.country
ORDER BY players DESC
LIMIT {top_n};
""")

col3,col4=st.columns(2)

with col3:
    st.plotly_chart(
        top_players_chart(top),
        use_container_width=True
    )

with col4:
    st.plotly_chart(
        player_distribution_chart(distribution),
        use_container_width=True
    )

st.markdown("---")

# ==========================================================
# CHART 7
# Top Countries by Points
# ==========================================================

country_points = run_query(f"""
SELECT
    c.country,
    SUM(r.points) AS total_points
FROM competitors c
JOIN rankings r
ON c.competitor_id=r.competitor_id

{where_clause}

GROUP BY c.country
ORDER BY total_points DESC
LIMIT {top_n};
""")

st.plotly_chart(
    top_country_points_chart(country_points),
    use_container_width=True
)
