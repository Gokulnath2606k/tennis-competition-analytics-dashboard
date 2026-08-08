import streamlit as st
from dashboard.db import run_query
from queries import (
    TOP_20_PLAYERS,
    TOP_PLAYERS_POINTS,
    TOP_PLAYERS_COMPETITIONS,
    RANKING_MOVEMENT,
    POINTS_BY_COUNTRY,
    AVERAGE_POINTS_COUNTRY,
    TOP10_COUNTRIES
)

from charts.player_charts import (
    top_players_points_chart,
    competitions_played_chart,
    ranking_movement_chart,
    country_points_chart,
    average_points_chart,
    top_countries_chart,
    player_distribution_chart
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Player Rankings",
    page_icon="🏆",
    layout="wide"
)

st.markdown(
"""
<h1 style="text-align:center;font-weight:bold;">
🏆 Player Rankings Dashboard
</h1>
""",
unsafe_allow_html=True
)

st.markdown("---")

# =====================================================
# SIDEBAR FILTERS
# =====================================================

st.sidebar.header("🏆 Player Ranking Filters")

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

# Rank Filter

max_rank = st.sidebar.slider(
    "Maximum Rank Position",
    10,
    500,
    100,
    10
)

# Points Filter

min_points = st.sidebar.slider(
    "Minimum Ranking Points",
    0,
    12000,
    0,
    100
)

# =====================================================
# WHERE CLAUSE
# =====================================================

filters = [
    f"r.rank_position <= {max_rank}",
    f"r.points >= {min_points}"
]

if selected_country != "All":
    filters.append(f"c.country='{selected_country}'")

where_clause = "WHERE " + " AND ".join(filters)

# =====================================================
# CHART 1
# =====================================================

points = run_query(
    TOP_PLAYERS_POINTS(where_clause)
)

st.plotly_chart(
    top_players_points_chart(points),
    use_container_width=True
)

st.markdown("---")

# =====================================================
# CHART 2 & 3
# =====================================================

competitions = run_query(
    TOP_PLAYERS_COMPETITIONS(where_clause)
)

movement = run_query(
    RANKING_MOVEMENT(where_clause)
)

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        competitions_played_chart(competitions),
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        ranking_movement_chart(movement),
        use_container_width=True
    )

st.markdown("---")

# =====================================================
# CHART 4
# =====================================================

country_points = run_query(
    POINTS_BY_COUNTRY(where_clause)
)

st.plotly_chart(
    country_points_chart(country_points),
    use_container_width=True
)

st.markdown("---")

# =====================================================
# CHART 5
# =====================================================

avg_points = run_query(
    AVERAGE_POINTS_COUNTRY(where_clause)
)

st.plotly_chart(
    average_points_chart(avg_points),
    use_container_width=True
)

st.markdown("---")

# =====================================================
# CHART 6 & 7
# =====================================================

countries = run_query(
    TOP10_COUNTRIES(where_clause)
)

col3, col4 = st.columns(2)

with col3:

    st.plotly_chart(
        top_countries_chart(countries),
        use_container_width=True
    )

with col4:

    st.plotly_chart(
        player_distribution_chart(countries),
        use_container_width=True
    )

st.markdown("---")

# =====================================================
# TOP 20 PLAYERS TABLE
# =====================================================

st.subheader("🏅 Top Ranked Players")

top20 = run_query(
    TOP_20_PLAYERS(where_clause)
)

st.dataframe(
    top20,
    use_container_width=True,
    hide_index=True
)
