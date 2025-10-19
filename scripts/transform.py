# scripts/transform.py
import pathlib
import pandas as pd

DATA_DIR = pathlib.Path("/opt/airflow/data")
RAW = DATA_DIR / "raw" / "listings.csv"
PROCESSED_DIR = DATA_DIR / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
OUT = PROCESSED_DIR / "listings_clean.parquet"

def transform():
    print(f"[transform] Reading {RAW}")
    df = pd.read_csv(RAW)

    # Standardize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Coerce types
    date_cols = ["last_review"]
    for c in date_cols:
        if c in df.columns:
            df[c] = pd.to_datetime(df[c], errors="coerce").dt.date

    numeric_cols = [
        "price", "minimum_nights", "number_of_reviews",
        "reviews_per_month", "calculated_host_listings_count", "availability_365"
    ]
    for c in numeric_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    # Basic cleaning: drop rows missing critical fields
    df = df.dropna(subset=["id", "name", "host_id", "room_type", "price"])

    # Business filters (example):
    df = df[(df["price"] > 0) & (df["minimum_nights"] >= 1)]

    # Derived fields
    df["is_entire_home"] = (df["room_type"].str.lower() == "entire home/apt").astype(int)

    # Rename to match warehouse schema
    df = df.rename(columns={
        "id": "listing_id",
        "neighbourhood": "neighbourhood",
    })

    # Keep only warehouse columns (order matters)
    keep = [
        "listing_id", "name", "host_id", "neighbourhood", "room_type",
        "price", "minimum_nights", "number_of_reviews", "last_review",
        "reviews_per_month", "calculated_host_listings_count", "availability_365"
    ]
    for k in keep:
        if k not in df.columns:
            df[k] = pd.NA
    df = df[keep]

    print(f"[transform] Writing {OUT}")
    df.to_parquet(OUT, index=False)

if __name__ == "__main__":
    transform()
