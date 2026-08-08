import streamlit as st
from dashboard.db import run_query
from queries import (
    VENUES_BY_COUNTRY,
    VENUES_BY_CITY,
    TOP20_VENUES,
    COMPLEXES_BY_COUNTRY,
    VENUES_PER_COMPLEX,
    CITY_DISTRIBUTION,
    COUNTRY_DISTRIBUTION
)

from charts.venue_charts import (
    venue_country_chart,
    venue_city_chart,
    complexes_country_chart,
    venues_complex_chart,
    city_distribution_chart,
    country_distribution_chart
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Venue Analysis",
    page_icon="🏟",
    layout="wide"
)

st.markdown(
"""
<h1 style="text-align:center;font-weight:bold;">
🏟 Venue Analysis Dashboard
</h1>
""",
unsafe_allow_html=True
)

st.markdown("---")

# =====================================================
# FILTERS
# =====================================================

st.sidebar.header("🏟 Venue Filters")

# Country

countries = run_query("""
SELECT DISTINCT country_name
FROM venues
WHERE country_name IS NOT NULL
ORDER BY country_name
""")

selected_country = st.sidebar.selectbox(
    "Country",
    ["All"] + countries["country_name"].tolist()
)

# City

cities = run_query(f"""
SELECT DISTINCT city_name
FROM venues
{"WHERE country_name='"+selected_country+"'" if selected_country!="All" else ""}
ORDER BY city_name
""")

selected_city = st.sidebar.selectbox(
    "City",
    ["All"] + cities["city_name"].dropna().tolist()
)

# Complex

complexes = run_query("""
SELECT DISTINCT complex_name
FROM complexes
ORDER BY complex_name
""")

selected_complex = st.sidebar.selectbox(
    "Complex",
    ["All"] + complexes["complex_name"].tolist()
)

# Top N

top_n = st.sidebar.slider(
    "Top Venues",
    5,
    30,
    10
)

# =====================================================
# WHERE CLAUSE
# =====================================================

filters=[]

if selected_country!="All":
    filters.append(f"v.country_name='{selected_country}'")

if selected_city!="All":
    filters.append(f"v.city_name='{selected_city}'")

if selected_complex!="All":
    filters.append(f"cx.complex_name='{selected_complex}'")

where_clause=""

if filters:
    where_clause="WHERE "+" AND ".join(filters)

# =====================================================
# CHART 1
# =====================================================

country = run_query(VENUES_BY_COUNTRY(where_clause,top_n))

st.plotly_chart(
    venue_country_chart(country),
    use_container_width=True
)

st.markdown("---")

# =====================================================
# CHART 2 & 3
# =====================================================

city = run_query(VENUES_BY_CITY(where_clause,top_n))

complexes = run_query(COMPLEXES_BY_COUNTRY(where_clause,top_n))

col1,col2=st.columns(2)

with col1:

    st.plotly_chart(
        venue_city_chart(city),
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        complexes_country_chart(complexes),
        use_container_width=True
    )

st.markdown("---")

# =====================================================
# CHART 4
# =====================================================

complex_chart=run_query(
    VENUES_PER_COMPLEX(where_clause,top_n)
)

st.plotly_chart(
    venues_complex_chart(complex_chart),
    use_container_width=True
)

st.markdown("---")

# =====================================================
# CHART 5 & 6
# =====================================================

city_dist=run_query(
    CITY_DISTRIBUTION(where_clause,top_n)
)

country_dist=run_query(
    COUNTRY_DISTRIBUTION(where_clause,top_n)
)

col3,col4=st.columns(2)

with col3:

    st.plotly_chart(
        city_distribution_chart(city_dist),
        use_container_width=True
    )

with col4:

    st.plotly_chart(
        country_distribution_chart(country_dist),
        use_container_width=True
    )

st.markdown("---")

# =====================================================
# TOP VENUES TABLE
# =====================================================

st.subheader("🏟 Top Venues")

venues=run_query(
    TOP20_VENUES(where_clause)
)

st.dataframe(
    venues,
    use_container_width=True,
    hide_index=True
)
