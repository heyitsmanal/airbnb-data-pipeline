# scripts/extract.py
import os
import pathlib
import requests

DATA_DIR = pathlib.Path("/opt/airflow/data")
RAW_DIR = DATA_DIR / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

def download_csv():
    url = os.getenv("EXTERNAL_CSV_URL", "").strip()
    target = RAW_DIR / "listings.csv"

    if url:
        print(f"[extract] Downloading CSV from {url}")
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        target.write_bytes(r.content)
        print(f"[extract] Saved to {target}")
    else:
        # Fallback to sample file if provided
        sample = RAW_DIR / "sample_listings.csv"
        if not sample.exists():
            # minimal sample in case user forgot
            sample.write_text(
                "id,name,host_id,neighbourhood,room_type,price,minimum_nights,number_of_reviews,last_review,reviews_per_month,calculated_host_listings_count,availability_365\n"
                "1001,Cozy Studio,501,Downtown,Entire home/apt,85,2,123,2024-09-12,1.5,2,180\n"
                "1002,Sunny Room,502,Old Town,Private room,45,1,56,2024-08-10,0.8,1,250\n"
                "1003,City Loft,503,Center,Entire home/apt,120,3,240,2025-01-09,2.4,5,90\n"
            )
        sample.replace(target)
        print(f"[extract] Using local sample: {target}")

if __name__ == "__main__":
    download_csv()
