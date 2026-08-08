import streamlit as st
from sqlalchemy import create_engine, text

st.title("Railway MySQL Connection Test")

try:
    DATABASE_URL = st.secrets["DATABASE_URL"]

    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,
        connect_args={"connect_timeout": 10}
    )

    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        st.success("✅ Railway MySQL connected successfully!")
        st.write(result.fetchone())

except Exception as e:
    st.error("❌ Database connection failed")
    st.write(type(e).__name__)
    st.write(e)
