import numpy as np
import pandas as pd
from pathlib import Path


SEED = 42
np.random.seed(SEED)

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

HOLDER_NAMES = [
    "Ariana Sharma", "Rohan Nair", "Priya Menon", "David Kim", "Sofia Rossi",
    "Arjun Patil", "Meera Iyer", "Daniel Wu", "Elena Garcia", "Nikhil Rao",
    "Emma Brown", "Lucas Silva", "Hina Shah", "Samir Khan", "Lena Fischer"
]
DIRECTORS = [
    "Rajiv Singh", "Maya Johnson", "Ankit Mehra", "Lena Foster", "Sanjay Verma",
    "Olivia Martin", "Vikram Sethi", "Nina Patel", "Daniel Cole", "Priya Das",
    "Chris Walker", "Aisha Malik", "Victor Lee", "Laura Hughes", "Haruto Sato"
]
COUNTRIES = [
    "United States", "India", "United Kingdom", "Canada", "France", "Japan", "South Korea",
    "Spain", "Brazil", "Mexico", "Germany", "Australia", "Italy", "Nigeria", "Argentina"
]
GENRES = [
    "Action", "Drama", "Comedy", "Thriller", "Romance", "Documentary", "Crime", "Sci-Fi",
    "Adventure", "Family", "Fantasy", "Mystery", "Horror", "Animation", "Biography"
]
RATINGS = ["TV-MA", "TV-14", "PG-13", "TV-PG", "R", "PG", "TV-Y", "G", "NR", "TV-G"]
TITLE_PREFIXES = [
    "Midnight", "Summer", "Golden", "Silent", "Shadow", "Street", "Ocean", "Hidden", "Falling",
    "Last", "Bright", "Dark", "Wild", "Royal", "Storm", "Young", "Crimson", "Velvet", "London"
]
TITLE_SUFFIXES = [
    "Heights", "Breeze", "River", "Hall", "Circle", "Echo", "Lens", "Dreams", "Signal", "Run",
    "Story", "Trail", "Knights", "Rise", "Island", "Quest", "Night", "Orbit", "Chase", "Focus"
]


def random_title(prefixes, suffixes):
    prefix = np.random.choice(prefixes)
    suffix = np.random.choice(suffixes)
    return f"{prefix} {suffix}"


def random_country():
    return np.random.choice(COUNTRIES)


def random_genre_list():
    selected = np.random.choice(GENRES, size=np.random.randint(1, 4), replace=False)
    return ", ".join(selected)


def random_duration(content_type):
    if content_type == "Movie":
        return f"{np.random.randint(70, 210)} min"
    seasons = np.random.randint(1, 9)
    return f"{seasons} Seasons"


def random_date():
    year = np.random.randint(2015, 2025)
    month = np.random.randint(1, 13)
    day = np.random.randint(1, 28)
    return pd.Timestamp(year=year, month=month, day=day)


rows = []
for index in range(2500):
    content_type = np.random.choice(["Movie", "TV Show"])
    title = random_title(TITLE_PREFIXES, TITLE_SUFFIXES)
    if index < 20:
        title = f"{content_type} {index + 1}"

    row = {
        "show_id": f"s{index + 1:05d}",
        "type": content_type,
        "title": title,
        "director": np.random.choice(DIRECTORS),
        "cast": ", ".join(np.random.choice(HOLDER_NAMES, size=np.random.randint(2, 5), replace=False)),
        "country": random_country(),
        "date_added": random_date(),
        "release_year": np.random.randint(2008, 2025),
        "rating": np.random.choice(RATINGS),
        "duration": random_duration(content_type),
        "listed_in": random_genre_list(),
        "description": f"{title} explores a world of emotion, conflict, and strong character arcs in a gripping {content_type.lower()} format.",
    }
    rows.append(row)

# add a few duplicates to simulate real-world data issues
for duplicate_index in range(20):
    rows.append(rows[duplicate_index].copy())

# add missing values to mimic imperfect raw data
for row in rows:
    if np.random.rand() < 0.08:
        row["director"] = np.nan
    if np.random.rand() < 0.10:
        row["cast"] = np.nan
    if np.random.rand() < 0.12:
        row["country"] = np.nan
    if np.random.rand() < 0.07:
        row["rating"] = np.nan
    if np.random.rand() < 0.04:
        row["date_added"] = np.nan

# add inconsistent values to test cleaning logic
rows[0]["country"] = "United States, United Kingdom"
rows[1]["director"] = "  Maya Johnson  "
rows[2]["duration"] = "2 Seasons"
rows[3]["duration"] = "128 min"
rows[4]["date_added"] = "2024/09/01"

# Ensure final file is not too large for the portfolio but useful for analysis
netflix_df = pd.DataFrame(rows)
netflix_df.to_csv(DATA_DIR / "netflix_titles_raw.csv", index=False)
print(f"Created {len(netflix_df)} raw rows in {DATA_DIR / 'netflix_titles_raw.csv'}")
