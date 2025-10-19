# scripts/load.py
import os
import pathlib
import pandas as pd
from sqlalchemy import create_engine, text

WAREHOUSE_CONN_STR = os.getenv("WAREHOUSE_CONN_STR")
DATA_DIR = pathlib.Path("/opt/airflow/data")
INFILE = DATA_DIR / "processed" / "listings_clean.parquet"

def load():
    print(f"[load] Connecting to warehouse")
    engine = create_engine(WAREHOUSE_CONN_STR, future=True)
    df = pd.read_parquet(INFILE)

    with engine.begin() as conn:
        # Optional: truncate for idempotent daily loads (demo-friendly)
        conn.execute(text("TRUNCATE TABLE airbnb.listings;"))
        df.to_sql(
            "listings",
            con=conn,
            schema="airbnb",
            if_exists="append",
            index=False,
            method="multi",
            chunksize=1000
        )
    print("[load] Load complete")

if __name__ == "__main__":
    load()
