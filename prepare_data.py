
# prepare_data.py - Convert MovieLens ratings.csv + movies.csv into sample_ratings.csv
# Usage:
#   1. Download and unzip ml-latest-small.zip from https://grouplens.org/datasets/movielens/latest/
#   2. Place the "ml-latest-small" folder inside this project directory
#   3. Run: python prepare_data.py

import pandas as pd
from pathlib import Path

ml_dir = Path("ml-latest-small")
ratings_path = ml_dir / "ratings.csv"
movies_path = ml_dir / "movies.csv"
output_path = Path("data/sample_ratings.csv")

if not ratings_path.exists() or not movies_path.exists():
    print("❌ Error: Please put 'ml-latest-small' folder (with ratings.csv, movies.csv) in this directory.")
    exit(1)

ratings = pd.read_csv(ratings_path)
movies = pd.read_csv(movies_path)

merged = pd.merge(ratings, movies, on="movieId")
df = merged[["userId", "title", "rating"]]
df.columns = ["userId", "movie", "rating"]
df.to_csv(output_path, index=False)

print(f"✅ Done! Generated {output_path} with {len(df)} rows.")
