import pandas as pd
import os

# Ensure output folders exist
os.makedirs("bronze", exist_ok=True)
os.makedirs("silver", exist_ok=True)
os.makedirs("gold", exist_ok=True)

# ===============================
# 1. Bronze Layer (Raw Ingestion)
# ===============================
raw_df = pd.read_csv("data/ride_requests_200.csv")
bronze_path = "bronze/ride_requests.csv"
raw_df.to_csv(bronze_path, index=False)

print("✅ Bronze layer saved:", bronze_path)
print(raw_df.head(), "\n")

# ===============================
# 2. Silver Layer (Cleansed Data)
# ===============================
silver_df = raw_df.copy()
silver_df = silver_df.drop_duplicates()

# Fill missing values
for col in silver_df.select_dtypes(include="object").columns:
    silver_df[col] = silver_df[col].fillna("Unknown")

for col in silver_df.select_dtypes(include="number").columns:
    silver_df[col] = silver_df[col].fillna(silver_df[col].mean())

# Ensure numeric column 'Amount'
if "Amount" in silver_df.columns:
    silver_df["Amount"] = pd.to_numeric(silver_df["Amount"], errors="coerce").fillna(0)

silver_path = "silver/ride_requests_cleaned.csv"
silver_df.to_csv(silver_path, index=False)

print("✅ Silver layer saved:", silver_path)
print(silver_df.head(), "\n")

# ===============================
# 3. Gold Layer (Aggregated Data)
# ===============================
if "Status" in silver_df.columns and "Amount" in silver_df.columns:
    gold_df = silver_df.groupby("Status", as_index=False).agg(
        Avg_Amount=("Amount", "mean"),
        Total_Rides=("Amount", "count")
    )
else:
    gold_df = pd.DataFrame()

gold_path = "gold/ride_fare_summary.csv"
gold_df.to_csv(gold_path, index=False)

print("✅ Gold layer saved:", gold_path)
print(gold_df, "\n")
