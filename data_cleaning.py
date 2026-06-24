import pandas as pd
import os

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)

files = [f for f in os.listdir(RAW_PATH) if f.endswith(".csv")]

for file in files:
    path = os.path.join(RAW_PATH, file)

    print(f"Processing {file}")

    df = pd.read_csv(path)

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert date columns automatically
    for col in df.columns:
        if "date" in col.lower():
            try:
                df[col] = pd.to_datetime(df[col])
            except:
                pass

    # Save cleaned file
    output_path = os.path.join(PROCESSED_PATH, file)
    df.to_csv(output_path, index=False)

    print(f"Saved cleaned {file}")

print("All files cleaned successfully!")