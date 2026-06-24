import pandas as pd
import os
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

PROCESSED_PATH = "data/processed"

files = [f for f in os.listdir(PROCESSED_PATH) if f.endswith(".csv")]

for file in files:
    table_name = file.replace(".csv", "").replace("-", "_")

    print(f"Loading {table_name}...")

    df = pd.read_csv(os.path.join(PROCESSED_PATH, file))

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

print("\nDatabase created successfully!")