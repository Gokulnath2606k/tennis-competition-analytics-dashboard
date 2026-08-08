import streamlit as st
from db import run_query
from charts.competition_charts import (
    competition_category_chart,
    competition_type_chart,
    competition_gender_chart,
    category_gender_chart,
    category_type_chart,
    top_competition_chart
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Competition Analysis",
    page_icon="🎾",
    layout="wide"
)

st.markdown(
    """
    <h1 style="text-align:center;font-weight:bold;">
        🎾 Competition Analysis Dashboard
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# =====================================================
# SIDEBAR FILTERS
# =====================================================

st.sidebar.header("🔍 Competition Filters")

categories = run_query("""
SELECT DISTINCT category_name
FROM categories
ORDER BY category_name;
""")

types = run_query("""
SELECT DISTINCT type
FROM competitions
WHERE type IS NOT NULL
ORDER BY type;
""")

genders = run_query("""
SELECT DISTINCT gender
FROM competitions
WHERE gender IS NOT NULL
ORDER BY gender;
""")

selected_category = st.sidebar.selectbox(
    "Category",
    ["All"] + categories["category_name"].tolist()
)

selected_type = st.sidebar.selectbox(
    "Competition Type",
    ["All"] + types["type"].tolist()
)

selected_gender = st.sidebar.selectbox(
    "Gender",
    ["All"] + genders["gender"].tolist()
)

# =====================================================
# BUILD WHERE CLAUSE
# =====================================================

filters = []

if selected_category != "All":
    filters.append(f"cat.category_name='{selected_category}'")

if selected_type != "All":
    filters.append(f"c.type='{selected_type}'")

if selected_gender != "All":
    filters.append(f"c.gender='{selected_gender}'")

where_clause = ""

if filters:
    where_clause = "WHERE " + " AND ".join(filters)

# =====================================================
# CHART 1
# =====================================================

competition = run_query(f"""
SELECT
    cat.category_name,
    COUNT(*) AS competitions
FROM competitions c
JOIN categories cat
ON c.category_id = cat.category_id

{where_clause}

GROUP BY cat.category_name
ORDER BY competitions DESC;
""")

st.plotly_chart(
    competition_category_chart(competition),
    use_container_width=True
)

st.markdown("---")

# =====================================================
# CHART 2 & 3
# =====================================================

competition_type = run_query(f"""
SELECT
    c.type,
    COUNT(*) AS competitions
FROM competitions c
JOIN categories cat
ON c.category_id = cat.category_id

{where_clause}

GROUP BY c.type;
""")

gender = run_query(f"""
SELECT
    c.gender,
    COUNT(*) AS competitions
FROM competitions c
JOIN categories cat
ON c.category_id = cat.category_id

{where_clause}

GROUP BY c.gender;
""")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        competition_type_chart(competition_type),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        competition_gender_chart(gender),
        use_container_width=True
    )

st.markdown("---")

# =====================================================
# CHART 4
# =====================================================

category_gender = run_query(f"""
SELECT
    cat.category_name,
    c.gender,
    COUNT(*) AS total
FROM competitions c
JOIN categories cat
ON c.category_id = cat.category_id

{where_clause}

GROUP BY cat.category_name, c.gender;
""")

st.plotly_chart(
    category_gender_chart(category_gender),
    use_container_width=True
)

st.markdown("---")

# =====================================================
# CHART 5
# =====================================================

category_type = run_query(f"""
SELECT
    cat.category_name,
    c.type,
    COUNT(*) AS total
FROM competitions c
JOIN categories cat
ON c.category_id = cat.category_id

{where_clause}

GROUP BY cat.category_name, c.type;
""")

st.plotly_chart(
    category_type_chart(category_type),
    use_container_width=True
)

st.markdown("---")

# =====================================================
# CHART 6 & 7
# =====================================================

top = run_query(f"""
SELECT
    c.competition_name,
    COUNT(*) AS competitions
FROM competitions c
JOIN categories cat
ON c.category_id = cat.category_id

{where_clause}

GROUP BY c.competition_name
ORDER BY competitions DESC
LIMIT 20;
""")

st.plotly_chart(
    top_competition_chart(top),
    use_container_width=True
)

st.markdown("---")

st.subheader("🏆 Top 20 Competition Names")

st.dataframe(
    top,
    use_container_width=True,
    hide_index=True
)
