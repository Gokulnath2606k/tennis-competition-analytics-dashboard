import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = st.secrets["DATABASE_URL"]

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"connect_timeout": 10}
)

def run_query(query):
    return pd.read_sql(query, engine)
