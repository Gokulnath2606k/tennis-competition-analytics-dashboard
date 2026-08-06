from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "mysql+pymysql://root:k.gokulnath2606@localhost:3306/tennis_analytics"
)

def run_query(query):
    return pd.read_sql(query, engine)