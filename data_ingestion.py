import pandas as pd
import os

folder_path = "data/raw"

for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        path = os.path.join(folder_path, file)

        df = pd.read_csv(path)

        print("\n" + "=" * 50)
        print(f"FILE: {file}")
        print("=" * 50)

        print("Shape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())