import pandas as pd
import os

RAW_PATH = "data/raw"

files = [f for f in os.listdir(RAW_PATH) if f.endswith(".csv")]

for file in files:
    print("\n" + "="*50)
    print(file)

    df = pd.read_csv(os.path.join(RAW_PATH, file))

    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("Duplicates:", df.duplicated().sum())

    missing = df.isnull().sum()
    print("\nMissing Values:")
    print(missing[missing > 0])

print("\nAll files checked!")