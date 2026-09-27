import numpy as np
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RAW_FILE = DATA_DIR / "netflix_titles_raw.csv"
CLEAN_FILE = DATA_DIR / "netflix_titles_cleaned.csv"


def clean_dataset():
    df = pd.read_csv(RAW_FILE)

    print(f"Initial rows: {len(df)}")
    print(f"Initial columns: {list(df.columns)}")

    # 1. Remove duplicate records
    df = df.drop_duplicates().copy()
    print(f"Rows after dropping duplicates: {len(df)}")

    # 2. Standardize column names
    df.columns = [
        "show_id", "type", "title", "director", "cast", "country",
        "date_added", "release_year", "rating", "duration", "listed_in",
        "description"
    ]

    # 3. Clean string values
    for col in ["type", "title", "director", "cast", "country", "rating", "listed_in", "description"]:
        df[col] = df[col].fillna("Unknown").astype(str).str.strip()

    # Replace placeholder string values caused by missing values in CSV export
    for col, default in {
        "type": "Unknown",
        "title": "Unknown Title",
        "rating": "Not Rated",
        "country": "Unknown",
        "director": "Unknown Director",
        "cast": "Unknown Cast",
        "listed_in": "General",
        "description": "No description available.",
    }.items():
        df[col] = df[col].replace(["nan", "None", "NaN"], default)

    # 4. Handle missing values with practical defaults
    df["director"] = df["director"].replace("Unknown Director", "Unknown Director")
    df["cast"] = df["cast"].replace("Unknown Cast", "Unknown Cast")
    df["country"] = df["country"].replace("Unknown", "Unknown")
    df["rating"] = df["rating"].replace("Not Rated", "Not Rated")
    df["listed_in"] = df["listed_in"].replace("General", "General")
    df["description"] = df["description"].replace("No description available.", "No description available.")

    # 5. Convert date column to proper datetime format
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

    # 6. Standardize content type
    df["type"] = df["type"].str.title().str.replace("Tv Show", "TV Show")
    df["type"] = df["type"].replace({"Unknown": "Movie"})

    # 7. Fix country formatting by splitting multiple country names cleanly
    df["country"] = df["country"].str.replace(r"\s*,\s*", ", ", regex=True)
    df["country"] = df["country"].fillna("Unknown")

    # 8. Separate multiple genres and country names into clean data values
    df["listed_in"] = df["listed_in"].fillna("General")
    df["main_genre"] = df["listed_in"].str.split(",").str[0].str.strip().str.title()

    # 9. Parse duration values and create useful columns
    def extract_runtime(value):
        if pd.isna(value):
            return None
        text = str(value).strip()
        if "min" in text.lower():
            return int(text.lower().replace("min", "").strip())
        if "season" in text.lower():
            try:
                return int(text.lower().split("season")[0].strip())
            except ValueError:
                return None
        return None

    df["duration_minutes"] = df["duration"].apply(extract_runtime)
    df["duration_value"] = df["duration"].str.extract(r"(\d+)")
    df["duration_unit"] = np.where(df["duration"].str.contains("min", case=False, na=False), "Minutes", "Seasons")

    # 10. Create derived columns
    current_year = pd.Timestamp.today().year
    df["year_added"] = df["date_added"].dt.year
    df["month_added"] = df["date_added"].dt.month_name()
    df["content_age"] = current_year - df["release_year"]

    # 11. Remove impossible or invalid years
    df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce").fillna(0).astype(int)
    df = df[df["release_year"] >= 1940].copy()

    # 12. Final data quality check
    df = df.dropna(subset=["title", "type"]).copy()
    df = df.reset_index(drop=True)

    df.to_csv(CLEAN_FILE, index=False)

    print(f"Cleaned rows: {len(df)}")
    print(f"Columns after cleaning: {list(df.columns)}")
    print(f"Missing values after cleaning: \n{df.isna().sum()}\n")
    print(f"Sample cleaned data saved to: {CLEAN_FILE}")


if __name__ == "__main__":
    import numpy as np
    clean_dataset()
