import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("\nUNIQUE FUND HOUSES:")
print(fund_master["fund_house"].unique())

print("\nUNIQUE CATEGORIES:")
print(fund_master["category"].unique())

print("\nUNIQUE SUB-CATEGORIES:")
print(fund_master["sub_category"].unique())

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("\nAMFI CODE VALIDATION")
print(f"Codes in fund_master: {len(fund_codes)}")
print(f"Codes in nav_history: {len(nav_codes)}")
print(f"Missing codes: {len(missing_codes)}")

if len(missing_codes) > 0:
    print(missing_codes)
else:
    print("All AMFI codes validated successfully")