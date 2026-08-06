# 🎾 Tennis Competition Analytics Dashboard

An interactive data analytics dashboard built using **SportRadar Tennis API**, **MySQL**, **Python**, **Plotly**, and **Streamlit**. The dashboard provides comprehensive insights into tennis competitions, players, venues, and countries through interactive visualizations and filters.

---

# 📌 Project Overview

This project collects tennis competition data from the SportRadar API, stores it in a MySQL database, processes it using Python, and visualizes the data in an interactive Streamlit dashboard.

The dashboard helps users analyze:

- 🎾 Tennis Competitions
- 🏆 Player Rankings
- 🌍 Country Statistics
- 🏟 Venue Information

---

# 🚀 Features

## 🏠 Home Dashboard

- KPI Cards
  - Total Competitions
  - Total Players
  - Total Venues
  - Total Categories
  - Total Complexes

- Competition Overview
- Top Countries by Players
- Gender Distribution
- Venue Distribution
- Top 20 Ranked Players

---

## 🎾 Competition Analysis

- Competitions by Category
- Competition Type Distribution
- Competition Gender Distribution
- Category vs Gender
- Category vs Competition Type
- Top Competitions
- Competition Details Table

### Interactive Filters

- Category
- Competition Type
- Gender

---

## 🏆 Player Rankings

- Top Players by Ranking Points
- Competitions Played
- Ranking Movement
- Ranking Points by Country
- Average Points by Country
- Top Countries by Players
- Player Distribution

### Interactive Filters

- Country
- Minimum Ranking Points
- Top N Players

---

## 🌍 Country Analysis

- Players by Country
- Venues by Country
- Ranking Points by Country
- Average Ranking Points
- Top Countries
- Country Distribution
- Player Distribution

### Interactive Filters

- Country
- Minimum Ranking Points
- Top N Countries

---

## 🏟 Venue Analysis

- Venues by Country
- Top Cities by Venues
- Complexes by Country
- Venues per Complex
- Venue Distribution by Country
- Venue Distribution by City
- Top 20 Venues

### Interactive Filters

- Country
- City
- Complex
- Top N Venues

---

# 🛠 Tech Stack

- Python
- Streamlit
- MySQL
- SQLAlchemy
- Pandas
- Plotly Express
- PyMySQL
- SportRadar Tennis API

---

# 📂 Project Structure

```
game_analysis/
│
├── app.py
├── db.py
├── queries.py
├── requirements.txt
├── README.md
│
├── charts/
│   ├── competition_charts.py
│   ├── player_charts.py
│   ├── country_charts.py
│   └── venue_charts.py
│
├── pages/
│   ├── Competition_Analysis.py
│   ├── Player_Rankings.py
│   ├── Country_Analysis.py
│   ├── Venue_Analysis.py
│   └── Project_Info.py
│
└── assets/
```

---

# 📊 Database Tables

- competitions
- competitors
- rankings
- venues
- complexes
- categories

---

# 🔄 Project Workflow

```
SportRadar API
       │
       ▼
Python ETL
       │
       ▼
MySQL Database
       │
       ▼
SQL Queries
       │
       ▼
Pandas Data Processing
       │
       ▼
Plotly Visualizations
       │
       ▼
Streamlit Dashboard
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/tennis-competition-analytics-dashboard.git
```

Move into the project directory

```bash
cd tennis-competition-analytics-dashboard
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

# 📈 Dashboard Highlights

- Interactive visualizations
- Dynamic filters
- KPI Dashboard
- Responsive layout
- Clean user interface
- Data-driven insights

---

# 🎯 Learning Outcomes

This project demonstrates:

- API Integration
- ETL Pipeline Development
- SQL Query Writing
- Database Design
- Data Cleaning
- Data Analysis
- Interactive Dashboard Development
- Data Visualization
- Streamlit Application Development

---

# 👨‍💻 Developed By

**Gokul K**

B.Tech Artificial Intelligence & Data Science

Aspiring Data Analyst

---

# ⭐ If you found this project useful, consider giving it a star!
