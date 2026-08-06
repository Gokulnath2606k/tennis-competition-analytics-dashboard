from sqlalchemy import create_engine

# Update these values if needed
USERNAME = "root"
PASSWORD = "k.gokulnath2606"
HOST = "localhost"
PORT = "3306"
DATABASE = "tennis_analytics"

engine = create_engine(
    f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

print("✅ MySQL Engine Created Successfully")