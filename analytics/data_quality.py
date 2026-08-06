import pandas as pd
from db_connection import engine

# Load Tables
tables = {
    "Competitions": pd.read_sql("SELECT * FROM competitions", engine),
    "Categories": pd.read_sql("SELECT * FROM categories", engine),
    "Competitors": pd.read_sql("SELECT * FROM competitors", engine),
    "Rankings": pd.read_sql("SELECT * FROM rankings", engine),
    "Complexes": pd.read_sql("SELECT * FROM complexes", engine),
    "Venues": pd.read_sql("SELECT * FROM venues", engine)
}

print("=" * 70)
print("TENNIS COMPETITION ANALYSIS - DATA QUALITY REPORT")
print("=" * 70)

for table_name, df in tables.items():

    print(f"\n📌 Table : {table_name}")
    print("-" * 70)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn Names")
    print(df.columns.tolist())

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    print("\nData Types")
    print(df.dtypes)

print("\n" + "=" * 70)
print("✅ Data Quality Assessment Completed")
print("=" * 70)