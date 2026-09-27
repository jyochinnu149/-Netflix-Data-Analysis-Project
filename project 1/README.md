# Netflix Data Analysis Project

This project is a complete, beginner-friendly Netflix data analysis portfolio project built from scratch. It uses a Netflix Movies and TV Shows dataset to explore content trends, compare Movies vs TV Shows, inspect countries and ratings, and present business insights through a clean data pipeline and professional visualizations.

## Project Objective

The main goal is to analyze Netflix content patterns and answer business questions such as:

- How many Movies and TV Shows are available?
- Which countries produce the most Netflix content?
- What are the most common ratings and genres?
- How has Netflix content grown over time?
- Which content types dominate the platform?

This project is designed for a B.Tech fresher portfolio and interview preparation, with code that is clean, readable, and easy to explain.

## Problem Statement

Streaming platforms such as Netflix need to understand content performance, user preferences, rating patterns, and geographic content distribution. By analyzing metadata such as title, release year, rating, genre, duration, and country, we can identify content trends and help in strategic decisions such as content acquisition, regional targeting, and catalog planning.

## Dataset

The project uses a Netflix-style dataset containing fields like:

- show_id
- type
- title
- director
- cast
- country
- date_added
- release_year
- rating
- duration
- listed_in
- description

The raw dataset is stored in:

- data/netflix_titles_raw.csv

The cleaned dataset is stored in:

- data/netflix_titles_cleaned.csv

## Project Structure

```text
project-1/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── netflix_titles_raw.csv
│   └── netflix_titles_cleaned.csv
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   └── 02_eda.ipynb
├── scripts/
│   ├── 00_generate_dataset.py
│   ├── 01_data_cleaning.py
│   └── 02_eda.py
├── dashboard/
│   └── powerbi_dashboard_requirements.md
├── visuals/
│   ├── content_type_distribution.png
│   ├── top_countries.png
│   ├── rating_distribution.png
│   ├── release_year_trend.png
│   ├── genre_analysis.png
│   ├── content_age_distribution.png
│   ├── year_month_heatmap.png
│   └── rating_share_pie.png
├── analysis_summary.txt
└── .venv/
```

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Power BI (dashboard concept)

## Dataset and Data Cleaning Process

The raw dataset is generated as a realistic Netflix-style dataset and then cleaned in a structured workflow.

### Cleaning steps

- Remove duplicate rows
- Standardize column names
- Fill missing values using logical defaults
- Convert date strings to proper datetime objects
- Fix inconsistent content types and durations
- Split combined values such as multiple countries and genres
- Create derived columns such as:
  - year_added
  - month_added
  - content_age
  - main_genre
  - duration_minutes

## EDA Process

After cleaning, the project performs exploratory data analysis to answer business questions:

- How many Movies and TV Shows are there?
- What is the share of Movie vs TV Show content?
- Which countries produce the most titles?
- What are the main ratings used by Netflix?
- Which years saw the highest content growth?
- Which genres are most common?
- What is the pattern in content age and addition time?

## Key Visualizations

The project creates professional charts including:

- Bar charts for content type and ratings
- Line charts for release trends
- Histograms for content age distribution
- Heatmap for monthly additions by year
- Bar chart for top countries
- Donut/pie chart for rating share
- Genre analysis visual

## Key Findings

Some expected findings from the generated Netflix-style dataset include:

- Movies are generally more common than TV Shows.
- A few countries dominate Netflix production and distribution trends.
- Certain ratings such as TV-MA and TV-14 appear more frequently.
- Content production increased significantly in recent years.
- A few genres dominate the catalog and repeat across many titles.

## Business Insights

This project can support practical streaming business decisions:

- Invest more in genres with growing demand.
- Prioritize regions that produce popular content.
- Plan releases around high-activity months.
- Balance the catalog with both Movies and TV Shows.
- Understand rating mix to match audience expectations.

## Dashboard Requirements (Power BI / Tableau)

A professional dashboard should include:

- Total Titles
- Movies
- TV Shows
- Countries
- Genres
- Year-wise content trend
- Rating distribution
- Top countries
- Top genres

### Filters

- Content type
- Release year
- Country
- Rating
- Genre

The dashboard requirements file is here:

- dashboard/powerbi_dashboard_requirements.md

## Project Execution

Run the scripts in this order:

```bash
python scripts/00_generate_dataset.py
python scripts/01_data_cleaning.py
python scripts/02_eda.py
```

## Challenges Faced

- Handling inconsistent raw data values
- Correcting missing values without losing important records
- Standardizing fields like countries, genres, and duration
- Presenting clean visualizations while keeping the project easy to understand

## Future Improvements

- Add a real-world Kaggle Netflix dataset
- Build an interactive Streamlit dashboard
- Add SQL-based data analysis queries
- Perform sentiment analysis on descriptions and titles
- Add recommendation-style analysis using user preference patterns

## Interview Ready Summary

This project demonstrates the ability to work on a real-world data problem using Python, Pandas, and EDA workflows. It is suitable for placements because it shows:

- Data cleaning and preprocessing
- Business question formulation
- Data storytelling
- Visualization skills
- Portfolio-ready project structure

## Technical Interview Questions

The project also includes a set of interview questions and answers in the project documentation and final portfolio explanation.

---

This project is intentionally structured to be simple, professional, and explainable for interviews and placement preparation.
