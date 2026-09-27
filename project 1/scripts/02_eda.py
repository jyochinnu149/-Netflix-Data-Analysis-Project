import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
VIS_DIR = ROOT / "visuals"
VIS_DIR.mkdir(exist_ok=True)

INPUT_FILE = DATA_DIR / "netflix_titles_cleaned.csv"
OUTPUT_SUMMARY = ROOT / "analysis_summary.txt"


def load_data():
    df = pd.read_csv(INPUT_FILE)
    print(f"Loaded {len(df)} records from {INPUT_FILE}")
    return df


def save_chart(fig, name):
    fig.tight_layout()
    fig.savefig(VIS_DIR / name, dpi=300, bbox_inches="tight")
    plt.close(fig)


def build_visuals(df):
    sns.set_style("whitegrid")

    # 1. Content type distribution
    type_counts = df["type"].value_counts()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=type_counts.index, y=type_counts.values, palette="Set2", ax=ax)
    ax.set_title("Netflix Content by Type")
    ax.set_xlabel("Content Type")
    ax.set_ylabel("Number of Titles")
    save_chart(fig, "content_type_distribution.png")

    # 2. Top countries
    country_counts = df["country"].str.split(",").explode().str.strip().value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=country_counts.values, y=country_counts.index, palette="viridis", ax=ax)
    ax.set_title("Top Countries Producing Netflix Content")
    ax.set_xlabel("Number of Titles")
    ax.set_ylabel("Country")
    save_chart(fig, "top_countries.png")

    # 3. Rating distribution
    rating_counts = df["rating"].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=rating_counts.index, y=rating_counts.values, palette="magma", ax=ax)
    ax.set_title("Netflix Content by Rating")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Count")
    plt.xticks(rotation=45)
    save_chart(fig, "rating_distribution.png")

    # 4. Release trend by year
    yearly_counts = df.groupby("release_year").size().sort_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, marker="o", ax=ax)
    ax.set_title("Netflix Content Growth by Release Year")
    ax.set_xlabel("Release Year")
    ax.set_ylabel("Titles Released")
    save_chart(fig, "release_year_trend.png")

    # 5. Genre analysis
    genre_counts = df["main_genre"].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=genre_counts.values, y=genre_counts.index, palette="crest", ax=ax)
    ax.set_title("Most Common Genres on Netflix")
    ax.set_xlabel("Count")
    ax.set_ylabel("Genre")
    save_chart(fig, "genre_analysis.png")

    # 6. Content age distribution
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df["content_age"], bins=20, kde=True, color="steelblue", ax=ax)
    ax.set_title("Distribution of Content Age")
    ax.set_xlabel("Content Age (Years)")
    ax.set_ylabel("Frequency")
    save_chart(fig, "content_age_distribution.png")

    # 7. Heatmap: month vs year content additions
    monthly_year = df.groupby(["year_added", "month_added"]).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(monthly_year, cmap="YlGnBu", annot=False, fmt="d", ax=ax)
    ax.set_title("Content Added by Year and Month")
    ax.set_xlabel("Month Added")
    ax.set_ylabel("Year Added")
    save_chart(fig, "year_month_heatmap.png")

    # 8. Pie chart for ratings
    rating_share = df["rating"].value_counts().head(5)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(rating_share.values, labels=rating_share.index, autopct="%1.1f%%", startangle=90)
    ax.set_title("Top 5 Ratings Share")
    save_chart(fig, "rating_share_pie.png")

    print("All visualizations were generated successfully.")


def summary_stats(df):
    total_titles = len(df)
    movie_count = (df["type"] == "Movie").sum()
    tv_count = (df["type"] == "TV Show").sum()
    countries = df["country"].str.split(",").explode().str.strip().nunique() - 1
    top_rating = df["rating"].mode().iloc[0]
    top_genre = df["main_genre"].mode().iloc[0]
    peak_year = df["release_year"].value_counts().idxmax()

    summary = {
        "Total titles": total_titles,
        "Movies": movie_count,
        "TV Shows": tv_count,
        "Unique countries": countries,
        "Top rating": top_rating,
        "Top genre": top_genre,
        "Peak release year": peak_year,
    }

    return summary


def main():
    df = load_data()
    build_visuals(df)
    stats = summary_stats(df)

    with OUTPUT_SUMMARY.open("w", encoding="utf-8") as f:
        for key, value in stats.items():
            f.write(f"{key}: {value}\n")

    print("\nKey findings:")
    for key, value in stats.items():
        print(f"- {key}: {value}")


if __name__ == "__main__":
    main()
