import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)

# =====================================================
# TITLE
# =====================================================

st.markdown(
    "<h1 style='text-align:center; font-size:42px;'>🎾 Tennis Analytics Dashboard</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# =====================================================
# PROJECT OVERVIEW
# =====================================================

st.markdown(
    "<h2 style='font-size:24px;'>📌 Project Overview</h2>",
    unsafe_allow_html=True
)

st.write("""
This project is a complete Tennis Competition Analytics Dashboard developed
using the SportRadar Tennis API.

The project demonstrates the complete Data Analytics lifecycle including:

• API Data Collection

• ETL Pipeline Development

• MySQL Database Design

• Advanced SQL Analytics

• Python Data Analysis

• Interactive Streamlit Dashboard

The dashboard enables users to analyze tennis competitions,
player rankings, venues and country-level insights through interactive
visualizations.
""")

st.markdown("---")

# =====================================================
# PROJECT OBJECTIVES
# =====================================================

st.markdown(
    "<h2 style='font-size:24px;'>🎯 Project Objectives</h2>",
    unsafe_allow_html=True
)

st.write("""
✔ Collect live tennis data from SportRadar API

✔ Store structured data in MySQL

✔ Build normalized database tables

✔ Perform SQL analytics

✔ Analyze player rankings

✔ Analyze competition categories

✔ Analyze countries and venues

✔ Build an interactive business dashboard
""")

st.markdown("---")

# =====================================================
# TECHNOLOGY STACK
# =====================================================

st.markdown(
    "<h2 style='font-size:24px;'>🛠 Technology Stack</h2>",
    unsafe_allow_html=True
)

st.table({
    "Technology":[
        "Python",
        "SportRadar API",
        "MySQL",
        "SQL",
        "Pandas",
        "Plotly",
        "Streamlit",
        "GitHub"
    ],
    "Purpose":[
        "ETL & Data Processing",
        "Data Source",
        "Database",
        "Analytics",
        "Data Analysis",
        "Interactive Charts",
        "Dashboard",
        "Version Control"
    ]
})

st.markdown("---")

# =====================================================
# DATABASE TABLES
# =====================================================

st.markdown(
    "<h2 style='font-size:24px;'>🗄 Database Tables</h2>",
    unsafe_allow_html=True
)

st.table({
    "Table":[
        "categories",
        "competitions",
        "competitors",
        "complexes",
        "venues",
        "rankings"
    ],
    "Description":[
        "Competition Categories",
        "Competition Information",
        "Player Information",
        "Sports Complexes",
        "Venue Information",
        "Player Rankings"
    ]
})

st.markdown("---")

# =====================================================
# DASHBOARD MODULES
# =====================================================

st.markdown(
    "<h2 style='font-size:24px;'>📊 Dashboard Modules</h2>",
    unsafe_allow_html=True
)

st.write("""
🏠 Home Dashboard

• KPI Cards

• Top Ranked Players

• Project Summary

🎾 Competition Analysis

• Competition Categories

• Competition Types

• Gender Analysis

• Parent Competitions

• Category vs Gender

• Category vs Type

🌍 Country Analysis

• Players by Country

• Venues by Country

• Ranking Points by Country

• Average Ranking Points

• Player Distribution

🏆 Player Rankings

• Top Players

• Ranking Points

• Competitions Played

• Ranking Movement

• Country Rankings
""")

st.markdown("---")

# =====================================================
# PROJECT WORKFLOW
# =====================================================

st.markdown(
    "<h2 style='font-size:24px;'>⚙ Project Workflow</h2>",
    unsafe_allow_html=True
)

st.write("""
SportRadar API

⬇

Python ETL Pipeline

⬇

JSON Files

⬇

MySQL Database

⬇

Advanced SQL Queries

⬇

Python (Pandas)

⬇

Plotly Visualizations

⬇

Streamlit Dashboard
""")

st.markdown("---")

# =====================================================
# KEY FEATURES
# =====================================================

st.markdown(
    "<h2 style='font-size:24px;'>⭐ Key Features</h2>",
    unsafe_allow_html=True
)

st.write("""
✔ API Integration

✔ Automated ETL Pipeline

✔ Normalized Relational Database

✔ Advanced SQL Queries

✔ Interactive Charts

✔ Business KPIs

✔ Responsive Dashboard

✔ Data-Driven Insights
""")

st.markdown("---")

# =====================================================
# DEVELOPER
# =====================================================

st.markdown(
    "<h2 style='font-size:24px;'>👨‍💻 Developer</h2>",
    unsafe_allow_html=True
)

st.info("""
Name : Gokulnath K

Role : Data Analyst

Skills :

• Python

• SQL

• MySQL

• Streamlit

• Power BI

• Excel

• API Integration

• Data Visualization
""")