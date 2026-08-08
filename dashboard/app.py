import streamlit as st

from db import run_query
from charts.executive_charts import (
    competition_category_chart,
    player_country_chart,
    gender_chart,
    venue_country_chart
)


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Tennis Competition Analytics",
    page_icon="🎾",
    layout="wide"
)


# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.markdown(
    """
    <h2 style="
        text-align:center;
        font-weight:bold;
    ">
        🎾 Tennis Analytics
    </h2>
    """,
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Competition Analysis",
        "Player Rankings",
        "Venue Analysis",
        "Country Analysis",
        "About Project"
    ]
)


# =====================================================
# HOME PAGE
# =====================================================

if page == "Home":

    # -------------------------------------------------
    # Dashboard Title
    # -------------------------------------------------

    st.markdown(
        """
        <h1 style="
            text-align:center;
            font-size:42px;
            font-weight:bold;
            margin-bottom:5px;
        ">
            🎾 Tennis Competition Analytics Dashboard
        </h1>

        <p style="
            text-align:center;
            font-size:18px;
            color:gray;
        ">
            SportRadar API | Python | MySQL | Plotly | Streamlit
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")


    # =================================================
    # KPI CARDS
    # =================================================

    kpi = run_query("""
        SELECT
            (SELECT COUNT(*) FROM competitions)
                AS total_competitions,

            (SELECT COUNT(*) FROM competitors)
                AS total_players,

            (SELECT COUNT(*) FROM venues)
                AS total_venues,

            (SELECT COUNT(*) FROM categories)
                AS total_categories,

            (SELECT COUNT(*) FROM complexes)
                AS total_complexes
    """)

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "🎾 Competitions",
        int(kpi.iloc[0]["total_competitions"])
    )

    col2.metric(
        "👤 Players",
        int(kpi.iloc[0]["total_players"])
    )

    col3.metric(
        "🏟 Venues",
        int(kpi.iloc[0]["total_venues"])
    )

    col4.metric(
        "📂 Categories",
        int(kpi.iloc[0]["total_categories"])
    )

    col5.metric(
        "🏢 Complexes",
        int(kpi.iloc[0]["total_complexes"])
    )

    st.markdown("---")


    # =================================================
    # CHART 1 - COMPETITIONS BY CATEGORY
    # =================================================

    competition = run_query("""
        SELECT
            cat.category_name,
            COUNT(*) AS competitions
        FROM competitions c

        JOIN categories cat
            ON c.category_id = cat.category_id

        GROUP BY cat.category_name

        ORDER BY competitions DESC
    """)

    st.plotly_chart(
        competition_category_chart(competition),
        use_container_width=True
    )

    st.markdown("---")


    # =================================================
    # CHART 2 - TOP COUNTRIES BY PLAYERS
    # =================================================

    players_country = run_query("""
        SELECT
            country,
            COUNT(*) AS players

        FROM competitors

        WHERE country IS NOT NULL

        GROUP BY country

        ORDER BY players DESC

        LIMIT 10
    """)

    st.plotly_chart(
        player_country_chart(players_country),
        use_container_width=True
    )

    st.markdown("---")


    # =================================================
    # CHART 3 & 4
    # =================================================

    gender = run_query("""
        SELECT
            gender,
            COUNT(*) AS competitions

        FROM competitions

        WHERE gender IS NOT NULL

        GROUP BY gender
    """)


    venue = run_query("""
        SELECT
            country_name,
            COUNT(*) AS venues

        FROM venues

        WHERE country_name IS NOT NULL

        GROUP BY country_name

        ORDER BY venues DESC

        LIMIT 10
    """)


    col1, col2 = st.columns(2)


    # Gender Chart
    with col1:

        st.plotly_chart(
            gender_chart(gender),
            use_container_width=True
        )


    # Venue Chart
    with col2:

        st.plotly_chart(
            venue_country_chart(venue),
            use_container_width=True
        )

    st.markdown("---")


    # =================================================
    # TOP 20 PLAYERS
    # =================================================

    st.markdown(
        """
        <h2 style="
            text-align:center;
            font-size:28px;
            font-weight:bold;
        ">
            🏆 Top 20 Ranked Players
        </h2>
        """,
        unsafe_allow_html=True
    )


    top_players = run_query("""
        SELECT
            r.rank_position,
            c.competitor_name,
            c.country,
            r.points,
            r.competitions_played

        FROM rankings r

        JOIN competitors c
            ON r.competitor_id = c.competitor_id

        ORDER BY r.rank_position

        LIMIT 20
    """)


    st.dataframe(
        top_players,
        use_container_width=True,
        hide_index=True
    )


# =====================================================
# COMPETITION ANALYSIS
# =====================================================

elif page == "Competition Analysis":

    st.markdown(
        """
        <h1 style="
            text-align:center;
            font-weight:bold;
        ">
            🎾 Competition Analysis
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.info(
        "Open the Competition Analysis page from the Streamlit pages section."
    )


# =====================================================
# PLAYER RANKINGS
# =====================================================

elif page == "Player Rankings":

    st.markdown(
        """
        <h1 style="
            text-align:center;
            font-weight:bold;
        ">
            🏆 Player Rankings
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.info(
        "Open the Player Rankings page from the Streamlit pages section."
    )


# =====================================================
# VENUE ANALYSIS
# =====================================================

elif page == "Venue Analysis":

    st.markdown(
        """
        <h1 style="
            text-align:center;
            font-weight:bold;
        ">
            🏟 Venue Analysis
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.info(
        "Open the Venue Analysis page from the Streamlit pages section."
    )


# =====================================================
# COUNTRY ANALYSIS
# =====================================================

elif page == "Country Analysis":

    st.markdown(
        """
        <h1 style="
            text-align:center;
            font-weight:bold;
        ">
            🌍 Country Analysis
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.info(
        "Open the Country Analysis page from the Streamlit pages section."
    )


# =====================================================
# ABOUT PROJECT
# =====================================================

elif page == "About Project":

    st.markdown(
        """
        <h1 style="
            text-align:center;
            font-size:42px;
            font-weight:bold;
        ">
            ℹ️ About Project
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        """
        <h2 style="font-size:24px; font-weight:bold;">
            🎾 Tennis Competition Analytics
        </h2>

        <p style="font-size:18px;">
            This project analyzes tennis competition, player,
            ranking, venue and country data using an end-to-end
            data analytics workflow.
        </p>


        <h2 style="font-size:24px; font-weight:bold;">
            🛠 Technology Stack
        </h2>

        <p style="font-size:18px;">
            • Python<br>
            • SportRadar API<br>
            • MySQL<br>
            • SQLAlchemy<br>
            • Pandas<br>
            • Plotly<br>
            • Streamlit
        </p>


        <h2 style="font-size:24px; font-weight:bold;">
            ⚙️ Project Workflow
        </h2>

        <p style="
            font-size:20px;
            font-weight:bold;
            text-align:center;
        ">
            SportRadar API
            ➜ Python ETL
            ➜ MySQL
            ➜ SQL Analysis
            ➜ Plotly
            ➜ Streamlit Dashboard
        </p>


        <h2 style="font-size:24px; font-weight:bold;">
            📊 Dashboard Modules
        </h2>

        <p style="font-size:18px;">
            🏠 Home Dashboard<br><br>

            🎾 Competition Analysis<br><br>

            🏆 Player Rankings<br><br>

            🏟 Venue Analysis<br><br>

            🌍 Country Analysis
        </p>
        """,
        unsafe_allow_html=True
    )
